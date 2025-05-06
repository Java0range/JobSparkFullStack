import axios from "axios";

const baseURL = "http://localhost:5000";

const $api = axios.create({
  withCredentials: true,
  baseURL: baseURL,
})

// sfdsfsdf

export default $api;