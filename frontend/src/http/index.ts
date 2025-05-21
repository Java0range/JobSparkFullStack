import axios, { type AxiosResponse } from 'axios'

const baseURL = "http://localhost/api";

const $api = axios.create({
  withCredentials: true,
  baseURL: baseURL,
})

$api.interceptors.response.use((config) => {
  return config;
}, async (error) => {
  const originalRequest = error.config;
  if (error.response.status === 401 &&
    (error.response.data == "Invalid access token" ||
    error.response.data == "Error: Invalid access token") &&
    error.config && !error.config._isRetry) {
    originalRequest._isRetry = true;
    try {
      await $api.post<AxiosResponse>("/users/refresh");
      return $api.request(originalRequest);
    } catch (err) {
      console.log(err);
    }
  }
  throw error;
})

export default $api;