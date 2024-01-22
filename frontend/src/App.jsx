import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import LoadingSpinner from "./components/LoadingSpinner/LoadingSpinner.jsx";
import useApiRequest from "./hooks/useApiRequest.js";
import PageRoutes from "./routes/index.jsx";
import { loginUser, logoutUser } from "./store/slices/loggedInUser.js";

export default function App() {
  const token = useSelector((store) => store.loggedInUser.accessToken);
  const accessToken = token || localStorage.getItem("auth-token");
  const { sendRequest, error, loading } = useApiRequest();
  const dispatch = useDispatch();

  useEffect(() => {
    if (accessToken) {
      sendRequest("post", "auth/access-token/verification", {
        access_token: accessToken,
      });
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [accessToken]);

  useEffect(() => {
    if (!loading && error === null) {
      dispatch(loginUser({ accessToken: accessToken }));
    }
    if (error !== null) {
      dispatch(logoutUser());
      localStorage.removeItem("auth-token");
    }
  }, [accessToken, dispatch, error, loading]);

  if (token || token === null) return <PageRoutes />;

  return <LoadingSpinner />;
}
