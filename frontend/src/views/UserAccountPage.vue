<script setup lang="ts">
import { useUserStore } from '@/stores/user.ts'
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'

const userStore = useUserStore()

const username = ref<string>("");

const router = useRouter();

onMounted(() => {
  console.log(userStore.userInfo)
  username.value = userStore.userInfo.username;
})

</script>

<template>
  <div class="bg-white w-3/5 m-auto rounded-xl shadow-[0_0_25px_rgb(255,255,255)] shadow-sky-500 mt-20">
    <header class="flex justify-between border-b border-slate-200 px-10 py-8">
      <div class="flex items-center gap-4">
        <h2 class="font-bold text-xl">{{ username }}</h2>
      </div>

      <ul class="flex items-center gap-10">
        <li @click="router.push({ path: '/' })" class="flex items-center gap-3 cursor-pointer hover:-translate-y-1 transition duration-200">
          <span>На главную</span>
        </li>
        <li class="flex items-center gap-1 cursor-pointer hover:-translate-y-1 transition duration-200">
          <span>Избранное</span>
          <img src="/yellow_star.svg" alt="star" class="h-5">
        </li>
        <li class="flex items-center gap-1 cursor-pointer hover:-translate-y-1 transition duration-200">
          <span>Выйти</span>
          <img src="/logout.svg" alt="logout" class="h-5">
        </li>
      </ul>
    </header>
    <div class="p-10">
      <div class="flex justify-between items-center mb-10">
        <h1 class="text-3xl font-bold">Резюме:</h1>
      </div>
    </div>
  </div>
</template>