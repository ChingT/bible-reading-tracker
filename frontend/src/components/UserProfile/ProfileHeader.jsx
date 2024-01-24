import avatarImage from "../../assets/avatar.svg";
import {
  AvatarImg,
  NameAndLocation,
  ProfileHeaderLeftContainer,
  ProfileHeaderRightContainer,
} from "./ProfileHeader.style.js";

function ProfileHeader({ userdata }) {
  return (
    <>
      <ProfileHeaderLeftContainer>
        <AvatarImg alt="avatar" src={userdata.avatar || avatarImage} />
      </ProfileHeaderLeftContainer>

      <ProfileHeaderRightContainer>
        <NameAndLocation>
          <h2>{userdata.display_name}</h2>
          <p>{userdata.email}</p>
        </NameAndLocation>
      </ProfileHeaderRightContainer>
    </>
  );
}

export default ProfileHeader;
