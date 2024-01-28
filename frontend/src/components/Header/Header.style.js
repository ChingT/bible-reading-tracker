import { NavLink } from "react-router-dom";
import styled from "styled-components";

export const NavbarLink = styled(NavLink)`
  height: 100%;
  display: flex;
  align-items: center;
  text-decoration: none;

  h1 {
    color: ${(props) => props.theme.colors.primary};
    font-size: 2rem;
    font-weight: 400;
  }
`;

export const ContainerRight = styled.nav`
  display: flex;
  gap: 2rem;
`;

export const MenuContainer = styled.div`
  display: flex;
  align-items: center;

  > img {
    cursor: pointer;
    width: 2rem;
    height: 2rem;
  }
`;

export const Avatar = styled.img`
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 50%;
  object-fit: cover;
  cursor: pointer;
`;

export const ActionContainer = styled.div`
  position: absolute;
  top: calc(100% + 0.5rem);
  right: 2rem;
  background-color: white;
  padding: 1rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  cursor: pointer;
  border: 1px solid ${(props) => props.theme.colors.primary};

  &:hover {
    background: rgba(0, 0, 0, 0.05);
  }
`;
