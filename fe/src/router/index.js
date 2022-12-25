import { useLogin } from "@/composables/useLogin";
import { store } from "@/store/store";
import { createRouter, createWebHistory } from "vue-router";
import IndexView from "../views/IndexView.vue";
import NotFoundView from "../views/NotFoundView.vue";
import C from "@/constants";
import { getAccessToken } from "@/utils/accessToken";

const routes = [
  {
    path: "/index",
    name: "index",
    meta: {
      layout: "FooterLayout",
      isPrivate: false,
    },
    component: IndexView,
  },
  {
    path: "/",
    redirect: "/index",
    meta: {
      isPrivate: false,
    },
  },
  {
    path: "/login",
    name: "login",
    meta: {
      layout: "FooterLayout",
      isPrivate: false,
    },
    component: () =>
      import(/* webpackChunkName: "login" */ "../views/LoginView.vue"),
  },
  {
    path: "/register",
    name: "register",
    meta: {
      layout: "FooterLayout",
      isPrivate: false,
    },
    component: () =>
      import(/* webpackChunkName: "register" */ "../views/RegisterView.vue"),
  },
  {
    path: "/home",
    name: "home",
    meta: {
      layout: "HeaderLayout",
      isPrivate: true,
    },
    component: () =>
      import(/* webpackChunkName: "home" */ "../views/HomeView.vue"),
  },
  {
    path: "/detail/:id",
    name: "detail",
    meta: {
      layout: "HeaderLayout",
      isPrivate: true,
    },
    component: () =>
      import(/* webpackChunkName: "detail" */ "../views/DetailView.vue"),
  },
  {
    path: "/:pathMatch(.*)*",
    component: NotFoundView,
    meta: {
      isPrivate: false,
    },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach(async (to, from, next) => {
  console.log("to, from: ", to, from);
  console.log("getAccessToken(): ", getAccessToken());

  if (to?.meta?.isPrivate) {
    const { getMyProfile } = useLogin();
    const isAuthenticated = await getMyProfile();
    if (isAuthenticated?.statusCode === 401 && to.name !== "login") {
      next({ name: "login" });
    }
    store.setProfile(isAuthenticated.data);
    if (
      isAuthenticated?.statusCode === 200 &&
      (to.name === "index" || to.name === "login")
    ) {
      next({ name: "home" });
    }
  } else {
    if (getAccessToken()) {
      next({ name: "home" });
    }
    store.setAuthState(null);
  }
  next();
});

export default router;
