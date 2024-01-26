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
    height: 100vh;
    min-height: 100vh;
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

  header {
  height: ${(props) => props.theme.header_height};
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow:
    0px 0px 1px rgba(0, 0, 0, 0.2),
    0px 10px 20px rgba(0, 0, 0, 0.05);
  position: fixed;
  top: 0;
  z-index: 10;
  padding: 0 2rem;
  border-bottom: solid rgba(0, 119, 191, 1) 1px;
  background-size: 24px 24px;
  }

  a {
    text-decoration: none;
    color: inherit
  }

  input::placeholder, textarea::placeholder {
    color: #333;
  }
`;

export default GlobalStyle;

export const ButtonsStyle = styled.button`
  background-color: ${(props) => props.theme.colors.primary};
  color: ${(props) => props.theme.fontColors.button};
  border-radius: 10px;
  box-shadow: rgba(0, 0, 0, 0.25);
  padding: 10px 20px 10px 20px;
  cursor: pointer;
  font-size: 19px;
  font-weight: 600;
`;
