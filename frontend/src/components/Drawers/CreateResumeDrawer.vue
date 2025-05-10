<script setup lang="ts">
import DescriptionInput from '@/components/DescriptionInput.vue'
import { ref } from 'vue'

const props = defineProps<{
  closeDrawer: () => void
}>();

const description = ref<string>("");

const resumeCreateSteps = ref<number>(1);


const experience = ref<number>(0);


const createResume = async () => {

}
</script>

<template>
  <div class="fixed top-0 left-0 h-full w-full bg-black z-10 opacity-50"></div>
  <div class="fixed top-1/2 left-1/2 -translate-y-1/2 -translate-x-1/2 rounded-3xl bg-white z-20 p-10 max-sm:w-full max-lg:w-3/4">
    <img @click="props.closeDrawer()" src="/close.svg" alt="close" class="opacity-100 hover:shadow-xl cursor-pointer transition left-full -translate-x-12 fixed" />
    <p class="text-lg font-bold mb-3">Создание Резюме Шаг {{ resumeCreateSteps }}:</p>
    <div v-if="resumeCreateSteps == 1">
      <div class="flex items-center justify-between gap-3 w-full">
        <div class="mb-5">
          <label class="block mb-2 text-sm font-medium text-black">Имя:</label>
          <input type="text" class="bg-gray-50 border-2 border-gray-300 text-black text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5">
        </div>
        <div class="mb-5">
          <label class="block mb-2 text-sm font-medium text-black">Фамилия:</label>
          <input type="text" class="bg-gray-50 border-2 border-gray-300 text-black text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5">
        </div>
      </div>
      <div class="flex items-center justify-between gap-3 w-full">
        <div class="mb-5">
          <label class="block mb-2 text-sm font-medium text-black">Профессия:</label>
          <input type="text" class="bg-gray-50 border-2 border-gray-300 text-black text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5">
        </div>
        <div class="flex flex-col w-1/2">
          <div class="flex items-center justify-start w-full">
            <label for="stage" class="block mb-2 text-sm font-medium text-black">Стаж от: {{ experience }} г.</label>
          </div>
          <input v-model="experience" id="stage" type="range" min="0" max="10" value="2" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer">
        </div>
      </div>
    </div>
    <div v-if="resumeCreateSteps == 2">
      <description-input v-model="description" desc_type="resume"/>
    </div>
    <div v-if="resumeCreateSteps == 3">
      <div class="mb-5">
        <label class="block mb-2 text-sm font-medium text-black">Образование:</label>
        <select class="border-2 text-sm rounded-lg block w-full p-2.5 bg-white border-gray-200 placeholder-gray-400 text-black focus:ring-sky-500 focus:border-sky-500">
          <option selected>Среднее</option>
          <option>Среднее Проф.</option>
          <option>Высшее</option>
        </select>
      </div>
      <div>
        <div class="mb-5">
          <label class="block mb-2 text-sm font-medium text-black">Учебное заведение:</label>
          <input type="text" class="bg-gray-50 border-2 border-gray-300 text-black text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5">
        </div>
      </div>
      <div>
        <div class="mb-5">
          <label class="block mb-2 text-sm font-medium text-black">Факультет:</label>
          <input type="text" class="bg-gray-50 border-2 border-gray-300 text-black text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5">
        </div>
      </div>
      <div class="flex items-center justify-between w-full gap-3 mb-3">
        <div class="w-full">
          <div class="flex items-center justify-start w-full">
            <label for="countries" class="block mb-2 text-sm font-medium text-black">Город:</label>
          </div>
          <select class="border-2 text-sm rounded-lg block w-full p-2.5 bg-white border-gray-200 placeholder-gray-400 text-black focus:ring-sky-500 focus:border-sky-500">
            <option selected>Не указано</option>
            <option>Москва</option>
            <option>Санкт-Петербург</option>
            <option>Владивосток</option>
            <option>Воронеж</option>
            <option>Екатеринбург</option>
            <option>Казань</option>
            <option>Калуга</option>
            <option>Краснодар</option>
            <option>Красноярск</option>
            <option>Нижний Новгород</option>
            <option>Новосибирск</option>
            <option>Ростов-на-Дону</option>
            <option>Самара</option>
            <option>Саратов</option>
            <option>Сочи</option>
            <option>Уфа</option>
            <option>Ярославль</option>
            <option>Челябинск</option>
            <option>Саратов</option>
            <option>Иннополис</option>
            <option>Липецк</option>
            <option>Владимир</option>
            <option>Белгород</option>
            <option>Брянск</option>
            <option>Иркутск</option>
            <option>Калининград</option>
            <option>Кемерово</option>
            <option>Кострома</option>
            <option>Курган</option>
            <option>Курск</option>
            <option>Мурманск</option>
            <option>Омск</option>
            <option>Оренбург</option>
            <option>Пенза</option>
            <option>Рязань</option>
            <option>Тамбов</option>
            <option>Томск</option>
            <option>Тула</option>
            <option>Тюмень</option>
            <option>Волгоград</option>
          </select>
        </div>
        <div class="w-full">
          <div class="flex items-center justify-start w-full">
            <label class="block mb-2 text-sm font-medium text-black">Уровень дохода от:</label>
          </div>
          <input type="number" aria-describedby="helper-text-explanation" class="bg-gray-50 border-2 border-gray-200 text-gray-900 text-sm rounded-lg focus:ring-sky-500 focus:border-sky-500 block w-full p-2.5" placeholder="100000" required />
        </div>
      </div>
    </div>
    <div class="flex items-center justify-center w-full">
      <button @click="resumeCreateSteps != 3 ? resumeCreateSteps += 1 : createResume" class="min-w-36 max-sm:min-w-12 bg-sky-500 hover:bg-sky-400 text-white font-bold py-2 px-4 rounded-xl transition-all">
        {{ resumeCreateSteps != 3 ? "Дальше" : "Создать"}}
      </button>
    </div>
  </div>
</template>