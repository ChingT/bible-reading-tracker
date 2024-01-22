import TimeAgo from "javascript-time-ago";
import en from "javascript-time-ago/locale/en.json";
import ReactDOM from "react-dom/client";
import { Provider } from "react-redux";
import { ThemeProvider } from "styled-components";
import App from "./App.jsx";
import store from "./store/store.js";
import GlobalStyle from "./styles/globalStyles.js";
import theme from "./styles/theme.js";

TimeAgo.addDefaultLocale(en);

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <Provider store={store}>
    <ThemeProvider theme={theme}>
      <GlobalStyle />
      <App />
    </ThemeProvider>
  </Provider>
);
