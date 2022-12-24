import { ref } from "vue";
import { getAccessToken, setAccessToken } from "@/utils/accessToken";
import { isOk } from "@/utils/response";
import instance from "@/utils/axios";
import { store } from "@/store/store";
import C from "@/constants";

const error = ref(null);
const isPending = ref(false);

async function logIn(phone, password) {
  isPending.value = true;
  error.value = null;
  try {
    const response = await instance.post("/auth", {
      phone: phone,
      password: password,
    });
    if (!isOk(response)) throw new Error("Login failed!");

    const accessToken = response.data["access_token"];
    setAccessToken(instance, accessToken);
    return response;
  } catch (err) {
    error.value = err.response.data.message;
  } finally {
    isPending.value = false;
  }
}

async function getMyProfile() {
  try {
    // return new Promise((resolve, reject) => {
    //   setTimeout(() => {
    //     resolve({
    //       statusCode: 200,
    //       data: {},
    //     });
    //   }, 3000);
    // });
    store.setAuthState(C.__request_status__.REQUEST);
    const response = await instance.get("/auth");
    store.setAuthState(C.__request_status__.SUCCESS);
    return {
      statusCode: 200,
      data: response.data,
    };
  } catch (err) {
    console.log("err: ", err);
    store.setAuthState(C.__request_status__.ERROR);
    return {
      statusCode: 401,
    };
  }
}

export function useLogin() {
  return {
    isPending,
    error,
    logIn,
    getMyProfile,
  };
}
