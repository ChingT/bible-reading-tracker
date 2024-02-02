import { createSlice } from "@reduxjs/toolkit";

export const books = createSlice({
  name: "books",
  initialState: { books: [] },
  reducers: {
    loadBooks: (state, action) => {
      state.books = action.payload;
    },
  },
});
export const { loadBooks } = books.actions;
export default books.reducer;
