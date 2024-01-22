import { useEffect } from "react";
import { useDispatch } from "react-redux";
import LoadingSpinner from "./components/LoadingSpinner/LoadingSpinner.jsx";
import useAutoFetch from "./hooks/useAutoFetch.js";
import PageRoutes from "./routes/index.jsx";
import { loginUser, logoutUser } from "./store/slices/loggedInUser.js";

const App = () => {
  const dispatch = useDispatch();
  const userData = JSON.parse(localStorage.getItem("user"));
  const accessToken = localStorage.getItem("auth-token");

  const { error, loading } = useAutoFetch("post", "auth/token/verify/", {
    token: accessToken,
  });

  useEffect(() => {
    if (error === null) {
      dispatch(loginUser({ user: userData, accessToken: accessToken }));
    } else {
      dispatch(logoutUser());
      localStorage.clear();
    }
  }, [error, accessToken, dispatch, userData]);

  if (loading) return <LoadingSpinner />;

  return <PageRoutes />;
};

export default App;
