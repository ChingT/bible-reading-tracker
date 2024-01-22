import { NavLink } from "react-router-dom";
import styled from "styled-components";

export const AuthFormContainer = styled.div`
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
`;

export const AuthForm = styled.form`
  width: 27%;
  height: 40%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  padding: 20px;
  margin-top: 7rem;

  .input-container {
    flex: 2;
    display: grid;
    align-content: flex-start;
    justify-items: center;
    grid-template-columns: 1fr;
    gap: 2rem;
    @media (${(props) => props.theme.breakPoints.md}) {
      grid-template-columns: repeat(
        ${(props) => (props.$cols ? props.$cols : 1)},
        1fr
      );
    }

    .input-wrapper input::placeholder {
      color: ${(props) => props.theme.fontColors.primary};
      font-size: 18px;
    }
  }
`;

export const FormTitle = styled.h2`
  font-size: 2.5rem;
  font-weight: 500;
  text-align: center;
  margin-bottom: 0.5em;
  grid-column: 1/-1;
`;

export const FormTitlePasswordReset = styled.h2`
  font-size: 2rem;
  font-weight: 500;
  max-width: 80%;
  text-align: center;
  margin-bottom: 0.5em;
  grid-column: 1/-1;
`;

export const InputFieldContainer = styled.div`
  grid-column: 1 / ${(props) => (props.$span ? -1 : "unset")};
  width: 100%;

  label {
    text-transform: capitalize;
    color: ${(props) => props.theme.fontColors.heroPageSecondaryColor};
  }

  .input-wrapper {
    position: relative;
    border-bottom: 2px solid rgba(0, 0, 0, 0.1);
    display: flex;
    align-items: center;
    gap: 1.5rem;
    font-style: italic;

    input {
      border: none;
      flex: 1 1 24rem;
      padding: 1rem 0.25rem;
      font: inherit;
      background-size: 24px 24px;

      &:focus {
        outline: 2px solid
          ${(props) => props.theme.backgroundColors.impactIconSelected};
      }
    }
  }
`;

export const InputField = styled.div`
  grid-column: 1 / ${(props) => (props.$span ? -1 : "unset")};
  width: 70%;

  label {
    text-transform: capitalize;
    color: ${(props) => props.theme.fontColors.heroPageSecondaryColor};
  }

  .input-wrapper {
    position: relative;
    border-bottom: 2px solid rgba(0, 0, 0, 0.1);
    display: flex;
    align-items: center;
    gap: 1.5rem;
    font-style: italic;

    input {
      border: none;
      flex: 1 1 18rem;
      padding: 1rem 0.25rem;
      font: inherit;
      background-size: 24px 24px;

      &:focus {
        outline: 2px solid
          ${(props) => props.theme.backgroundColors.impactIconSelected};
      }
    }
  }
`;

export const ConfirmationText = styled.p`
  text-align: center;
  line-height: 1.6;
  font-size: 18px;
  margin-bottom: 2rem;
`;

export const ErrorMessage = styled.p`
  color: red;
  font-size: 16px;
  margin-top: 0.2rem;
`;

export const ResetNavLink = styled(NavLink)`
  text-decoration: underline;

  &:hover {
    text-decoration-color: ${(props) => props.theme.ResetPasswordColors.color};
    color: ${(props) => props.theme.ResetPasswordColors.color};
  }
`;

export const AlreadyHaveAnAccountNavLink = styled(NavLink)`
  text-decoration: underline;
  line-height: 1.4rem;
  text-align: center;

  &:hover {
    text-decoration-color: ${(props) => props.theme.ResetPasswordColors.color};
    color: ${(props) => props.theme.ResetPasswordColors.color};
  }
`;
