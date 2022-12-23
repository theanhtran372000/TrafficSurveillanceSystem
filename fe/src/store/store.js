import { reactive } from "vue";
import C from "@/constants"
export const store = reactive({
  profile: {},
  authState: C.__request_status__.REQUEST,
  setProfile(profile) {
    this.profile = profile;
  },
  setAuthState(state) {
    this.authState = state;
  },
});
