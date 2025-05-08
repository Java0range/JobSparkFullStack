import type { UserResponse } from '@/models/UserResponse.ts'

export interface EmployersModel {
  city: string,
  description: string,
  email: string,
  id: number,
  name: string,
  phone_number: string,
  remotely: boolean,
  salary: number,
  telegram_username: string,
  work_experience: number,
  user: UserResponse
}