<template>
  <div
    v-if="store.loading === true"
    class="w-screen h-screen bg-white flex items-center justify-center"
  >
    <img src="@/assets/images/icons8-fiat-500.gif" />
  </div>
  <component :is="layout" v-if="store.loading === false">
    <router-view />
  </component>
</template>

<script>
import { computed } from "vue";
import { useRoute } from "vue-router";
import C from "./constants";
import { store } from "@/store/store";

export default {
  setup() {
    const route = useRoute();
    return {
      layout: computed(() => route.meta.layout || C.__default_layout__),
    };
  },
  data() {
    return {
      store,
    };
  },
};
</script>
