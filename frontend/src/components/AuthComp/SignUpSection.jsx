import { useState } from "react";
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
  const [user, setUser] = useState({
    email: "",
    password: "",
    display_name: "",
  });

  const { sendRequest, error } = useApiRequest();

  const handleInput = (e) => {
    setUser({ ...user, [e.target.id]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    sendRequest("post", "auth/registration", user);
  };

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
                required
                onChange={handleInput}
                id="email"
              />
            </div>
            {error?.email && <ErrorMessage>{error.email}</ErrorMessage>}
          </InputFieldContainer>
          <InputFieldContainer>
            <div className={"input-wrapper"}>
              <input
                placeholder="Password"
                type="password"
                required
                onChange={handleInput}
                id="password"
              />
            </div>
            {error?.password && <ErrorMessage>{error.password}</ErrorMessage>}
          </InputFieldContainer>
          <InputFieldContainer>
            <div className={"input-wrapper"}>
              <input
                placeholder="Your Name"
                type="text"
                required
                onChange={handleInput}
                id="display_name"
              />
            </div>
            {error?.display_name && (
              <ErrorMessage>{error.display_name}</ErrorMessage>
            )}
          </InputFieldContainer>
        </div>
        <div>
          <ButtonsStyle onClick={handleSubmit}>Sign Up</ButtonsStyle>
        </div>
      </AuthForm>
      <AlreadyHaveAnAccountNavLink to="/signin">
        Already have an account? Sign in →
      </AlreadyHaveAnAccountNavLink>
    </AuthFormContainer>
  );
}

export default SignUpSection;
