import { createRouter, createWebHashHistory } from "vue-router";
import Layout from "@/components/Layout";

const routes = [
  {
    path: "/",
    name: "Layout",
    component: Layout,
    redirect: "/home",
    children: [
      {
        path: "/home",
        name: "HomeView",
        component: () => import("@/views/HomeView"),
      },
      {
        path: "/map",
        name: "MapView",
        component: () => import("@/views/MapView"),
      },
      {
        path: "/statistics",
        name: "StatisticsView",
        component: () => import("@/views/StatisticsView"),
      },
    ],
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
