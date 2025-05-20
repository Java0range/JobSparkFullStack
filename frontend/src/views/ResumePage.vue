<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router'
import DescriptionView from '@/components/DescriptionView.vue'
import type { ResumeResponse } from '@/models/ResumeModels.ts'
import { onMounted, ref } from 'vue'
import ResumeService from '@/services/ResumeService.ts'

const router = useRouter();

const route = useRoute();

const resume = ref<ResumeResponse>({
  "city": "",
  "description": "adfasf",
  "education": "",
  "educational_institution": "",
  "email": "",
  "expected_salary": 0,
  "experience": 0,
  "faculty": "",
  "id": 0,
  "job_name": "",
  "name": "",
  "phone_number": "",
  "surname": "",
  "telegram_username": "",
  "user": {
    "id": 0,
    "username": ""
  }
});


onMounted(async () => {
  try {
    const data = await ResumeService.fetchResume(route.params.id);
    if (data.data) {
      resume.value = data.data;
    }
  } catch (err) {
    console.log(err)
  }
})
</script>

<template>
  <div class="flex justify-center items-center h-full w-full">
    <div class="flex-col items-center w-3/4 max-lg:w-full mt-5">
      <header class="w-full max-sm:w-full flex justify-between items-center">
        <div>
          <img src="/JobSpark.png" alt="icon" class="h-12" />
        </div>
        <div class="flex items-center gap-3 uppercase opacity-70 text-base max-md:flex-col">
          <p @click="router.push({ path: '/' })" class="hover:opacity-100 text-black cursor-pointer hover:-translate-y-1 transition-all font-bold text-sky-500">Главная</p>
        </div>
        <div>
          <button @click="router.push({ path: '/me' })" class="min-w-36 max-sm:min-w-12 bg-sky-500 hover:bg-sky-400 text-white font-bold py-2 px-4 rounded-full transition-all">
            Профиль
          </button>
        </div>
      </header>
      <div class="flex justify-center w-full mt-12">
        <div class="flex flex-col items-center w-1/2 rounded-2xl border-2 border-gray-300 p-7 shadow-[0_0_20px_rgb(255,255,255)] shadow-sky-500 transition duration-310 bg-white">
          <div class="flex items-center gap-1 justify-start w-full">
            <img src="/user.svg" alt="user" class="h-12">
            <h3 class="text-2xl font-bold">{{ resume.surname }}</h3>
            <h3 class="text-2xl font-bold">{{ resume.name }}</h3>
          </div>
          <div class="flex items-center justify-start gap-3 w-full mt-3">
            <h3 class="font-bold text-xl">{{ resume.job_name }}</h3>
            <div class="p-1 px-2 bg-slate-200 rounded-lg">
              <p class="text-sm text-slate-600">{{ resume.experience > 0 ? `Стаж: ${resume.experience} г.` : "Без опыта"}}</p>
            </div>
            <div class="p-1 px-2 bg-slate-200 rounded-lg">
              <p class="text-sm text-slate-600">{{ resume.expected_salary > 0 ? `От: ${resume.expected_salary} ₽` : "Зп не указана"}}</p>
            </div>
          </div>
          <div class="flex items-center justify-start gap-3 w-full mt-3">
            <div class="flex items-center gap-1">
              <img src="/map-pin.svg" alt="map-pin" class="h-6">
              <p class="text-lg">{{ resume.city }}</p>
            </div>
          </div>
          <div class="flex items-center justify-start w-full mt-3">
            <div class="flex flex-col items-start border-2 border-slate-400 bg-slate-100 p-2 rounded-2xl">
              <div class="flex items-center gap-1">
                <p class="text-lg">Образование:</p>
                <p class="text-lg text-sky-500">{{ resume.education }}</p>
              </div>
              <div class="flex items-center gap-1 mt-1">
                <p class="text-lg">Учреждение:</p>
                <p class="text-lg text-sky-500">{{ resume.educational_institution }}</p>
              </div>
              <div v-if="resume.faculty" class="flex items-center gap-1 mt-1">
                <p class="text-lg">Факультет:</p>
                <p class="text-lg text-sky-500">{{ resume.faculty }}</p>
              </div>
            </div>
          </div>
          <div class="flex items-center justify-start w-full mt-3">
            <DescriptionView :description="resume.description" />
          </div>
          <div v-if="resume.email || resume.phone_number || resume.telegram_username" class="flex items-center justify-start w-full mt-3">
            <div class="flex flex-col items-center border-2 border-slate-400 bg-slate-100 p-2 rounded-2xl gap-2">
              <div class="flex items-center justify-start w-full">
                <h3 class="text-lg font-bold">Контакты:</h3>
              </div>
              <div v-if="resume.telegram_username" class="flex items-center gap-1 w-full">
                <img src="/telegram-icon.svg" alt="telegram icon" class="h-5">
                <p>{{ resume.telegram_username }}</p>
              </div>
              <div v-if="resume.phone_number" class="flex items-center gap-1 w-full">
                <img src="/phone.svg" alt="phone" class="h-5">
                <p>{{ resume.phone_number }}</p>
              </div>
              <div v-if="resume.email" class="flex items-center gap-1 w-full">
                <img src="/email.svg" alt="email" class="h-5">
                <p>{{ resume.email }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>