<script setup lang="ts">
import { ref } from 'vue'
import AuthService from '@/services/AuthService.ts'
import { useUserStore } from '@/stores/user.ts'
import { useRouter } from 'vue-router'

const errorTitle = ref<string>("Invalid uusername or password");
const errorFlag = ref<boolean>(false);
const loginWindowFlag = ref<boolean>(true);

const registerUsername = ref<string>("");
const registerPassword = ref<string>("");

const loginUsername = ref<string>("");
const loginPassword = ref<string>("");

const userStore = useUserStore();

const router = useRouter();

const loginUser = async () => {
  try {
    const data = await AuthService.login(loginUsername.value, loginPassword.value);
    if (data.status === 200) {
      userStore.userInfo = data.data;
      await router.push({ path: "/me" });
    }
  } catch (err: any) {
    if (err.response.status === 406 || 401) {
      errorTitle.value = err.response.data;
      errorFlag.value = true;
    } else {
      console.log(err);
    }
  }
}

const registerUser = async () => {
  try {
    const data = await AuthService.register(registerUsername.value, registerPassword.value);
    if (data.status === 200) {
      userStore.userInfo = data.data;
      await router.push({ path: "/me" });
    }
  } catch (err: any) {
    if (err.response.status === 406) {
      errorTitle.value = err.response.data;
      errorFlag.value = true;
    } else {
      console.log(err);
    }
  }
}
</script>

<template>
  <div class="min-h-screen bg-no-repeat bg-bottom bg-[url('/wave.svg')]"></div>
  <div class="fixed top-0 left-0 flex items-center gap-2 px-3 py-1">
    <img src="/JobSpark.png" alt="icon" class="h-22" />
  </div>
  <div v-if="loginWindowFlag" class="h-1/2 w-1/3 bg-white fixed left-1/2 -translate-x-1/2 top-52 rounded-2xl p-10 flex flex-col items-center justify-center shadow-2xl max-xl:w-2/4 max-md:w-3/4 max-sm:w-full">
    <svg width="50px" height="50px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="mb-2 min-h-12">
      <circle cx="12" cy="9" r="3" stroke="#00a6f4" stroke-width="1.5"/>
      <circle cx="12" cy="12" r="10" stroke="#00a6f4" stroke-width="1.5"/>
      <path d="M17.9691 20C17.81 17.1085 16.9247 15 11.9999 15C7.07521 15 6.18991 17.1085 6.03076 20" stroke="#00a6f4" stroke-width="1.5" stroke-linecap="round"/>
    </svg>
    <b class="text-lg mb-5">Войдите в ваш аккаунт</b>
    <div v-if="errorFlag" class="mb-6 flex items-center gap-2 p-3 rounded-lg border-solid border-red-400 border-2 bg-red-100">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#991b1b" class="size-6">
        <path stroke-linecap="round" stroke-linejoin="round" d="m9.75 9.75 4.5 4.5m0-4.5-4.5 4.5M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
      </svg>
      <p class="text-red-800">{{ errorTitle }}</p>
    </div>
    <div class="relative z-0 w-3/4 mb-5 group">
      <input v-model="loginUsername" type="text" name="floating_first_name" class="w-full block py-2.5 px-0 text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-sky-500 peer" placeholder=" " required />
      <label for="floating_first_name" class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-sky-500 peer-focus:dark:text-sky-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Логин</label>
    </div>
    <div class="relative z-0 w-3/4 mb-8 group">
      <input v-model="loginPassword" type="password" name="floating_password" class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-sky-500 peer" placeholder=" " required />
      <label for="floating_password" class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-sky-500 peer-focus:dark:text-sky-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Пароль</label>
    </div>
    <button @click="loginUser" class="bg-sky-500 hover:bg-sky-400 text-white font-bold py-2 px-4 rounded-full transition-all">
      Вход
    </button>
    <p class="mt-3">Нет аккаунта? <button @click="loginWindowFlag = !loginWindowFlag" class="text-sky-500 hover:text-sky-300 transition">Зарегистрируйся</button></p>
  </div>
  <div v-if="!loginWindowFlag" class="h-1/2 w-1/3 bg-white fixed left-1/2 -translate-x-1/2 top-52 rounded-2xl p-10 flex flex-col items-center justify-center shadow-2xl max-xl:w-2/4 max-md:w-3/4 max-sm:w-full">
    <svg width="50px" height="50px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="mb-2 min-h-12">
      <circle cx="12" cy="9" r="3" stroke="#00a6f4" stroke-width="1.5"/>
      <circle cx="12" cy="12" r="10" stroke="#00a6f4" stroke-width="1.5"/>
      <path d="M17.9691 20C17.81 17.1085 16.9247 15 11.9999 15C7.07521 15 6.18991 17.1085 6.03076 20" stroke="#00a6f4" stroke-width="1.5" stroke-linecap="round"/>
    </svg>
    <b class="text-lg mb-5">Регистрация Нового Аккаунта</b>
    <div v-if="errorFlag" class="mb-6 flex items-center gap-2 p-3 rounded-lg border-solid border-red-400 border-2 bg-red-100">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#991b1b" class="size-6">
        <path stroke-linecap="round" stroke-linejoin="round" d="m9.75 9.75 4.5 4.5m0-4.5-4.5 4.5M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
      </svg>
      <p class="text-red-800">{{ errorTitle }}</p>
    </div>
    <div class="relative z-0 w-3/4 mb-5 group">
      <input v-model="registerUsername" type="text" name="floating_first_name" class="w-full block py-2.5 px-0 text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-sky-500 peer" placeholder=" " required />
      <label for="floating_first_name" class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-sky-500 peer-focus:dark:text-sky-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Логин</label>
    </div>
    <div class="relative z-0 w-3/4 mb-8 group">
      <input v-model="registerPassword" type="password" name="floating_password" class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-sky-500 peer" placeholder=" " required />
      <label for="floating_password" class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-sky-500 peer-focus:dark:text-sky-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Пароль</label>
    </div>
    <button @click="registerUser" class="bg-sky-500 hover:bg-sky-400 text-white font-bold py-2 px-4 rounded-full transition-all">
      Регистрация
    </button>
    <p class="mt-3">Есть аккаунт? <button @click="loginWindowFlag = !loginWindowFlag" class="text-sky-500 hover:text-sky-300 transition">Войти</button></p>
  </div>
</template>