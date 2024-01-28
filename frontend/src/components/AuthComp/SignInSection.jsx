import { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { useLocation, useNavigate } from "react-router-dom";
import useApiRequest from "../../hooks/useApiRequest.js";
import { loginUser } from "../../store/slices/loggedInUser.js";
import { ButtonsStyle } from "../../styles/globalStyles.js";
import {
  AlreadyHaveAnAccountNavLink,
  AuthForm,
  ErrorMessage,
  FormTitle,
  InputFieldContainer,
  ResetNavLink,
} from "./AuthComp.style.js";

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
      const from = location.state?.from || { pathname: "/" };
      navigate(from);
    }
  }, [data, dispatch, navigate, location]);

  return (
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
          {error?.password && <ErrorMessage>{error.password}</ErrorMessage>}
        </InputFieldContainer>
        {error?.detail && <p className={"error-message"}>{error.detail}</p>}
      </div>
      <ButtonsStyle onClick={handleSubmit}>Sign In</ButtonsStyle>
      <ResetNavLink to="/password-reset/">Forgot password?</ResetNavLink>
      <AlreadyHaveAnAccountNavLink to="/signup">
        New to Bible Reading Tracker?
        <br /> Create an account →
      </AlreadyHaveAnAccountNavLink>
    </AuthForm>
  );
}

export default SignInSection;
