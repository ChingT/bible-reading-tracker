import { Outlet } from "react-router-dom";
import Header from "../Header/Header.jsx";
import { GeneralContainer } from "./Layout.style.js";

const Layout = () => {
  return (
    <>
      <Header />
      <GeneralContainer>
        <Outlet />
      </GeneralContainer>
    </>
  );
};

export default Layout;
