<script setup lang="ts">
import { useUserStore } from '@/stores/user.ts'
import { useRouter } from 'vue-router'
import { ref, watch } from 'vue'
import AuthService from '@/services/AuthService.ts'

const emits = defineEmits(["changeActiveList"])

const router = useRouter();

const useStore = useUserStore()

const width = ref<number>(window.innerWidth)

const activeView = ref<string>("Главная")

async function logout () {
  await AuthService.logout()
  useStore.userInfo = null;
  await router.push({ path: "/" });
}

watch(activeView, () => {
  emits('changeActiveList', activeView.value);
})
</script>

<template>
  <div class="w-full max-sm:w-full flex justify-between items-center">
    <div>
      <img src="/JobSpark.png" alt="icon" class="h-12" />
    </div>
    <div v-if="width > 770" class="flex items-center gap-3 uppercase opacity-70 text-base">
      <p @click="activeView = 'Соискателям'" class="hover:opacity-100 text-black cursor-pointer hover:-translate-y-1 transition-all" :class="activeView === 'Соискателям' ? 'font-bold text-sky-500' : ''">Соискателям</p>
      <p @click="activeView = 'Главная'" class="hover:opacity-100 text-black cursor-pointer hover:-translate-y-1 transition-all" :class="activeView === 'Главная' ? 'font-bold text-sky-500' : ''">Главная</p>
      <p @click="activeView = 'Работодателям'" class="hover:opacity-100 text-black cursor-pointer hover:-translate-y-1 transition-all" :class="activeView === 'Работодателям' ? 'font-bold text-sky-500' : ''">Работодателям</p>
    </div>
    <div v-if="width <= 770">
      <select v-model="activeView" class="border text-sm rounded-lg block w-24 p-2.5 bg-zinc-900 border-green-500 placeholder-gray-400 text-black focus:ring-green-500 focus:border-green-500">
        <option>Главная</option>
        <option>Фильмы</option>
        <option>Сериалы</option>
        <option>Категории</option>
      </select>
    </div>
    <div>
      <button class="min-w-36 max-sm:min-w-12 bg-sky-500 hover:bg-sky-400 text-white font-bold py-2 px-4 rounded-full transition-all">
        Профиль
      </button>
    </div>
  </div>
</template>