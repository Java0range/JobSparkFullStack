import type { UserResponse } from '@/models/UserResponse.ts'

export interface ResumeResponse {
  id: number,
  name: string,
  surname: string,
  job_name: string,
  description: string,
  education: string,
  educational_institution: string,
  faculty: string,
  experience: number,
  expected_salary: number,
  city: string,
  phone_number: string,
  email: string,
  telegram_username: string,
  user: UserResponse
}


export interface CreateResume {
  city: string,
  description: string,
  edu_institution: string,
  education: string,
  email: string
  expected_salary: number,
  experience: number,
  faculty: string,
  job_name: string,
  name: string,
  phone_number: string,
  surname: string,
  telegram_username: string
}