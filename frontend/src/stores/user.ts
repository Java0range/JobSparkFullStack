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
  const getUserResume = () => {
    return userInfo.value?.resume
  }
  const getUserEmployer = () => {
    return userInfo.value?.employer
  }
  return { userInfo, logout, getUsername, getUserResume, getUserEmployer }
})