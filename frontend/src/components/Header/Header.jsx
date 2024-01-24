import { useState } from "react";
import { useSelector } from "react-redux";
import { Link, useLocation } from "react-router-dom";
import avatarImage from "../../assets/avatar.svg";
import MenuDot from "../../assets/menu_dots.svg";
import { ButtonsStyle } from "../../styles/globalStyles.js";
import {
  Avatar,
  ContainerLeft,
  ContainerRight,
  HeaderContainer,
  MenuContainer,
  NavbarLink,
  StyledH1,
} from "./Header.style.js";
import NavigationActionsContainer from "./HeaderActionsContainer.jsx";

const Header = () => {
  const isLoggedIn = useSelector((store) => store.loggedInUser.accessToken);

  const [showMenu, setShowMenu] = useState(false);

  const location = useLocation();
  const isLoginPage = location.pathname === "/signin";
  const isSignUpPage = location.pathname === "/signup";

  const signUpButton = (
    <Link to="/signup">
      <ButtonsStyle>Sign Up</ButtonsStyle>
    </Link>
  );

  const signInButton = (
    <Link to="/signin">
      <ButtonsStyle>Sign In</ButtonsStyle>
    </Link>
  );
  const menuButton = (
    <MenuContainer>
      <img src={MenuDot} alt="Menu" onClick={() => setShowMenu(!showMenu)} />
      {showMenu && <NavigationActionsContainer setShowMenu={setShowMenu} />}
    </MenuContainer>
  );

  const profileButton = (
    <Link to={"/profile"}>
      <Avatar src={avatarImage} alt="Avatar" />
    </Link>
  );

  return (
    <HeaderContainer>
      <ContainerLeft>
        <NavbarLink to="/">
          <StyledH1>Bible Reading Tracker</StyledH1>
        </NavbarLink>
      </ContainerLeft>

      <ContainerRight>
        {isLoggedIn ? (
          <>
            {profileButton}
            {menuButton}
          </>
        ) : (
          <>
            {isLoginPage && signUpButton}
            {(isSignUpPage || (!isLoginPage && !isSignUpPage)) && signInButton}
          </>
        )}
      </ContainerRight>
    </HeaderContainer>
  );
};

export default Header;
