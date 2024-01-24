import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import useApiRequest from "../../hooks/useApiRequest.js";
import { ButtonsStyle } from "../../styles/globalStyles.js";
import {
  AuthForm,
  AuthFormContainer,
  ErrorMessage,
  FormTitlePasswordReset,
  InputField,
} from "./AuthComp.style.js";

export default function PasswordResetRequest() {
  const [userEmail, setEmail] = useState("");
  const { sendRequest, error, data } = useApiRequest();
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
        </div>
        <ButtonsStyle onClick={handlePasswordResetRequest}>
          Send password reset email
        </ButtonsStyle>
      </AuthForm>
    </AuthFormContainer>
  );
}
