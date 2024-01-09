import datetime

from jose import JWTError, jwt

from app.core.config import settings
from app.models.auth import CodeType, JWTTokenPayload, TokensResponse

JWT_ALGORITHM = "HS256"


def generate_tokens_response(subject: str | int) -> TokensResponse:
    """Generate tokens and return AccessTokenResponse."""
    access_token = create_token(
        subject, settings.ACCESS_TOKEN_EXPIRE_HOURS, CodeType.ACCESS
    )
    refresh_token = create_token(
        subject, settings.REFRESH_TOKEN_EXPIRE_HOURS, CodeType.REFRESH
    )
    return TokensResponse(access_token=access_token, refresh_token=refresh_token)


def create_token(sub: str | int, exp_hours: float, code_type: CodeType) -> str:
    """Create jwt access or refresh token for user.

    Args:
    ----
        sub: anything unique to user, id or email etc. Need to be converted to a string.
        exp_hours: expire time in hours.
        code_type: code type.
    """
    now = datetime.datetime.now(tz=datetime.UTC)
    exp = now + datetime.timedelta(hours=exp_hours)

    claims = {
        **JWTTokenPayload(
            sub=str(sub), exp=exp, nbf=now, code_type_value=code_type.value
        ).model_dump()
    }
    return jwt.encode(claims, settings.SECRET_KEY, JWT_ALGORITHM)


def decode_token(token: str, code_type: CodeType) -> str:
    """Decode JWT token and return the subject."""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[JWT_ALGORITHM])
    except JWTError:
        return None

    token_data = JWTTokenPayload(**payload)
    if code_type.value != token_data.code_type_value:
        return None

    return token_data.sub


def generate_registration_validation_token(code: str) -> str:
    """Create registration validation token with email as subject."""
    return create_token(
        code, settings.EMAIL_VALIDATION_TOKEN_EXPIRE_HOURS, CodeType.REGISTER
    )


def generate_password_reset_validation_token(code: str) -> str:
    """Create password reset validation token with email as subject."""
    return create_token(
        code, settings.EMAIL_VALIDATION_TOKEN_EXPIRE_HOURS, CodeType.PASSWORD_RESET
    )
