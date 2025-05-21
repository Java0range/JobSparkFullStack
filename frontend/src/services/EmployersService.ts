import type { CreateEmployer, EmployersModel } from '@/models/EmployersModels.ts'
import type { AxiosResponse } from 'axios'
import $api from '@/http'

export default class EmployersService {
  static async fetchEmployers(
    city: string,
    words: string | undefined,
    remotely: boolean,
    salary_from: number,
    experience_from: number
  ): Promise<AxiosResponse<EmployersModel[]>> {
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
    if (remotely) {
      if (filter) {
        filter += `&remotely=${remotely}`
      } else {
        filter += `?remotely=${remotely}`
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
    return $api.get<EmployersModel[]>("/employers" + filter)
  }

  static async createEmployer(json: CreateEmployer): Promise<AxiosResponse<string>> {
    return $api.post<string>("/employers", json)
  }

  static async updateEmployer(json: CreateEmployer): Promise<AxiosResponse<string>> {
    return $api.put<string>("/employers", json)
  }

  static async fetchEmployer(id: string | string[]): Promise<AxiosResponse<EmployersModel>> {
    return $api.get<EmployersModel>("/employers/" + id)
  }
}