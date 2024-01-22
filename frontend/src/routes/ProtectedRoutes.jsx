import { useEffect } from "react";
import { useSelector } from "react-redux";
import { Navigate, Outlet, useLocation } from "react-router-dom";

export const ProtectedRoutes = () => {
  const accessToken = useSelector((store) => store.loggedInUser.accessToken);
  const location = useLocation();

  useEffect(() => {
    if (accessToken === null)
      return <Navigate to="/signin" replace state={{ from: location }} />;
  }, [accessToken, location]);

  return (
    <main>
      <Outlet />
    </main>
  );
};

export default ProtectedRoutes;
