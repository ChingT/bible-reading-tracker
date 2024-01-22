import styled from "styled-components";
import { ButtonsStyle } from "../../../styles/buttons.style.js";

export const InputWrapper = styled.div`
  padding: 2.5rem 3.8rem;

  form {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(10rem, 1fr));
    gap: 2.4rem;
    @media (min-width: 42rem) {
      grid-template-columns: repeat(auto-fill, minmax(14rem, 1fr));
    }
  }

  .input-field {
    font-size: 18px;
    display: flex;
    flex-direction: column;
    gap: 0.4rem;
    width: 100%;
  }

    label {
      opacity: 0.5;
      font-size: 0.75rem;
    }

    input,
    textarea {
      background: none;
      border: none;
      font: inherit;

      border-bottom: 2px solid rgba(0, 0, 0, 0.2);
      padding-bottom: 1em;
      resize: none;
    }

    > button {
      ${ButtonsStyle}
    }
  }

  .things-liked {
    grid-column: 1 / -1;
    margin-top: 2.5rem;

    .input-submit-wrapper {
      display: flex;
      gap: 2rem;
      width: 100%;
      margin-top: 2rem;

      input {
        width: 100%;
      }

      button {
        ${ButtonsStyle}
      }
    }
  }
`;

export const CustomFileInputButton = styled.div`
  position: relative;

  input[type="file"] {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    opacity: 0;
  }
`;
