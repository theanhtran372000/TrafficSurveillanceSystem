import axios from "axios";
import constants from "../constants";
import { setAccessToken } from "./accessToken";

const instance = axios.create({
  baseURL: constants.__baseURL__,
  timeout: 5000,
});

setAccessToken(instance, constants.__access_token__);

export default instance;
