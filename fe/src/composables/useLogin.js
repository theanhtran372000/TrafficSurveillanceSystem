import { ref } from "vue";
import { getAccessToken, setAccessToken } from "@/utils/accessToken";
import { isOk } from "@/utils/response";
import instance from "@/utils/axios";

const error = ref(null);
const isPending = ref(false);

async function logIn(phone, password) {
  isPending.value = true;
  error.value = null;
  try {
    // Current access token
    const accessToken = getAccessToken(instance);

    // If dont have access token, request for one
    if (!accessToken) {
      const response = await instance.post("/auth", {
        phone: phone,
        password: password,
      });
      console.log(response);
      if (!isOk(response)) throw new Error("Login failed!");
      const accessToken = `Bearer ${response.data["access_token"]}`;
      console.log("Token: ", accessToken);
      setAccessToken(instance, accessToken);
    }

    const response = await instance.get("/auth");
    if (!isOk(response)) throw new Error("Login failed!");
    console.log("Response: ", response);
    return response;
  } catch (err) {
    console.log("Error:", err);
    error.value = err.response.data.message;
  } finally {
    isPending.value = false;
  }
}

export function useLogin() {
  return {
    isPending,
    error,
    logIn,
  };
}
