import { configureStore } from "@reduxjs/toolkit";
import loadBooks from "./slices/loadedBooks.js";
import loggedInUser from "./slices/loggedInUser.js";

export default configureStore({
  reducer: {
    loggedInUser: loggedInUser,
    loadedBooks: loadBooks,
  },
});
