<script setup lang="ts">
import DescriptionInput from '@/components/DescriptionInput.vue'
import { ref } from 'vue'
import EmployersService from '@/services/EmployersService.ts'

const props = defineProps<{
  closeDrawer: () => void
}>();

const resumeCreateSteps = ref<number>(1);

const name = ref<string>("");

const salary = ref<number>(0);

const experience = ref<number>(0);

const remotely = ref<boolean>(false);

const description = ref<string>("");

const city = ref<string>("Не указано");

const phone_number = ref<string>("");

const email = ref<string>("");

const telegram_username = ref<string>("");

const createEmployerDisable = ref<boolean>(false);


const createEmployer = async () => {
  const json = {
    name: name.value,
    salary: salary.value,
    work_experience: Number(experience.value),
    remotely: remotely.value,
    description: description.value,
    city: city.value,
    phone_number: phone_number.value,
    email: email.value,
    telegram_username: telegram_username.value
  }
  createEmployerDisable.value = true;
  try {
    const data = await EmployersService.createEmployer(json);
    if (data.data === "ok") {
      createEmployerDisable.value = false;
      props.closeDrawer();
    }
  } catch (err) {
    createEmployerDisable.value = false;
    props.closeDrawer();
    console.error(err);
  }
}
</script>

<template>
  <div class="fixed top-0 left-0 h-full w-full bg-black z-10 opacity-50"></div>
  <div class="fixed top-1/2 left-1/2 -translate-y-1/2 -translate-x-1/2 rounded-3xl bg-white z-20 p-10 max-sm:w-full max-lg:w-3/4">
    <img @click="props.closeDrawer()" src="/close.svg" alt="close" class="opacity-100 hover:shadow-xl cursor-pointer transition left-full -translate-x-12 fixed" />
    <p class="text-lg font-bold mb-3">Создание Вакансии Шаг {{ resumeCreateSteps }}:</p>
    <div v-if="resumeCreateSteps == 1">
      <div class="flex items-center justify-between gap-3 w-full">
        <div class="mb-5">
          <label class="block mb-2 text-sm font-medium text-black">Вакансия:</label>
          <input v-model="name" type="text" class="bg-gray-50 border-2 border-gray-300 text-black text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5">
        </div>
        <div class="flex flex-col w-1/2">
          <div class="flex items-center justify-start w-full">
            <label for="stage" class="block mb-2 text-sm font-medium text-black">Стаж от: {{ experience }} г.</label>
          </div>
          <input v-model="experience" id="stage" type="range" min="0" max="10" value="2" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer">
        </div>
      </div>
      <div class="flex items-center justify-between w-full gap-3 mb-3">
        <div class="w-full">
          <div class="flex items-center justify-start w-full">
            <label for="countries" class="block mb-2 text-sm font-medium text-black">Город:</label>
          </div>
          <select v-model="city" class="border-2 text-sm rounded-lg block w-full p-2.5 bg-white border-gray-200 placeholder-gray-400 text-black focus:ring-sky-500 focus:border-sky-500">
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
        <div class="w-full">
          <div class="flex items-center justify-start w-full">
            <label class="block mb-2 text-sm font-medium text-black">Уровень дохода от:</label>
          </div>
          <input v-model="salary" type="number" aria-describedby="helper-text-explanation" class="bg-gray-50 border-2 border-gray-200 text-gray-900 text-sm rounded-lg focus:ring-sky-500 focus:border-sky-500 block w-full p-2.5" placeholder="100000" required />
        </div>
      </div>
      <div class="flex items-center justify-center w-full mt-1 mb-4">
        <div class="inline-flex items-center gap-2 justify-center w-full">
          <div class="relative inline-block w-11 h-5">
            <input v-model="remotely" id="switch-component-on" type="checkbox" class="peer appearance-none w-11 h-5 bg-slate-200 rounded-full checked:bg-sky-500 cursor-pointer transition-colors duration-300" />
            <label for="switch-component-on" class="absolute top-0 left-0 w-5 h-5 bg-white rounded-full border border-slate-300 shadow-sm transition-transform duration-300 peer-checked:translate-x-6 peer-checked:border-sky-500 cursor-pointer">
            </label>
          </div>
          <label for="switch-component-on" class="text-slate-600 text-sm cursor-pointer">Можно удалённо</label>
        </div>
      </div>
    </div>
    <div v-if="resumeCreateSteps == 2">
      <description-input v-model="description" desc_type="employer"/>
    </div>
    <div v-if="resumeCreateSteps == 3">
      <div class="flex items-center justify-between gap-3 w-full">
        <div class="mb-5">
          <label class="block mb-2 text-sm font-medium text-black">Email:</label>
          <input v-model="email" type="text" class="bg-gray-50 border-2 border-gray-300 text-black text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5">
        </div>
        <div class="mb-5">
          <label class="block mb-2 text-sm font-medium text-black">Номер Телефона:</label>
          <input v-model="phone_number" type="text" class="bg-gray-50 border-2 border-gray-300 text-black text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5">
        </div>
      </div>
      <div class="flex items-center justify-center w-full">
        <div class="mb-5">
          <label class="block mb-2 text-sm font-medium text-black">Telegram Username:</label>
          <input v-model="telegram_username" type="text" class="bg-gray-50 border-2 border-gray-300 text-black text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5">
        </div>
      </div>
    </div>
    <div class="flex items-center justify-center w-full">
      <button @click="resumeCreateSteps != 3 ? resumeCreateSteps += 1 : createEmployer()" class="min-w-36 max-sm:min-w-12 bg-sky-500 hover:bg-sky-400 text-white font-bold py-2 px-4 rounded-xl transition-all">
        {{ resumeCreateSteps != 3 ? "Дальше" : "Создать"}}
      </button>
    </div>
  </div>
</template>