import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import logoutImage from "../../assets/icon_logout.svg";
import { logoutUser } from "../../store/slices/loggedInUser.js";
import { ActionContainer } from "./Header.style.js";

const NavigationActionsContainer = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleClickLogout = () => {
    localStorage.clear();
    dispatch(logoutUser());
    navigate("/signin");
  };

  return (
    <ActionContainer onClick={handleClickLogout}>
      <img alt="Logout Image" src={logoutImage} />
      <p>Logout</p>
    </ActionContainer>
  );
};

export default NavigationActionsContainer;
