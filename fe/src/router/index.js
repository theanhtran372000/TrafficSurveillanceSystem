import { createRouter, createWebHistory } from "vue-router";
import IndexView from "../views/IndexView.vue";
import NotFoundView from "../views/NotFoundView.vue";

const routes = [
  {
    path: "/index",
    name: "index",
    meta: {
      layout: "FooterLayout",
    },
    component: IndexView,
  },
  {
    path: "/",
    redirect: "/index",
  },
  {
    path: "/login",
    name: "login",
    meta: {
      layout: "FooterLayout",
    },
    component: () =>
      import(/* webpackChunkName: "login" */ "../views/LoginView.vue"),
  },
  {
    path: "/register",
    name: "register",
    meta: {
      layout: "FooterLayout",
    },
    component: () =>
      import(/* webpackChunkName: "register" */ "../views/RegisterView.vue"),
  },
  {
    path: "/home",
    name: "home",
    meta: {
      layout: "HeaderLayout",
    },
    component: () =>
      import(/* webpackChunkName: "home" */ "../views/HomeView.vue"),
  },
  {
    path: "/detail",
    name: "detail",
    meta: {
      layout: "HeaderLayout",
    },
    component: () =>
      import(/* webpackChunkName: "detail" */ "../views/DetailView.vue"),
  },
  {
    path: "/:pathMatch(.*)*",
    component: NotFoundView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
