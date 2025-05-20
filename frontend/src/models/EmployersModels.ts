import type { LiteUserResponse } from '@/models/UserResponse.ts'

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
  user: LiteUserResponse
}


export interface UserEmployersModel {
  city: string,
  description: string,
  email: string,
  id: number,
  name: string,
  phone_number: string,
  remotely: boolean,
  salary: number,
  telegram_username: string,
  work_experience: number
}


export interface CreateEmployer {
  name: string,
  salary: number,
  work_experience: number,
  remotely: boolean,
  description: string,
  city: string,
  phone_number: string,
  email: string,
  telegram_username: string
}