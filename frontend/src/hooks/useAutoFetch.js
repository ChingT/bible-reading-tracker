/* eslint-disable react-hooks/exhaustive-deps */

import { useEffect } from "react";
import useApiRequest from "./useApiRequest.js";

const useAutoFetch = (method, url, requestData, auth, trigger) => {
  const { sendRequest, data, error, loading } = useApiRequest(auth);

  useEffect(() => {
    sendRequest(method, url, requestData);
  }, [trigger]);

  return { data, error, loading };
};

export default useAutoFetch;
