<script setup lang="ts">
import ResumeCard from '@/components/ResumeCard.vue'
import type { ResumeResponse } from '@/models/ResumeModels.ts'

defineProps<{resumesList: ResumeResponse[]}>();
</script>

<template>
  <div class="flex flex-col justify-center items-center gap-5 w-full mb-80">
    <ResumeCard
      v-for="resumeInfo in resumesList"
      :key="resumeInfo.id"
      :resume-info="resumeInfo"
    />
  </div>
</template>