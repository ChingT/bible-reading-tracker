import { useState } from "react";
import CheckMarkIcon from "../../../assets/checkmark_new.svg";
import useApiRequest from "../../../hooks/useApiRequest.js";
import useAutoFetch from "../../../hooks/useAutoFetch.js";
import { CheckMark } from "../../../styles/globalStyles.js";
import LoadingSpinner from "../../LoadingSpinner/LoadingSpinner.jsx";
import {
  LabelStyle,
  ProfileHeaderEditContainer,
  ProfileHeaderLeftContainer,
  ProfileHeaderRightContainer,
  SavedChangesMessage,
  StyledInputHeader,
  StyledTextArea,
} from "../Profile/ProfileHeader.style.js";
import { InputWrapper } from "./EditProfile.style.js";
import LeftEditContainer from "./LeftEditContainer.jsx";

function EditProfile() {
  const { data, loading } = useAutoFetch("get", "users/me/", "", true);
  const inputFields = {
    first_name: { type: "text", value: data?.first_name, label: "First Name" },
    last_name: { type: "text", value: data?.last_name, label: "Last Name" },
    email: { type: "email", value: data?.email, label: "Email" },
    username: { type: "text", value: data?.username, label: "Username" },
    location: { type: "text", value: data?.location, label: "Location" },
    password: { type: "password", value: data?.password, label: "Password" },
    about_me: { type: "text", value: data?.about_me, label: "About" },
  };

  const { sendRequest } = useApiRequest(true);
  const [userData, setUserData] = useState({});
  const [changesSaved, setChangesSaved] = useState(false);

  const handleInput = (e) => {
    setUserData({ ...userData, [e.target.id]: e.target.value });
  };

  const handleProfileUpdate = () => {
    sendRequest("patch", "users/me/", userData);
    showChangesSavedMessage();
  };

  const showChangesSavedMessage = () => {
    setChangesSaved(true);
    setTimeout(() => setChangesSaved(false), 2000);
  };

  if (loading) return <LoadingSpinner />;
  return (
    <>
      <ProfileHeaderEditContainer>
        <ProfileHeaderLeftContainer>
          <LeftEditContainer
            initialAvatar={data?.avatar}
            handleProfileUpdate={handleProfileUpdate}
          />
        </ProfileHeaderLeftContainer>
        <ProfileHeaderRightContainer>
          <InputWrapper>
            <form>
              {Object.keys(inputFields).map((field) => {
                return (
                  <div className={"input-field"} key={field}>
                    <LabelStyle>{inputFields[field].label}</LabelStyle>
                    {field !== "about_me" ? (
                      <StyledInputHeader
                        type={inputFields[field].type}
                        value={
                          userData[field] === undefined
                            ? inputFields[field].value
                            : userData[field]
                        }
                        id={field}
                        onChange={handleInput}
                      />
                    ) : (
                      <StyledTextArea
                        name="Text1"
                        cols="40"
                        rows="5"
                        value={
                          userData[field] === undefined
                            ? inputFields[field].value
                            : userData[field]
                        }
                        id={field}
                        onChange={handleInput}
                      />
                    )}
                  </div>
                );
              })}
            </form>

            {changesSaved && (
              <SavedChangesMessage>
                <CheckMark src={CheckMarkIcon} />
                changes saved!
              </SavedChangesMessage>
            )}
          </InputWrapper>
        </ProfileHeaderRightContainer>
      </ProfileHeaderEditContainer>
    </>
  );
}

export default EditProfile;
