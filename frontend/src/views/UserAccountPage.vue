<script setup lang="ts">
import type { UserResumeResponse } from '@/models/ResumeModels.ts'
import type { UserEmployersModel } from '@/models/EmployersModels.ts'
import { useUserStore } from '@/stores/user.ts'
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import AuthService from '@/services/AuthService.ts'
import CreateResumeDrawer from '@/components/Drawers/CreateResumeDrawer.vue'
import CreateEmployerDrawer from '@/components/Drawers/CreateEmployerDrawer.vue'
import UpdateResumeDrawer from '@/components/Drawers/UpdateResumeDrawer.vue'
import UpdateEmployerDrawer from '@/components/Drawers/UpdateEmployerDrawer.vue'
import UserEmployerCart from '@/components/UserEmployerCart.vue'
import UserResumeCart from '@/components/UserResumeCart.vue'

const userStore = useUserStore()

const updateResumeDrawer = ref<boolean>(false);

const updateResumeDrawerClose = () => {updateResumeDrawer.value = false};

const updateEmployerDrawer = ref<boolean>(false);

const updateEmployerDrawerClose = () => {updateEmployerDrawer.value = false};

const username = ref<string>("");

const userResume = ref<UserResumeResponse | null>(null);

const defaultResume = {
  "city": "Не указано",
  "description": "",
  "education": "",
  "educational_institution": "",
  "email": "",
  "expected_salary": 0,
  "experience": 0,
  "faculty": "",
  "id": 0,
  "job_name": "",
  "name": "",
  "phone_number": "",
  "surname": "",
  "telegram_username": ""
};

const getUserResume = () => {return userResume.value ? userResume.value : defaultResume};

const userEmployer = ref<UserEmployersModel | null>(null);

const defaultEmployer = {
  "city": "Не указано",
  "description": "",
  "email": "",
  "id": 0,
  "name": "",
  "phone_number": "",
  "remotely": false,
  "salary": 0,
  "telegram_username": "",
  "work_experience": 0
};

const getUserEmployer = () => {return userEmployer.value ? userEmployer.value : defaultEmployer};

const router = useRouter();

const createResumeDrawer = ref<boolean>(false);

const closeResumeDrawer = () => {
  createResumeDrawer.value = false;
}

const createEmployerDrawer = ref<boolean>(false);

const closeEmployerDrawer = () => {
  createEmployerDrawer.value = false;
}

const logout = async () => {
  await AuthService.logout();
  userStore.logout();
  await router.push('/');
}

const updateUserInfo = async () => {
  try {
    const data = await AuthService.isAuthenticated();
    if (data.data.auth) {
      userStore.userInfo = data.data.user;
      userResume.value = userStore.getUserResume();
      userEmployer.value = userStore.getUserEmployer();
    }
  } catch (err) {
    console.log(err)
  }
}

onMounted(() => {
  console.log(userStore.userInfo)
  username.value = userStore.getUsername();
  userResume.value = userStore.getUserResume();
  userEmployer.value = userStore.getUserEmployer();
})

</script>

<template>
  <UpdateResumeDrawer v-if="updateResumeDrawer" :resume-info="getUserResume()" :close-drawer="updateResumeDrawerClose" :update-user-info="updateUserInfo" />
  <UpdateEmployerDrawer v-if="updateEmployerDrawer" :employer-info="getUserEmployer()" :close-drawer="updateEmployerDrawerClose" :update-user-info="updateUserInfo" />
  <CreateResumeDrawer v-if="createResumeDrawer" :update-user-info="updateUserInfo" :close-drawer="closeResumeDrawer" />
  <CreateEmployerDrawer v-if="createEmployerDrawer" :update-user-info="updateUserInfo" :close-drawer="closeEmployerDrawer" />
  <div class="bg-white w-3/5 max-lg:w-4/5 max-md:w-8/9 max-sm:w-full m-auto rounded-xl shadow-[0_0_25px_rgb(255,255,255)] shadow-sky-500 mt-20">
    <header class="flex justify-between border-b border-slate-200 px-10 py-8">
      <div class="flex items-center gap-2">
        <img src="/user.svg" alt="user" class="h-8">
        <h2 class="font-bold text-xl">{{ username }}</h2>
      </div>
      <ul class="flex max-sm:flex-col max-sm:gap-3 items-center gap-10">
        <li @click="router.push({ path: '/' })" class="flex items-center gap-3 cursor-pointer hover:-translate-y-1 transition duration-200">
          <span>На главную</span>
        </li>
        <li @click="logout" class="flex items-center gap-1 cursor-pointer hover:-translate-y-1 transition duration-200">
          <span>Выйти</span>
          <img src="/logout.svg" alt="logout" class="h-5">
        </li>
      </ul>
    </header>
    <div class="max-md:p-5 p-10">
      <div class="flex flex-col items-start mb-10">
        <div class="flex items-center gap-2 mb-3">
          <h1 class="text-3xl font-bold">Резюме:</h1>
          <div @click="updateResumeDrawer = true" class="flex items-center justify-center p-1 rounded-lg border-2 border-slate-300 hover:bg-slate-100">
            <img src="/edit.svg" alt="edit" class="h-5">
          </div>
        </div>
        <UserResumeCart v-if="userResume" :user-resume="userResume" />
        <button v-if="!userResume" @click="createResumeDrawer = true" class="min-w-36 max-sm:min-w-12 bg-sky-500 hover:bg-sky-400 text-white font-bold py-2 px-4 rounded-xl transition-all">
          Создать резюме
        </button>
      </div>
      <div class="flex flex-col items-start mb-10">
        <div class="flex items-center gap-2 mb-3">
          <h1 class="text-3xl font-bold">Вакансия:</h1>
          <div @click="updateEmployerDrawer = true" class="flex items-center justify-center p-1 rounded-lg border-2 border-slate-300 hover:bg-slate-100">
            <img src="/edit.svg" alt="edit" class="h-5">
          </div>
        </div>
        <UserEmployerCart v-if="userEmployer" :user-employer="userEmployer" />
        <button v-if="!userEmployer" @click="createEmployerDrawer = true" class="min-w-36 max-sm:min-w-12 bg-sky-500 hover:bg-sky-400 text-white font-bold py-2 px-4 rounded-xl transition-all">
          Создать вакансию
        </button>
      </div>
    </div>
  </div>
</template>