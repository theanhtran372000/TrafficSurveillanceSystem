import { useRouter } from "vue-router";
const router = useRouter();
export function toIndex() {
  console.log("Back to index page!");
  router.push({
    name: "index",
    params: {},
  });
}
