import { useState, useEffect } from "react";

interface FetchState {
  data: any;
  loading: boolean;
  error: any;
}

const useFetch = (url: string, auth = ""): FetchState => {
  const [data, setData] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: auth,
      },
    })
      .then((response) => response.json())
      .then((data) => {
        setData(data);
      }).
      catch((error) => {
        setError(error);
      })
      .finally(() => {
        setLoading(false);
      });
  }, [url, auth]);

  return { data, loading, error };
};

export default useFetch;

