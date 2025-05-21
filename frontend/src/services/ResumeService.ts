import type { AxiosResponse } from 'axios'
import type { CreateResume, ResumeResponse } from '@/models/ResumeModels.ts'
import $api from '@/http'

export default class ResumeService {
  static async fetchResumes(
    city: string,
    words: string | undefined,
    salary_from: number,
    experience_from: number
  ): Promise<AxiosResponse<ResumeResponse[]>> {
    let filter = "";
    if (words) {
      filter += `?words=${words.split(' ').join(';')}`
    }
    if (city != "Не указано") {
      if (filter) {
        filter += `&city=${city}`
      } else {
        filter += `?city=${city}`
      }
    }
    if (salary_from || salary_from > 0) {
      if (filter) {
        filter += `&salary=${salary_from}`
      } else {
        filter += `?salary=${salary_from}`
      }
    }
    if (experience_from || experience_from > 0) {
      if (filter) {
        filter += `&experience=${experience_from}`
      } else {
        filter += `?experience=${experience_from}`
      }
    }
    return $api.get<ResumeResponse[]>("/resumes" + filter)
  }
  static async createResume(json: CreateResume): Promise<AxiosResponse<string>> {
    return await $api.post<string>("/resumes", json)
  }
  static async updateResume(json: CreateResume): Promise<AxiosResponse<string>> {
    return await $api.put<string>("/resumes", json)
  }
  static async fetchResume(id: string | string[]): Promise<AxiosResponse<ResumeResponse>> {
    return $api.get<ResumeResponse>(`/resumes/${id}`)
  }
}