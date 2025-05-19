<script setup lang="ts">
import type { UserResumeResponse } from '@/models/ResumeModels.ts'
import { useRouter } from 'vue-router'

defineProps<{
  userResume: UserResumeResponse
}>();

const router = useRouter()

</script>

<template>
  <div @click="router.push({ path: `/resume/${userResume.id}` })" class="mt-2 flex flex-col items-center justify-center rounded-2xl border-2 border-gray-300 p-5 hover:shadow-[0_0_20px_rgb(255,255,255)] shadow-sky-500 transition duration-310 w-full bg-white">
    <div class="flex flex-col items-start w-full gap-2">
      <div class="flex items-center justify-between w-full gap-1">
        <h3 class="font-bold text-xl">{{ userResume.job_name }}</h3>
      </div>
      <div class="flex items-center gap-4">
        <p> {{ userResume.expected_salary }} ₽ за месяц</p>
        <div class="p-1 px-2 bg-slate-200 rounded-lg">
          <p class="text-sm text-slate-600">{{ userResume.experience > 0 ? `Стаж: ${userResume.experience} г.` : "Без опыта"}}</p>
        </div>
      </div>
      <div class="flex items-center justify-start gap-1">
        <img src="/map-pin.svg" alt="map-pin" class="h-5">
        <p>{{ userResume.city }}</p>
      </div>
    </div>
  </div>
</template>