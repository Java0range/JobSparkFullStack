import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw, RouteLocationNormalized, NavigationGuardNext } from 'vue-router'
import { useUserStore } from '@/stores/user.ts'
import AuthService from '@/services/AuthService.ts'

const checkAuth = async (
  to: RouteLocationNormalized,
  from: RouteLocationNormalized,
  next: NavigationGuardNext
) => {
  const useStore = useUserStore()
  if (!useStore.userInfo) {
    try {
      const data = await AuthService.isAuthenticated();
      if (data.data.auth) {
        useStore.userInfo = data.data.user;
        next();
      } else {
        next({ name: "Auth" });
      }
    } catch (err) {
      next({ name: "Auth" });
      console.log(err);
    }
  } else {
    if (to.path != '/auth') {
      next()
    } else {
      next({ path: to.path })
    }
  }
}


const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'home',
    component: () => import('../views/HomePage.vue')
  },
  {
    path: '/auth',
    name: 'Auth',
    component: () => import('../views/AuthPage.vue')
  },
  {
    path: '/me',
    name: 'UserAccount',
    component: () => import('../views/UserAccountPage.vue'),
    beforeEnter: checkAuth
  },
  {
    path: '/resume/:id',
    name: 'ResumePage',
    component: () => import('../views/ResumePage.vue')
  },
  {
    path: '/employer/:id',
    name: 'EmployerPage',
    component: () => import('../views/EmployerPage.vue')
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes
})

export default router