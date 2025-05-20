import type { UserResumeResponse } from '@/models/ResumeModels.ts'
import type { UserEmployersModel } from '@/models/EmployersModels.ts'


export interface UserResponse {
  id: number,
  username: string,
  resume: UserResumeResponse | null,
  employer: UserEmployersModel | null
}

export interface LiteUserResponse {
  id: number,
  username: string
}