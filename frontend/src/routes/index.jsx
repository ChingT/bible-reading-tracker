import { BrowserRouter, Route, Routes } from "react-router-dom";
import PasswordReset from "../components/AuthComp/PasswordReset.jsx";
import SignInSection from "../components/AuthComp/SignInSection.jsx";
import SignUpSection from "../components/AuthComp/SignUpSection.jsx";
import Layout from "../components/Layout/Layout.jsx";
import NotFound from "../pages/NotFound.jsx";
import Plans from "../pages/Plans.jsx";
import ProfilePage from "../pages/ProfilePage.jsx";
import ProtectedRoutes from "./ProtectedRoutes.jsx";

const PageRoutes = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />}>
          <Route path="/" element={<Plans />} />
          <Route path="signin" element={<SignInSection />} />
          <Route path="signup" element={<SignUpSection />} />
          <Route path="password-reset" element={<PasswordReset />} />

          <Route path="*" element={<NotFound />} />

          <Route element={<ProtectedRoutes />}>
            <Route path="/profile/:profileId?" element={<ProfilePage />} />
          </Route>
        </Route>
      </Routes>
    </BrowserRouter>
  );
};

export default PageRoutes;
