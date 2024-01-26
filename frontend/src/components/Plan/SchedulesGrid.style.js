import styled from "styled-components";

export const GridContainer = styled.div`
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  width: 100%;
  grid-row-gap: 1rem;
`;

export const CardContainer = styled.div`
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  width: 93%;
  border-radius: 1rem;
  padding: 1rem;
  cursor: pointer;

  &:hover {
    outline-style: solid;
    outline-width: 1px;
  }
`;
