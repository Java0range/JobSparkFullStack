import type { AxiosResponse } from 'axios'
import type { CreateResume } from '@/models/ResumeModels.ts'
import $api from '@/http'

export default class ResumeService {
  static async createResume(json: CreateResume): Promise<AxiosResponse<string>> {
    return await $api.post<string>("/resumes", json)
  }
}