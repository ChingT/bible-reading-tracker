import { useState } from "react";
import { useSelector } from "react-redux";
import { Link, useLocation } from "react-router-dom";
import avatarImage from "../../assets/avatar.svg";
import MenuDot from "../../assets/menu_dots.svg";
import { ButtonsStyle } from "../../styles/buttons.style.js";
import {
  Avatar,
  ContainerLeft,
  ContainerRight,
  HeaderContainer,
  MenuContainer,
  NavbarLink,
  StyledH1,
} from "./Navigation.style.js";
import NavigationActionsContainer from "./NavigationActionsContainer.jsx";

const Navigation = () => {
  const loggedInUser = useSelector((store) => store.loggedInUser.user);
  const [showMenu, setShowMenu] = useState(false);

  const location = useLocation();
  const isLoginPage = location.pathname === "/signin";
  const isSignUpPage = location.pathname === "/signup";

  return (
    <HeaderContainer>
      <ContainerLeft>
        <NavbarLink to="/">
          <StyledH1>Bible Reading Tracker</StyledH1>
        </NavbarLink>
      </ContainerLeft>

      <nav>
        {loggedInUser ? (
          <>
            <ContainerRight>
              <Link to={"/profile"}>
                <Avatar
                  src={loggedInUser?.avatar || avatarImage}
                  alt="Avatar"
                />
              </Link>
              <MenuContainer>
                <img
                  src={MenuDot}
                  alt="Menu"
                  onClick={() => setShowMenu(!showMenu)}
                />
                {showMenu && (
                  <NavigationActionsContainer setShowMenu={setShowMenu} />
                )}
              </MenuContainer>
            </ContainerRight>
          </>
        ) : (
          <div>
            {isLoginPage && (
              <>
                <Link to="/signup">
                  <ButtonsStyle>Sign Up</ButtonsStyle>
                </Link>
              </>
            )}
            {isSignUpPage && (
              <>
                <Link to="/signin">
                  <ButtonsStyle>Sign In</ButtonsStyle>
                </Link>
              </>
            )}
            {!isLoginPage && !isSignUpPage && (
              <Link to="/signin">
                <ButtonsStyle>Sign In</ButtonsStyle>
              </Link>
            )}
          </div>
        )}
      </nav>
    </HeaderContainer>
  );
};

export default Navigation;
