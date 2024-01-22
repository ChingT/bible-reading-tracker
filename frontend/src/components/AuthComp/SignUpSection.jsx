import { useState } from "react";
import { useNavigate } from "react-router-dom";
import useApiRequest from "../../hooks/useApiRequest.js";
import { ButtonsStyle } from "../../styles/buttons.style.js";
import {
  AlreadyHaveAnAccountNavLink,
  AuthForm,
  AuthFormContainer,
  ErrorMessage,
  FormTitle,
  InputFieldContainer,
} from "../Layout/Layout.style.js";

function SignUpSection() {
  const [userEmail, setEmail] = useState("");
  const navigate = useNavigate();
  const { sendRequest, error, data } = useApiRequest("noAuth");

  const handleSignUpClick = async (e) => {
    e.preventDefault();
    sendRequest("post", "auth/registration/", { email: userEmail });
  };

  if (data !== null) {
    localStorage.setItem("registered_email", userEmail);
    navigate("/congratulations");
  }

  return (
    <AuthFormContainer>
      <AuthForm>
        <div className={"input-container"}>
          <FormTitle>Sign Up</FormTitle>
          <InputFieldContainer>
            <div className={"input-wrapper"}>
              <input
                placeholder="Email"
                type="email"
                value={userEmail}
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>
            {error?.email && <ErrorMessage>{error.email}</ErrorMessage>}
          </InputFieldContainer>
          {error?.detail && <ErrorMessage>{error.detail}</ErrorMessage>}
        </div>
        <div>
          <ButtonsStyle
            style={{ marginBottom: "5rem" }}
            onClick={handleSignUpClick}
          >
            Sign Up
          </ButtonsStyle>
        </div>
      </AuthForm>
      <AlreadyHaveAnAccountNavLink
        to="/signin"
        style={{ marginTop: "-5rem", marginBottom: "1rem" }}
      >
        Already have an account? Sign in →
      </AlreadyHaveAnAccountNavLink>
    </AuthFormContainer>
  );
}

export default SignUpSection;
