import styled from "styled-components";

export const GridContainer = styled.div`
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  width: 100%;
  grid-row-gap: 1rem;
  margin-top: 2rem;
`;

const CardBase = styled.div`
  box-shadow: 0 0 2px 2px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  width: 90%;
  border-radius: 1rem;
  padding: 1rem;
`;

export const CardTitle = styled(CardBase)`
  background-color: ${(props) => props.theme.colors.primary};
  color: ${(props) => props.theme.colors.secondary};
  font-weight: 600;
  align-items: center;
  justify-content: center;
  cursor: default;
`;

export const CardContainer = styled(CardBase)`
  cursor: pointer;

  &:hover {
    outline-style: solid;
    outline-width: 1px;
  }
`;
