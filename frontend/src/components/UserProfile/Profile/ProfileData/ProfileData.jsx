import { AboutMe, ProfileAboutContainer } from "./ProfileData.style.js";

function ProfileData(props) {
  return (
    <ProfileAboutContainer>
      <AboutMe>
        <h3>About me</h3>
        <p>{props.userdata.about_me}</p>
      </AboutMe>
    </ProfileAboutContainer>
  );
}

export default ProfileData;
