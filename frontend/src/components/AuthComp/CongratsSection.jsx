import { Link } from "react-router-dom";
import { ButtonsStyle } from "../../styles/buttons.style.js";
import {
  AuthForm,
  AuthFormContainer,
  ConfirmationText,
  FormTitle,
} from "../Layout/Layout.style.js";

function CongratsSection() {
  const userEmail = localStorage.getItem("registered_email");

  return (
    <AuthFormContainer>
      <AuthForm>
        <div className={"input-container"}>
          <FormTitle>Congratulations!</FormTitle>
          <ConfirmationText>
            We've sent a confirmation mail to your email.
            <br />
            {userEmail}
          </ConfirmationText>
        </div>
        <div>
          <Link to="/verification">
            <ButtonsStyle>Continue</ButtonsStyle>
          </Link>
        </div>
      </AuthForm>
    </AuthFormContainer>
  );
}

export default CongratsSection;
