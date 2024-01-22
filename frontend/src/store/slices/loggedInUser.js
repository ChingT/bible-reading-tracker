import { createSlice } from "@reduxjs/toolkit";

export const loggedInUser = createSlice({
  name: "current-user",
  initialState: { user: undefined, accessToken: undefined },
  reducers: {
    loginUser: (state, action) => {
      state.accessToken = action.payload.accessToken;
    },
    logoutUser: (state) => {
      state.accessToken = null;
    },
  },
});
export const { loginUser, logoutUser } = loggedInUser.actions;
export default loggedInUser.reducer;
