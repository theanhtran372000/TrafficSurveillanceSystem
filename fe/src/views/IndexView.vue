<template>
  <div class="pr-28 pl-10 w-full flex flex-row justify-center items-center">
    <!-- Image on the left -->
    <div class="mr-36" style="width: 500px; height: 500px">
      <img
        class="w-full h-full"
        :src="require('@/assets/images/animated_1.png')"
        alt="Index image"
      />
    </div>

    <!-- Title and description on the right -->
    <div class="flex flex-col">
      <h1 class="font-bold text-9xl text-gray text-center w-full">Traffity</h1>
      <h3 class="font-semibold text-3xl text-gray text-center w-full">
        Smart traffic surveillance system
      </h3>
      <div class="flex flex-row justify-center items-center w-full mt-8">
        <router-link
          :to="{
            name: 'login',
            params: {},
          }"
          class="transition ease-in-out duration-500 w-40 py-3 bg-gray border-4 border-gray text-center text-blue text-2xl font-bold rounded-full mr-8 hover:bg-blue hover:text-gray"
        >
          Sign in
        </router-link>
        <router-link
          :to="{
            name: 'register',
            params: {},
          }"
          class="transition ease-in-out duration-500 w-40 py-3 bg-transparent border-4 border-gray text-center text-gray text-2xl font-bold rounded-full hover:bg-blue"
        >
          Sign up
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { getAccessToken } from "@/utils/accessToken";
import instance from "@/utils/axios";
import { useRouter } from "vue-router";
import { useLogin } from "@/composables/useLogin";

export default {
  setup() {
    const router = useRouter();
    const { error, logIn } = useLogin();

    async function logInWithAccessToken() {
      const response = await logIn("", "");
      if (!error.value)
        router.push({
          name: "home",
          params: response.data,
        });
    }

    const accessToken = getAccessToken(instance);
    console.log("Access token: ", accessToken);

    // Login if already have access token
    if (accessToken) {
      console.log("Already have access token!");
      logInWithAccessToken();
    }
  },
};
</script>
