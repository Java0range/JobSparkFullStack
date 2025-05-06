import { ref } from 'vue'
import { defineStore } from 'pinia'
import type { UserResponse } from '@/models/UserResponse.ts'

export const useUserStore = defineStore('user', () => {
  const userInfo = ref<UserResponse | null>(null)
  return { userInfo }
})