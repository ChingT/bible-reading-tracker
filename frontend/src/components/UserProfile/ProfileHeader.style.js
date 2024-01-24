import styled from "styled-components";

export const ProfilePageMain = styled.div`
  display: flex;
  flex-direction: row;
  height: inherit;
  width: 97%;
  gap: 5rem;
  margin-top: 4rem;
`;

export const LeftBlock = styled.div`
  display: flex;
  margin-left: 2.4%;
  flex-direction: column;
  height: 90%;
  width: 50%;
  align-items: center;
  justify-content: center;
`;

export const RightBlock = styled.div`
  display: flex;
  flex-direction: column;
  width: 50%;
  align-items: center;
  justify-content: center;
  height: 90%;
`;

export const NameAndLocation = styled.div`
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
`;

export const ProfileHeaderTop = styled.div`
  display: flex;
  width: 100%;
  flex-direction: row;
  gap: 2rem;
  justify-content: center;
`;

export const ProfileHeaderLeftContainer = styled.div`
  width: 42%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 0rem;
`;

export const ProfileHeaderRightContainer = styled.div`
  display: flex;
  flex-direction: column;
  gap: 1rem;
  width: 90%;
  height: 100%;
  margin-top: 3rem;
  margin-left: 2.5%;
`;

export const AvatarImg = styled.img`
  width: 89%;
  object-fit: cover;
  opacity: 0.96;
  height: 64%;
  border-radius: 50%;
  border: 4px solid ${(props) => props.theme.colors.secondary};
  -webkit-transition: all 0.35s ease-in-out;
  transition: all 0.35s ease-in-out;
  transform: scale(1.6);
  position: relative;
  left: -15%;
`;
