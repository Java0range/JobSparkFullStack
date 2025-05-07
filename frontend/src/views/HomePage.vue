<script setup lang="ts">
import AuthView from '@/views/AuthPage.vue'
import Header from '@/components/Header.vue'
</script>
<template>
  <div class="flex justify-center items-center h-full w-full">
    <div class="flex-col items-center justify-center w-3/4 mt-5">
      <Header />
      <div class="w-full flex justify-center items-center mt-12">
        <img src="/JobSparkFull.png" alt="icon" class="h-36" />
      </div>
      <div class="w-full flex justify-center items-center mt-10">
          <div class="flex items-center bg-gray-200 rounded-full w-2/4">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-gray-400 ml-4">
              <circle cx="11" cy="11" r="8"></circle>
              <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
            <input
              type="text"
              placeholder="Профессия, Должность..."
              class="w-full bg-transparent text-black px-4 py-3 focus:outline-none placeholder-gray-400"
            />
            <button class="px-6 py-3 bg-sky-500 hover:bg-sky-400 text-white rounded-full transition-colors">
              Найти
            </button>
          </div>
      </div>
    </div>
  </div>
</template>