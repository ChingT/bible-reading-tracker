import { useSelector } from "react-redux";
import { Navigate, Outlet, useLocation } from "react-router-dom";

export const ProtectedRoutes = () => {
  const accessToken = useSelector((store) => store.loggedInUser.accessToken);
  const location = useLocation();

  if (accessToken === null)
    return <Navigate to="/signin" replace state={{ from: location }} />;

  return (
    <main>
      <Outlet />
    </main>
  );
};

export default ProtectedRoutes;
