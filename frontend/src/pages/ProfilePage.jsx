import { useParams } from "react-router";
import LoadingSpinner from "../components/LoadingSpinner/LoadingSpinner.jsx";
import ProfileHeader from "../components/UserProfile/ProfileHeader.jsx";
import {
  LeftBlock,
  ProfilePageMain,
  RightBlock,
} from "../components/UserProfile/ProfileHeader.style.js";
import useAutoFetch from "../hooks/useAutoFetch.js";

function ProfilePage() {
  const { profileId } = useParams();
  const endpointToFetch = profileId ? `users/${profileId}/` : "users/me/";
  const { data } = useAutoFetch("get", endpointToFetch, "", true, profileId);

  if (!data) return <LoadingSpinner />;
  return (
    <ProfilePageMain>
      <LeftBlock>
        <ProfileHeader userdata={data} />
      </LeftBlock>
      <RightBlock></RightBlock>
    </ProfilePageMain>
  );
}

export default ProfilePage;
