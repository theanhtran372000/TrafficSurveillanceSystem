<template>
  <div
    v-if="store.authState === C.__request_status__.REQUEST"
    
    class="fixed inset-0 bg-white flex items-center justify-center opacity-80"
  >
    <img src="@/assets/images/icons8-fiat-500.gif" />
  </div>
</template>
<script>
import { store } from "@/store/store";
import C from "@/constants";

export default {
  data() {
    console.log('store.authState: ', store.authState);
    return {
      store,
      C,
    };
  },
};
</script>
