import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import useApiRequest from "../../hooks/useApiRequest.js";
import { ButtonsStyle } from "../../styles/buttons.style.js";
import {
  AuthForm,
  AuthFormContainer,
  ErrorMessage,
  FormTitlePasswordReset,
  InputField,
} from "../Layout/Layout.style.js";

function PasswordResetValidation() {
  const [userData, setUserData] = useState({
    email: "",
    code: "",
    password: "",
    password_repeat: "",
  });
  const { sendRequest, error, data } = useApiRequest("noAuth");
  const navigate = useNavigate();

  const handleValidationSubmit = (e) => {
    e.preventDefault();
    sendRequest("patch", "auth/password-reset/validation/", userData);
  };

  const handleInput = (e) => {
    setUserData({ ...userData, [e.target.id]: e.target.value });
  };

  useEffect(() => {
    if (data !== null) {
      navigate("/signin");
    }
  }, [data, navigate]);

  return (
    <AuthFormContainer>
      <AuthForm>
        <div className={"input-container"}>
          <FormTitlePasswordReset>
            Password Reset Validation
          </FormTitlePasswordReset>
          <InputField>
            <div className={"input-wrapper"}>
              <input
                id="email"
                placeholder="Email"
                type="email"
                value={userData.email}
                onChange={handleInput}
              />
            </div>
          </InputField>
          <InputField>
            <div className={"input-wrapper"}>
              <input
                id="code"
                placeholder="Validation Code"
                type="text"
                value={userData.code}
                onChange={handleInput}
              />
            </div>
          </InputField>
          <InputField>
            <div className={"input-wrapper"}>
              <input
                id="password"
                placeholder="New Password"
                type="password"
                value={userData.password}
                onChange={handleInput}
              />
            </div>
          </InputField>
          <InputField>
            <div className={"input-wrapper"}>
              <input
                id="password_repeat"
                placeholder="Repeat Password"
                type="password"
                value={userData.password_repeat}
                onChange={handleInput}
              />
            </div>
          </InputField>
        </div>
        {error?.non_field_errors && (
          <ErrorMessage>{error.non_field_errors}</ErrorMessage>
        )}
        {error?.detail && <ErrorMessage>{error.detail}</ErrorMessage>}
        <div>
          <ButtonsStyle
            style={{ marginTop: "2.7rem" }}
            onClick={handleValidationSubmit}
          >
            Reset Password
          </ButtonsStyle>
        </div>
      </AuthForm>
    </AuthFormContainer>
  );
}

export default PasswordResetValidation;
