import { Link } from "react-router-dom";
import { ButtonsStyle } from "../styles/globalStyles.js";

const HeroPage = () => {
  const button = (
    <Link to="/plans">
      <ButtonsStyle>Go to schedule</ButtonsStyle>
    </Link>
  );

  return (
    <>
      <h1>Welcome to Bible Reading Tracking App</h1>
      {button}
    </>
  );
};

export default HeroPage;
