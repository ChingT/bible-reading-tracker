import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import logoutImage from "../../assets/icon_logout.svg";
import { logoutUser } from "../../store/slices/loggedInUser.js";
import { ActionContainer, ActionsWrapper } from "./Navigation.style.js";

const NavigationActionsContainer = ({ setShowMenu }) => {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleClickLogout = () => {
    localStorage.clear();
    dispatch(logoutUser());
    navigate("/");
  };

  return (
    <ActionsWrapper onMouseLeave={() => setShowMenu(false)}>
      <ActionContainer onClick={handleClickLogout}>
        <div>
          <img alt="Logout Image" src={logoutImage} />
          <p>Logout</p>
        </div>
      </ActionContainer>
    </ActionsWrapper>
  );
};

export default NavigationActionsContainer;
