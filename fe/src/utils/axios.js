import axios from "axios";
import constants from "../constants";
import { getAccessToken } from "./accessToken";

const instance = axios.create({
  baseURL: constants.__baseURL__,
  timeout: 5000,
});
instance.defaults.headers.common["Authorization"] = `Bearer ${getAccessToken()}`;
export default instance;
