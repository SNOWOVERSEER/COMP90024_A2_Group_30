import axios from "axios";

const request = axios.create({
  baseURL: "/", 
  timeout: 60000, // When the request exceeds 60 seconds without obtaining a result, the user will be notified of a timeout.
});

// interceptors axios
request.interceptors.request.use(
  (config) => {
    return config;
  },
  (err) => {
    Promise.reject(err);
  }
);

request.interceptors.response.use(
  (res) => {
    // console.log(res)
    return Promise.resolve(res);
  },
  (err) => {
    Promise.reject(err);
  }
);

export default request;
