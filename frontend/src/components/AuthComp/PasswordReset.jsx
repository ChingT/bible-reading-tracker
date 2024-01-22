import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import useApiRequest from "../../hooks/useApiRequest.js";
import { ButtonsStyle } from "../../styles/buttons.style.js";
import {
  AlreadyHaveAnAccountNavLink,
  AuthForm,
  AuthFormContainer,
  ErrorMessage,
  FormTitlePasswordReset,
  InputField,
} from "../Layout/Layout.style.js";

export default function PasswordResetRequest() {
  const [userEmail, setEmail] = useState("");
  const { sendRequest, error, data } = useApiRequest("noAuth");
  const navigate = useNavigate();

  const handlePasswordResetRequest = async (e) => {
    e.preventDefault();
    sendRequest("post", "auth/password-reset/", { email: userEmail });
  };

  useEffect(() => {
    if (data !== null) {
      navigate("/password-reset-validation");
    }
  }, [data, navigate]);
  return (
    <AuthFormContainer>
      <AuthForm>
        <div className={"input-container"}>
          <FormTitlePasswordReset>
            Password Reset Request
          </FormTitlePasswordReset>
          <InputField>
            <div className={"input-wrapper"}>
              <input
                placeholder="Email"
                type="email"
                value={userEmail}
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>
            {error?.email && <ErrorMessage>{error.email}</ErrorMessage>}
          </InputField>
          <ButtonsStyle
            style={{ marginTop: "1rem" }}
            onClick={handlePasswordResetRequest}
          >
            Send password reset email
          </ButtonsStyle>
        </div>
        <AlreadyHaveAnAccountNavLink
          to="/password-reset-validation"
          style={{ marginTop: "-5rem" }}
        >
          Got validation code already? <br />
          Validate here →
        </AlreadyHaveAnAccountNavLink>
      </AuthForm>
    </AuthFormContainer>
  );
}
