import { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { useLocation, useNavigate } from "react-router-dom";
import useApiRequest from "../../hooks/useApiRequest.js";
import { loginUser } from "../../store/slices/loggedInUser.js";
import { ButtonsStyle } from "../../styles/buttons.style.js";
import {
  AlreadyHaveAnAccountNavLink,
  AuthForm,
  AuthFormContainer,
  ErrorMessage,
  FormTitle,
  InputFieldContainer,
  ResetNavLink,
} from "../Layout/Layout.style.js";

function SignInSection() {
  const [user, setUser] = useState({ username: "", password: "" });
  const { sendRequest, data, error } = useApiRequest();
  const location = useLocation();
  const navigate = useNavigate();
  const dispatch = useDispatch();

  const handleInput = (e) => {
    setUser({ ...user, [e.target.id]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    sendRequest("post", "auth/access-token", user, true);
  };

  useEffect(() => {
    if (data !== null) {
      const accessToken = data.access_token;
      dispatch(loginUser({ accessToken: accessToken }));
      localStorage.setItem("auth-token", accessToken);
      const from = location.state?.from || { pathname: "/profile" };
      navigate(from);
    }
  }, [data, dispatch, navigate, location]);

  return (
    <AuthFormContainer>
      <AuthForm onSubmit={handleSubmit}>
        <div className={"input-container"}>
          <FormTitle>Sign In</FormTitle>
          <InputFieldContainer>
            <div className={"input-wrapper"}>
              <input
                placeholder="Email"
                type="email"
                required
                onChange={handleInput}
                id="username"
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
            <ResetNavLink to="/password-reset/">Forgot password?</ResetNavLink>
            {error?.password && <ErrorMessage>{error.password}</ErrorMessage>}
          </InputFieldContainer>
          {error?.detail && <p className={"error-message"}>{error.detail}</p>}
        </div>
        <div className={"form-footer"}>
          <ButtonsStyle style={{ marginTop: "2.5rem" }} onClick={handleSubmit}>
            Sign In
          </ButtonsStyle>
        </div>
        <AlreadyHaveAnAccountNavLink style={{ marginTop: "2rem" }} to="/signup">
          New to Bible Reading Tracker?
          <br /> Create an account →
        </AlreadyHaveAnAccountNavLink>
      </AuthForm>
    </AuthFormContainer>
  );
}

export default SignInSection;
