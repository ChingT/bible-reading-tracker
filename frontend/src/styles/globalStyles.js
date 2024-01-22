import styled, { createGlobalStyle } from "styled-components";

const GlobalStyle = createGlobalStyle`
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  body {
    width: 100vw;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  #root {
    min-height: calc(100vh - 96px);
    height: 100%;
    width: 100vw;
    background-size: 24px 24px;
    overflow-x: hidden;
    display: flex;
    flex-direction: column;
    font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
  }

  main {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
  min-height: calc(100vh - ${(props) => props.theme.header_height});
  max-height: calc(100vh - ${(props) => props.theme.header_height});
  overflow-y: auto;
  margin-top: ${(props) => props.theme.header_height};
  }


  a {
    text-decoration: none;
    color: inherit
  }

  input::placeholder, textarea::placeholder {
    color: #333;
  }
`;

export const CardWithShadowStyles = styled.div`
  box-shadow:
    0px 0px 1px rgba(0, 0, 0, 0.2),
    0px 10px 20px rgba(0, 0, 0, 0.05);
  width: 100%;
  height: 100%;
  background-color: white;
  border-radius: 0.3rem;
`;

export const CheckMark = styled.img`
  width: 5rem;
  aspect-ratio: 1/1;
  margin-bottom: 2rem;
  animation: scaleIn 400ms ease;

  @keyframes scaleIn {
    0% {
      transform: scale(0);
    }
    80% {
      transform: scale(1.3) rotate(-10deg);
    }
    100% {
      transform: scale(1) rotate(0);
    }
  }
`;

export default GlobalStyle;
