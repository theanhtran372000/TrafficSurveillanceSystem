<template>
  <!-- Header -->
  <div
    class="w-full h-14 bg-gray shadow-lg fixed top-0 flex flex-row justify-between"
  >
    <!-- Logo -->
    <div
      @click="onBackToIndex"
      class="flex h-full py-2 px-8 justify-center items-center cursor-pointer"
    >
      <img
        class="w-full h-full mr-4"
        :src="require('@/assets/images/logo.png')"
        alt="Logo"
      />
      <h3 class="font-bold text-xl text-blue">Traffity</h3>
    </div>

    <!-- User info -->
    <div class="flex h-full py-2 px-8 justify-center items-center">
      <font-awesome-icon
        class="text-2xl mr-4 text-dark_blue"
        icon="fa-solid fa-user-secret"
      />
      <h3 class="font-semibold text-lg text-blue mr-4">{{ store?.profile?.name }}</h3>
      <font-awesome-icon
        @click="onLogOut"
        class="text-2xl mr-4 text-dark_blue cursor-pointer"
        icon="fa-solid fa-right-from-bracket"
      />
    </div>
  </div>
  <slot></slot>
</template>

<script>
import { ref } from "vue";
import { useRouter, useRoute } from "vue-router";
import { resetAccessToken } from "@/utils/accessToken";
import instance from "@/utils/axios";
import { store } from "@/store/store";

export default {
  setup() {
    const router = useRouter();
    const route = useRoute();
    const username = ref(route.params.name ? route.params.name : "Guest");
    console.log("Route: ", route.params);
    // Back to index page
    function toIndex() {
      router.push({
        name: "index",
        params: {},
      });
    }

    function logOut() {
      // Reset access
      resetAccessToken(instance);

      // Back to index
      toIndex();
      window.location.reload();
    }

    function onBackToIndex() {
      toIndex();
    }

    function onLogOut() {
      logOut();
    }

    return {
      onBackToIndex,
      onLogOut,
      username,
    };
  },
  data() {
    return {
      store
    }
  }
};
</script>
