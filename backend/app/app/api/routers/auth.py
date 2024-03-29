import logging

from fastapi import APIRouter, Body, HTTPException, status

from app import crud
from app.api.deps import FormDataDep, SessionDep
from app.api.exceptions import (
    active_user_exception,
    credentials_exception,
    email_registered_exception,
    inactive_user_exception,
    user_not_found_exception,
)
from app.core.token_utils import (
    decode_token,
    generate_password_reset_validation_token,
    generate_registration_validation_token,
    generate_tokens_response,
)
from app.models.auth import (
    AuthCodeUpdate,
    CodeType,
    NewPassword,
    RefreshTokenRequest,
    TokensResponse,
    VerifyAccessTokenRequest,
)
from app.models.msg import Message
from app.models.user import UserCreateFromUser, UserRecoverPassword, UserUpdatePassword
from app.utils.celery_tasks import (
    send_new_account_email,
    send_reset_password_email,
    send_test_email,
)

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/access-token")
async def login_access_token(
    session: SessionDep, form_data: FormDataDep
) -> TokensResponse:
    """Get an access token for future requests using email and password."""
    user = await crud.user.authenticate(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password"
        )
    if not user.is_active:
        raise inactive_user_exception
    return generate_tokens_response(str(user.id))


@router.post("/access-token/verification")
async def verify_access_token(
    session: SessionDep, token: VerifyAccessTokenRequest
) -> None:
    """Verify if an access token is valid."""
    user_id = decode_token(token.access_token, CodeType.ACCESS)
    if not user_id or not await crud.user.get(session, id=user_id):
        raise credentials_exception


@router.post("/refresh-token")
async def refresh_token(
    session: SessionDep, token: RefreshTokenRequest
) -> TokensResponse:
    """Get an access token using a refresh token."""
    user_id = decode_token(token.refresh_token, CodeType.REFRESH)
    if user_id and await crud.user.get(session, id=user_id):
        return generate_tokens_response(user_id)
    raise credentials_exception


@router.post("/registration")
async def register_user(session: SessionDep, data: UserCreateFromUser) -> Message:
    """Register new user."""
    email = data.email
    if user := await crud.user.get_by_email(session, email):
        if user.is_active:
            raise email_registered_exception
    else:
        user = await crud.user.create_from_user(session, data)

    auth_code = await crud.auth_code.create_for_user(session, user)
    token = generate_registration_validation_token(auth_code.code)
    send_new_account_email.delay(email, token)
    return Message(msg="New account email sent")


@router.post("/registration/validation")
async def validate_register_user(
    session: SessionDep, token: str = Body(..., embed=True)
) -> Message:
    """Validate registration token and activate the account."""
    code = decode_token(token, CodeType.REGISTER)
    auth_code = await crud.auth_code.get_by_code(session, code)
    if not auth_code or auth_code.is_used:
        raise credentials_exception

    user = auth_code.user
    if user.is_active:
        raise active_user_exception

    await crud.user.activate(session, user)
    await crud.auth_code.update(session, auth_code, AuthCodeUpdate(is_used=True))
    return Message(msg="Account activated successfully")


@router.post("/password-reset")
async def reset_password(session: SessionDep, data: UserRecoverPassword) -> Message:
    """Send password reset email."""
    email = data.email
    user = await crud.user.get_by_email(session, email)
    if not user:
        raise user_not_found_exception
    if not user.is_active:
        raise inactive_user_exception

    auth_code = await crud.auth_code.create_for_user(session, user)
    token = generate_password_reset_validation_token(auth_code.code)
    send_reset_password_email.delay(email, token)
    return Message(msg="Password recovery email sent")


@router.post("/password-reset/validation")
async def validate_reset_password(session: SessionDep, body: NewPassword) -> Message:
    """Validate password reset token and reset the password."""
    code = decode_token(body.token, CodeType.PASSWORD_RESET)
    auth_code = await crud.auth_code.get_by_code(session, code)
    if auth_code is None or auth_code.is_used:
        raise credentials_exception

    user = auth_code.user
    if not user:
        raise user_not_found_exception
    if not user.is_active:
        raise inactive_user_exception

    await crud.user.update_from_user(
        session, user, UserUpdatePassword(password=body.new_password)
    )
    await crud.auth_code.update(session, auth_code, AuthCodeUpdate(is_used=True))
    return Message(msg="Password updated successfully")


@router.post("/test-email")
async def test_email(data: UserRecoverPassword) -> Message:
    """Register new user."""
    send_test_email.delay(data.email)
    return Message(msg="Test email sent")
