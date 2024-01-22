import { useEffect } from "react";
import { useSelector } from "react-redux";
import { Outlet, useNavigate } from "react-router-dom";
import Navigation from "../components/Navigation/Navigation.jsx";

export const ProtectedRoutes = () => {
  const accessToken = useSelector((store) => store.loggedInUser.accessToken);
  const navigate = useNavigate();

  useEffect(() => {
    if (accessToken === null) return navigate("/");
  }, [accessToken, navigate]);

  return (
    <main>
      <Navigation />
      <Outlet />
    </main>
  );
};

export default ProtectedRoutes;
