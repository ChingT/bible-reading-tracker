import styled from "styled-components";
import LoadingSpinner from "../LoadingSpinner/LoadingSpinner";

export default function ProgressBar({ numFinishedSchedules, numSchedules }) {
  if (!numSchedules) return <LoadingSpinner />;

  const progressNumber =
    ((numFinishedSchedules / numSchedules) * 100).toFixed(0) + " %";

  const progressBarStyle = { width: "50%", padding: "1rem" };

  return (
    <Container>
      Lesefortschritt
      <progress
        value={numFinishedSchedules}
        max={numSchedules}
        style={progressBarStyle}
      />
      {progressNumber}
    </Container>
  );
}

export const Container = styled.div`
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 1rem;
  width: 100%;
  margin-top: 1rem;
`;
