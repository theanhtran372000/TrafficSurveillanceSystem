import { reactive } from "vue";
import C from "@/constants"
export const store = reactive({
  profile: {},
  loading: C.__request_status__.REQUEST,
  setProfile(profile) {
    this.profile = profile;
  },
  setLoading(loading) {
    this.loading = loading;
  },
});
