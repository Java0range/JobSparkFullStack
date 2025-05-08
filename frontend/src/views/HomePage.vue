<script setup lang="ts">
import Header from '@/components/Header.vue'
import HomePageComponent from '@/components/PagesComponents/HomePageComponent.vue'
import { ref } from 'vue'
import ApplicantsPageComponet from '@/components/PagesComponents/ApplicantsPageComponet.vue'
import EmployersPageComponent from '@/components/PagesComponents/EmployersPageComponent.vue'

const selectedPage = ref<string>("Главная");

const changePage = (page: string) => {
  selectedPage.value = page;
}

</script>
<template>
  <div class="flex justify-center items-center h-full w-full">
    <div class="flex-col items-center justify-center w-3/4 max-lg:w-full mt-5">
      <Header @change-active-list="changePage"/>
      <HomePageComponent v-if="selectedPage == 'Главная'"/>
      <ApplicantsPageComponet v-if="selectedPage == 'Соискателям'"/>
      <EmployersPageComponent v-if="selectedPage == 'Работодателям'"/>
    </div>
  </div>
</template>