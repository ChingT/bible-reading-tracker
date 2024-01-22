import { useSelector } from "react-redux";
import { Link } from "react-router-dom";
import avatarImage from "../../../assets/avatar.svg";
import ProfileData from "./ProfileData/ProfileData.jsx";
import {
  AvatarImg,
  NameAndLocation,
  ProfileButton,
  ProfileHeaderContainer,
  ProfileHeaderLeftContainer,
  ProfileHeaderRightContainer,
  ProfileHeaderTop,
} from "./ProfileHeader.style.js";

function ProfileHeader({ userdata, error }) {
  const currentUser = useSelector((store) => store.loggedInUser.user);

  return (
    <ProfileHeaderContainer>
      {userdata && (
        <>
          <ProfileHeaderLeftContainer>
            <AvatarImg alt="avatar" src={userdata.avatar || avatarImage} />
            {userdata.id === currentUser.id ? (
              <Link to={"/profile/edit"}>
                <ProfileButton>Edit Profile</ProfileButton>
              </Link>
            ) : null}
          </ProfileHeaderLeftContainer>

          <ProfileHeaderRightContainer>
            <ProfileHeaderTop>
              <NameAndLocation>
                <h2>{`${userdata.first_name} ${userdata.last_name}`}</h2>
                <h3>{userdata.location}</h3>
              </NameAndLocation>
            </ProfileHeaderTop>
            <ProfileData userdata={userdata} />
          </ProfileHeaderRightContainer>
        </>
      )}
      {error && (
        <div>
          <h2>Profile not found</h2>
        </div>
      )}
    </ProfileHeaderContainer>
  );
}

export default ProfileHeader;
