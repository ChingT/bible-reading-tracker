import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import useApiRequest from "../../hooks/useApiRequest.js";
import { ButtonsStyle } from "../../styles/buttons.style.js";
import {
  AuthForm,
  AuthFormContainer,
  ErrorMessage,
  FormTitle,
  InputFieldContainer,
} from "../Layout/Layout.style.js";
import InputField from "./InputField.jsx";

const VerificationSection = () => {
  const registeredEmail = localStorage.getItem("registered_email");
  const [userData, setUserData] = useState({ email: registeredEmail });
  const navigate = useNavigate();

  const handleInput = (e) => {
    setUserData({ ...userData, [e.target.id]: e.target.value });
  };

  const { sendRequest, error, data } = useApiRequest();

  const handleValidationSubmit = (e) => {
    e.preventDefault();
    sendRequest("patch", "auth/registration/validation/", userData);
  };

  useEffect(() => {
    if (data !== null) {
      localStorage.removeItem("registered_email");
      navigate("/signin");
    }
  }, [navigate, data]);

  return (
    <AuthFormContainer>
      <AuthForm className="activation-form" $cols={2}>
        <div className="input-container">
          <FormTitle>Verification</FormTitle>
          <InputField
            placeholder="Validation Code"
            error={error}
            type="text"
            userData={userData}
            id={"code"}
            handleInput={handleInput}
            span={2}
          />

          <InputField
            type="email"
            userData={userData}
            id={"email"}
            error={error}
            handleInput={handleInput}
            placeholder="Email"
          />

          <InputField
            userData={userData}
            id={"username"}
            error={error}
            placeholder="Username"
            handleInput={handleInput}
            lplaceholder="Username"
          />

          <InputField
            placeholder="First Name"
            userData={userData}
            error={error}
            handleInput={handleInput}
            id={"first_name"}
          />
          <InputField
            placeholder="Last Name"
            userData={userData}
            error={error}
            id={"last_name"}
            handleInput={handleInput}
          />

          <InputField
            userData={userData}
            placeholder="Password"
            error={error}
            id={"password"}
            handleInput={handleInput}
            type={"password"}
          />

          <InputField
            userData={userData}
            placeholder="Password Repeat"
            error={error}
            id={"password_repeat"}
            handleInput={handleInput}
            type={"password"}
          />
          {error?.non_field_errors && (
            <ErrorMessage>{error.non_field_errors}</ErrorMessage>
          )}
          {error?.detail && <ErrorMessage>{error.detail}</ErrorMessage>}
        </div>
        <div>
          <InputFieldContainer $span={2}>
            <ButtonsStyle
              style={{ marginTop: "3rem" }}
              onClick={handleValidationSubmit}
            >
              Complete
            </ButtonsStyle>
          </InputFieldContainer>
        </div>
      </AuthForm>
    </AuthFormContainer>
  );
};

export default VerificationSection;
