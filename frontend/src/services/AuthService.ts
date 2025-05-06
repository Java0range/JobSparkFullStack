import $api from '@/http'
import type { AxiosResponse } from 'axios'
import type { isAuthResponse } from '@/models/AuthResponse'
import type { UserResponse } from '@/models/UserResponse.ts'


export default class AuthService {
  static async login(username: string, password: string): Promise<AxiosResponse<UserResponse>> {
    const json = {
      username: username,
      password: password
    }
    return $api.post<UserResponse>("/users/login", json)
  }

  static async register(username: string, password: string): Promise<AxiosResponse<UserResponse>> {
    const json = {
      username: username,
      password: password
    }
    return $api.post<UserResponse>("/users/registration", json)
  }

  static async logout(): Promise<AxiosResponse> {
    return $api.post("/users/logout")
  }

  static async isAuthenticated(): Promise<AxiosResponse<isAuthResponse>> {
    return $api.post<isAuthResponse>("/users/is-auth")
  }
}