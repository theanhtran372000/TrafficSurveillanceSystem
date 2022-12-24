<template>
  <div class="w-full flex flex-row justify-center items-center">
    <!-- Login form on the left -->
    <div>
      <form
        class="bg-gray p-8 rounded-lg flex flex-col mr-48 shadow-lg"
        style="width: 420px"
        @submit.prevent="onSubmit"
      >
        <!-- Phone -->
        <div class="row">
          <label class="flex flex-col" for="username">
            <span class="text-blue font-semibold text-xl ml-1">Phone</span>
            <input
              id="phone"
              type="text"
              class="placeholder-light_blue text-lg py-2 px-2 rounded-lg outline-none text-blue mt-1.5"
              v-model="phone"
              placeholder="Input your phone number..."
            />
          </label>
        </div>

        <!-- Password -->
        <div class="row mt-6">
          <label class="flex flex-col" for="password">
            <span class="text-blue font-semibold text-xl ml-1">Password</span>
            <input
              id="password"
              type="password"
              class="placeholder-light_blue text-lg py-2 px-2 rounded-lg outline-none text-blue mt-1.5"
              v-model="password"
              placeholder="Input your password..."
            />
          </label>
        </div>

        <!-- Error message -->
        <div class="row mt-4 -mb-5" v-if="error">
          <span class="text-light_blue">{{ error }}</span>
        </div>

        <!-- Login button -->
        <div class="row mt-12">
          <button
            class="transition ease-in-out duration-500 bg-blue text-gray font-bold text-2xl w-full p-2 rounded-lg border-blue border-4 hover:text-blue hover:bg-gray"
            type="submit"
            v-if="!isPending"
          >
            Sign in
          </button>

          <button
            class="transition ease-in-out duration-500 bg-slate-500 text-gray font-bold text-2xl w-full p-2 rounded-lg border-slate-500 border-4"
            type="submit"
            disabled
            v-else
          >
            Loading...
          </button>
        </div>

        <!-- Notification -->
        <div class="row mt-6">
          <p class="text-lg text-blue">
            I am a new member.
            <router-link
              class="ml-1 font-bold underline"
              :to="{ name: 'register', params: {} }"
              >Sign up here</router-link
            >
          </p>
        </div>
      </form>
    </div>

    <!-- Title and description on the right -->
    <div class="flex flex-col justify-center items-center">
      <div>
        <h1 class="font-bold text-7xl text-gray text-center w-full">
          Traffity
        </h1>
        <h3 class="font-semibold text-2xl text-gray text-center w-full">
          Smart traffic surveillance system
        </h3>
      </div>

      <div class="mt-4" style="width: 400px; height: 400px">
        <img
          class="w-full h-full"
          :src="require('@/assets/images/animated_7.png')"
          alt="Login image"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useLogin } from "@/composables/useLogin";
import { getAccessToken } from "@/utils/accessToken";
import instance from "@/utils/axios";

export default {
  setup() {
    const router = useRouter();

    const phone = ref("");
    const password = ref("");

    const { isPending, error, logIn } = useLogin();

    async function onSubmit() {
      console.log(phone.value, password.value);
      const response = await logIn(phone.value, password.value);
      if (!error.value)
        router.push({
          name: "home",
        });
    }

    return {
      isPending,
      error,
      phone,
      password,
      onSubmit,
    };
  },
};
</script>
