import avatarImage from "../../../assets/avatar.svg";
import {
  AvatarImg,
  NameAndLocation,
  ProfileHeaderContainer,
  ProfileHeaderLeftContainer,
  ProfileHeaderRightContainer,
  ProfileHeaderTop,
} from "./ProfileHeader.style.js";

function ProfileHeader({ userdata }) {
  return (
    <ProfileHeaderContainer>
      <ProfileHeaderLeftContainer>
        <AvatarImg alt="avatar" src={userdata.avatar || avatarImage} />
      </ProfileHeaderLeftContainer>

      <ProfileHeaderRightContainer>
        <ProfileHeaderTop>
          <NameAndLocation>
            <h2>{userdata.display_name}</h2>
            <p>{userdata.email}</p>
          </NameAndLocation>
        </ProfileHeaderTop>
      </ProfileHeaderRightContainer>
    </ProfileHeaderContainer>
  );
}

export default ProfileHeader;
