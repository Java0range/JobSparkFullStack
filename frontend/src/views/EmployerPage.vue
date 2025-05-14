<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router'
import { onMounted, ref } from 'vue'
import DescriptionView from '@/components/DescriptionView.vue'
import type { EmployersModel } from '@/models/EmployersModels.ts'
import EmployersService from '@/services/EmployersService.ts'

const router = useRouter();

const route = useRoute();

const employer = ref<EmployersModel>({
  "city": "",
  "description": "",
  "email": "",
  "id": 0,
  "name": "",
  "phone_number": "",
  "remotely": false,
  "salary": 0,
  "telegram_username": "",
  "user": {
    "id": 0,
    "username": ""
  },
  "work_experience": 0
});


onMounted(async () => {
  try {
    const data = await EmployersService.fetchEmployer(route.params.id);
    if (data.data) {
      employer.value = data.data;
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
          <div class="flex items-center justify-start gap-3 w-full mt-3">
            <h3 class="font-bold text-xl">{{ employer.name }}</h3>
            <div class="p-1 px-2 bg-slate-200 rounded-lg">
              <p class="text-sm text-slate-600">{{ employer.work_experience > 0 ? `Стаж: ${employer.work_experience} г.` : "Без опыта"}}</p>
            </div>
            <div class="p-1 px-2 bg-slate-200 rounded-lg">
              <p class="text-sm text-slate-600">{{ employer.salary > 0 ? `От: ${employer.salary} ₽.` : "Зп не указана"}}</p>
            </div>
            <div v-if="employer.remotely" class="p-1 px-2 bg-slate-200 rounded-lg">
              <p class="text-sm text-slate-600">Можно удалённо</p>
            </div>
          </div>
          <div class="flex items-center justify-start gap-3 w-full mt-3">
            <div class="flex items-center gap-1">
              <img src="/map-pin.svg" alt="map-pin" class="h-6">
              <p class="text-lg">{{ employer.city }}</p>
            </div>
          </div>
          <div class="flex items-center justify-start w-full mt-3">
            <DescriptionView :description="employer.description" />
          </div>
          <div v-if="employer.email || employer.phone_number || employer.telegram_username" class="flex items-center justify-start w-full mt-3">
            <div class="flex flex-col items-center border-2 border-slate-400 bg-slate-100 p-2 rounded-2xl gap-2">
              <div class="flex items-center justify-start w-full">
                <h3 class="text-lg font-bold">Контакты:</h3>
              </div>
              <div v-if="employer.telegram_username" class="flex items-center gap-1 w-full">
                <img src="/telegram-icon.svg" alt="telegram icon" class="h-5">
                <p>{{ employer.telegram_username }}</p>
              </div>
              <div v-if="employer.phone_number" class="flex items-center gap-1 w-full">
                <img src="/phone.svg" alt="phone" class="h-5">
                <p>{{ employer.phone_number }}</p>
              </div>
              <div v-if="employer.email" class="flex items-center gap-1 w-full">
                <img src="/email.svg" alt="email" class="h-5">
                <p>{{ employer.email }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>