<script setup lang="ts">
import { onMounted, ref } from 'vue'
import type { EmployersModel } from '@/models/EmployersModels.ts'
import EmployersCardsList from '@/components/EmployersCardsList.vue'
import EmployersService from '@/services/EmployersService.ts'


const employersInfoList = ref<EmployersModel[]>([]);

const words = ref<string>();

const experienceFrom = ref<number>(0);

const city = ref<string>("Не указано");

const salary = ref<number>();

const remotely = ref<boolean>(false);

const test = async () => {
  const data = await EmployersService.fetchEmployers(
    city.value,
    words.value,
    remotely.value,
    Number(salary.value),
    experienceFrom.value
  )
  employersInfoList.value = data.data;
}

onMounted(async () => {
  const data = await EmployersService.fetchEmployers(
    "Не указано",
    undefined,
    false,
    0,
    0
  )
  employersInfoList.value = data.data;
})
</script>

<template>
  <div class="w-full flex justify-center mt-12">
    <div class="flex flex-col items-center w-2/8 gap-4">
      <div class="flex flex-col items-center justify-center rounded-2xl border border-gray-200 p-5 w-full">
        <div class="flex items-center justify-start w-full">
          <label for="countries" class="block mb-2 text-sm font-medium text-black">Город:</label>
        </div>
        <select v-model="city" class="border-2 text-sm rounded-lg block w-full p-2.5 bg-white border-sky-500 placeholder-gray-400 text-black focus:ring-sky-500 focus:border-sky-500">
          <option>Не указано</option>
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
      <div class="flex flex-col justify-center items-center rounded-2xl border border-gray-200 p-5 w-full">
        <div class="flex items-center justify-start w-full">
          <label for="salary" class="block mb-2 text-sm font-medium text-black">Уровень дохода от:</label>
        </div>
        <input v-model="salary" type="number" id="salary" aria-describedby="helper-text-explanation" class="bg-gray-50 border-2 border-sky-500 text-gray-900 text-sm rounded-lg focus:ring-sky-500 focus:border-sky-500 block w-full p-2.5" placeholder="100000" required />
      </div>
      <div class="flex flex-col justify-center items-center rounded-2xl border border-gray-200 p-5 w-full">
        <div class="flex items-center justify-start w-full">
          <label for="stage" class="block mb-2 text-sm font-medium text-black">Стаж от: {{ experienceFrom }} г.</label>
        </div>
        <input v-model="experienceFrom" id="stage" type="range" min="0" max="10" value="2" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer">
      </div>
      <div class="flex flex-col justify-start items-center rounded-2xl border border-gray-200 p-5 w-full">
        <div class="inline-flex items-center gap-2 justify-start w-full">
          <div class="relative inline-block w-11 h-5">
            <input v-model="remotely" id="switch-component-on" type="checkbox" class="peer appearance-none w-11 h-5 bg-slate-200 rounded-full checked:bg-sky-500 cursor-pointer transition-colors duration-300" />
            <label for="switch-component-on" class="absolute top-0 left-0 w-5 h-5 bg-white rounded-full border border-slate-300 shadow-sm transition-transform duration-300 peer-checked:translate-x-6 peer-checked:border-sky-500 cursor-pointer">
            </label>
          </div>
          <label for="switch-component-on" class="text-slate-600 text-sm cursor-pointer">Можно удалённо</label>
        </div>
      </div>
    </div>
    <div class="flex-2 flex-col justify-center items-center mx-10 h-full">
      <div class="flex items-center mb-7">
        <div class="flex items-center bg-gray-200 rounded-full w-full">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-gray-400 ml-4">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
          <input
            v-model="words"
            type="text"
            placeholder="Профессия, Должность..."
            class="w-full bg-transparent text-black px-4 py-3 focus:outline-none placeholder-gray-400"
          />
          <button @click="test" class="px-6 py-3 bg-sky-500 hover:bg-sky-400 text-white rounded-full transition-colors">
            Найти
          </button>
        </div>
      </div>
      <EmployersCardsList :employers-info-list="employersInfoList"/>
    </div>
  </div>
</template>