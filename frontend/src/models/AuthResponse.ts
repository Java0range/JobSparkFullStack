import type { UserResponse } from '@/models/UserResponse.ts'

export interface isAuthResponse {
  auth: boolean,
  user: UserResponse
}