import { ref } from 'vue'
import { defineStore } from 'pinia'
import type { UserResponse } from '@/models/UserResponse.ts'

export const useUserStore = defineStore('user', () => {
  const userInfo = ref<UserResponse | null>(null)
  const logout = () => {
    userInfo.value = null
  }
  const getUsername = () => {
    return userInfo.value?.username || ''
  }
  return { userInfo, logout, getUsername }
})