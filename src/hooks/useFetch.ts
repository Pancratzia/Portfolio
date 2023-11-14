import { useState, useEffect } from "react";

interface FetchState {
  data: any;
  loading: boolean;
}

const useFetch = (url: string, auth = ""): FetchState => {
  const [data, setData] = useState({});
  const [loading, setLoading] = useState(true);

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
      })
      .finally(() => {
        setLoading(false);
      });
  }, [url, auth]);

  return { data, loading };
};

export default useFetch;

