import { useParams } from "react-router";
import LoadingSpinner from "../components/LoadingSpinner/LoadingSpinner.jsx";
import ProfileHeader from "../components/UserProfile/Profile/ProfileHeader.jsx";
import {
  LeftBlock,
  ProfilePageMain,
  RightBlock,
} from "../components/UserProfile/Profile/ProfileHeader.style.js";
import useAutoFetch from "../hooks/useAutoFetch.js";

function ProfilePage() {
  const { profileId } = useParams();
  const params = useParams();
  const endpointToFetch = profileId ? `users/${profileId}/` : "users/me/";
  const { data } = useAutoFetch("get", endpointToFetch, "", params);

  if (!data) return <LoadingSpinner />;
  return (
    <ProfilePageMain>
      <LeftBlock>
        <ProfileHeader userdata={data} profileId={profileId} />
      </LeftBlock>
      <RightBlock></RightBlock>
    </ProfilePageMain>
  );
}

export default ProfilePage;
