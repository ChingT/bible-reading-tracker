import { useState } from "react";
import { useSelector } from "react-redux";
import { Link, useLocation } from "react-router-dom";
import avatarImage from "../../assets/avatar.svg";
import MenuDot from "../../assets/menu_dots.svg";
import { ButtonsStyle } from "../../styles/globalStyles.js";
import {
  Avatar,
  ContainerRight,
  MenuContainer,
  NavbarLink,
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

  const onClick = () => {
    setShowMenu((prevState) => !prevState);
  };

  const menuButton = (
    <MenuContainer>
      <img src={MenuDot} alt="Menu" onClick={onClick} />
      {showMenu && (
        <NavigationActionsContainer onMouseLeave={() => setShowMenu(false)} />
      )}
    </MenuContainer>
  );

  const profileButton = (
    <Link to={"/profile"}>
      <Avatar src={avatarImage} alt="Avatar" />
    </Link>
  );

  return (
    <header>
      <NavbarLink to="/">
        <h1>Bible Reading Tracker</h1>
      </NavbarLink>

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
    </header>
  );
};

export default Header;
