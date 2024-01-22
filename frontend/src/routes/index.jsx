import { BrowserRouter, Route, Routes } from "react-router-dom";
import CongratsSection from "../components/AuthComp/CongratsSection.jsx";
import PasswordReset from "../components/AuthComp/PasswordReset.jsx";
import PasswordResetValidation from "../components/AuthComp/PasswordResetValidation.jsx";
import SignInSection from "../components/AuthComp/SignInSection.jsx";
import SignUpSection from "../components/AuthComp/SignUpSection.jsx";
import VerificationSection from "../components/AuthComp/VerificationSection.jsx";
import Layout from "../components/Layout/Layout.jsx";
import HeroPage from "../pages/HeroPage.jsx";
import NotFound from "../pages/NotFound.jsx";
import ProfilePage from "../pages/ProfilePage.jsx";
import ProtectedRoutes from "./ProtectedRoutes.jsx";

const PageRoutes = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />}>
          <Route path="/" element={<HeroPage />} />
          <Route path="signin" element={<SignInSection />} />
          <Route path="signup" element={<SignUpSection />} />
          <Route path="password-reset" element={<PasswordReset />} />
          <Route
            path="password-reset-validation"
            element={<PasswordResetValidation />}
          />
          <Route path="congratulations" element={<CongratsSection />} />
          <Route path="verification" element={<VerificationSection />} />
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
