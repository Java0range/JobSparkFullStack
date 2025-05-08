<script setup lang="ts">
import type { EmployersModel } from '@/models/EmployersResponse.ts'
import EmployersCart from '@/components/EmployersCard.vue'

defineProps<{employersInfoList: EmployersModel[]}>();
</script>

<template>
  <div class="flex flex-col justify-center items-center gap-5 w-full mb-80">
    <EmployersCart
      v-for="employerInfo in employersInfoList"
      :key="employerInfo.id"
      :employerInfo="employerInfo"
    />
  </div>
</template>