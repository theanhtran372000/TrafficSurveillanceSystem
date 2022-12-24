<template>
  <FullPageLoading />
  <component
    :is="layout"
    v-if="store.authState !== C.__request_status__.REQUEST"
  >
    <router-view />
  </component>
</template>

<script>
import { computed } from "vue";
import { useRoute } from "vue-router";
import C from "./constants";
import { store } from "@/store/store";
import FullPageLoading from "@/components/FullPageLoading.vue";

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
      C,
    };
  },
  components: {
    FullPageLoading,
  },
};
</script>
