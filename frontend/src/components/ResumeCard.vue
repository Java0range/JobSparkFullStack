<script setup lang="ts">
import type { ResumeResponse } from '@/models/ResumeModels.ts'
import { useRouter } from 'vue-router'

defineProps<{
  resumeInfo: ResumeResponse
}>();

const router = useRouter()

</script>

<template>
  <div @click="router.push({ path: `/resume/${resumeInfo.id}` })" class="flex flex-col items-center justify-center rounded-2xl border-2 border-gray-300 p-5 hover:shadow-[0_0_20px_rgb(255,255,255)] shadow-sky-500 transition duration-310 w-full bg-white">
    <div class="flex flex-col items-start w-full gap-2">
      <div class="flex items-center justify-between w-full gap-1">
        <h3 class="font-bold text-xl">{{ resumeInfo.job_name }}</h3>
        <img src="/yellow_star.svg" alt="star" class="h-6 opacity-70 hover:-translate-y-1 hover:opacity-100 transition duration-200" />
      </div>
      <div class="flex items-center gap-4">
        <p> {{ resumeInfo.expected_salary }} ₽ за месяц</p>
        <div class="p-1 px-2 bg-slate-200 rounded-lg">
          <p class="text-sm text-slate-600">{{ resumeInfo.experience > 0 ? `Стаж: ${resumeInfo.experience} г.` : "Без опыта"}}</p>
        </div>
      </div>
      <div class="flex items-center justify-start gap-1">
        <img src="/map-pin.svg" alt="map-pin" class="h-5">
        <p>{{ resumeInfo.city }}</p>
      </div>
      <div class="flex items-center justify-start gap-1">
        <p>Пользователь:</p>
        <p class="font-bold text-sky-500">{{ resumeInfo.user.username }}</p>
      </div>
    </div>
  </div>
</template>