import styled from "styled-components";

export const ProfileAboutContainer = styled.div`
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row;
  gap: 2rem;
  margin-top: 2rem;

  h3 {
    font-size: 5rem;
    font-weight: 600;
    margin-bottom: 0.8rem;
    color: ${(props) => props.theme.fontColors.profilePageSecondaryColor};
  }

  p {
    line-height: 1.6;
    hyphens: auto;
  }

  .email {
    flex: 65%;
    padding-right: 1rem;
  }
`;

export const AboutMe = styled.div`
  display: flex;
  width: 50%;
  height: 100%;
  flex-direction: column;
  p {
    line-height: 1.6;
    hyphens: auto;
  }

  h3 {
    font-size: 1.3rem;
    font-weight: 600;
    margin-bottom: 0.8rem;
    margin-top: 0.8rem;
  }
`;
