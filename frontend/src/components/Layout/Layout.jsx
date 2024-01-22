import { Outlet } from "react-router-dom";
import styled from "styled-components";
import Navigation from "../Navigation/Navigation.jsx";

const AuthenticationContainer = styled.div`
  display: flex;
  flex-direction: column;
  padding-top: 1rem;
  height: 100%;
  width: 100%;
`;

const HomePageContainer = styled.div`
  display: flex;
  flex-direction: column;
  height: 100vh;

  > div {
    width: 100%;
    height: 100%;
  }

  @media (${(props) => props.theme.breakPoints.md}) {
    flex-direction: row;

    ${AuthenticationContainer} {
      width: 100%;
    }
  }
`;

const Layout = () => {
  return (
    <>
      <Navigation />
      <HomePageContainer>
        <AuthenticationContainer>
          <Outlet />
        </AuthenticationContainer>
      </HomePageContainer>
    </>
  );
};

export default Layout;
