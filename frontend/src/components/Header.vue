<script setup lang="ts">
import { useRouter } from 'vue-router'
import { ref, watch } from 'vue'

const emits = defineEmits(["changeActiveList"]);

const props = defineProps<{
  selectedPage: string
}>();

const router = useRouter();

const width = ref<number>(window.innerWidth)

const activeView = ref<string>("Главная")

watch(props, () => {
  activeView.value = props.selectedPage;
});

watch(activeView, () => {
  emits('changeActiveList', activeView.value);
})
</script>

<template>
  <div class="w-full max-sm:w-full flex justify-between items-center">
    <div>
      <img src="/JobSpark.png" alt="icon" class="h-12" />
    </div>
    <div v-if="width > 450" class="flex items-center gap-3 uppercase opacity-70 text-base max-md:flex-col">
      <p @click="activeView = 'Соискателям'" class="hover:opacity-100 text-black cursor-pointer hover:-translate-y-1 transition-all" :class="activeView === 'Соискателям' ? 'font-bold text-sky-500' : ''">Соискателям</p>
      <p @click="activeView = 'Главная'" class="hover:opacity-100 text-black cursor-pointer hover:-translate-y-1 transition-all" :class="activeView === 'Главная' ? 'font-bold text-sky-500' : ''">Главная</p>
      <p @click="activeView = 'Работодателям'" class="hover:opacity-100 text-black cursor-pointer hover:-translate-y-1 transition-all" :class="activeView === 'Работодателям' ? 'font-bold text-sky-500' : ''">Работодателям</p>
    </div>
    <div v-if="width <= 450">
      <select v-model="activeView" class="border text-sm rounded-lg block w-24 p-2.5 bg-zinc-200 border-sky-500 placeholder-gray-400 text-black focus:ring-sky-500 focus:border-sky-500">
        <option>Главная</option>
        <option>Соискателям</option>
        <option>Работодателям</option>
      </select>
    </div>
    <div>
      <button @click="router.push({ path: '/me' })" class="min-w-36 max-sm:min-w-12 bg-sky-500 hover:bg-sky-400 text-white font-bold py-2 px-4 rounded-full transition-all">
        Профиль
      </button>
    </div>
  </div>
</template>