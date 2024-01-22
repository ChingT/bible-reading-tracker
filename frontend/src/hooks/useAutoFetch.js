/* eslint-disable react-hooks/exhaustive-deps */
import { useEffect } from "react";
import useApiRequest from "./useApiRequest.js";

const useAutoFetch = (method, url, requestData, trigger, auth) => {
  const token = localStorage.getItem("auth-token");
  const { sendRequest, data, error, loading } = useApiRequest(auth);

  useEffect(() => {
    if (auth === "noAuth" || token) sendRequest(method, url, requestData);
  }, [url, trigger]);

  return { data, error, loading };
};

export default useAutoFetch;
