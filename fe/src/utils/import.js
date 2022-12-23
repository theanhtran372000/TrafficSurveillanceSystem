import { defineAsyncComponent } from "vue";

export function registerGlobalComponents(app) {
  console.log(app);
  app.component(
    "FooterLayout",
    defineAsyncComponent(() => import("@/layouts/FooterLayout"))
  );
  app.component(
    "HeaderLayout",
    defineAsyncComponent(() => import("@/layouts/HeaderLayout"))
  );
  app.component(
    "EmptyLayout",
    defineAsyncComponent(() => import("@/layouts/EmptyLayout"))
  );
}
