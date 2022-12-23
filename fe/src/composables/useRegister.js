import { ref } from "vue";
import { isOk } from "@/utils/response";
import instance from "@/utils/axios";
import { randomEmail } from "@/utils/random";
import { useLogin } from "./useLogin";

const registerError = ref(null);
const isPending = ref(false);
const { error, logIn } = useLogin();

async function register(fullname, phone, password) {
  isPending.value = true;
  error.value = null;
  try {
    // Register new account
    const registerResponse = await instance.post("/accounts", {
      name: fullname,
      phone: phone,
      password: password,
      email: randomEmail(),
    });
    if (!isOk(registerResponse)) throw new Error("Register failed!");

    // Đăng nhập
    const loginResponse = await logIn(phone, password);
    if (error.value) {
      registerError.value = error.value;
      throw new Error("Register failed!");
    }
    return loginResponse;
  } catch (err) {
    console.log("Error:", err);
    registerError.value = err.response.data.message;
  } finally {
    isPending.value = false;
  }
}

export function useRegister() {
  return {
    isPending,
    error: registerError,
    register,
  };
}
