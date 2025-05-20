<script setup lang="ts">
import { ref } from 'vue'
import Header from '@/components/Header.vue'
import HomePageComponent from '@/components/PagesComponents/HomePageComponent.vue'
import ApplicantsPageComponet from '@/components/PagesComponents/ApplicantsPageComponet.vue'
import EmployersPageComponent from '@/components/PagesComponents/EmployersPageComponent.vue'

const selectedPage = ref<string>("Главная");

const homePageSearch = ref<string>("");

const changePageSearch = (search: string) => {
  homePageSearch.value = search;
  selectedPage.value = "Соискателям";
};

const changePage = (page: string) => {
  selectedPage.value = page;
};

</script>
<template>
  <div class="flex justify-center items-center h-full w-full">
    <div class="flex-col items-center justify-center w-3/4 max-lg:w-full mt-5">
      <Header @change-active-list="changePage" :selected-page="selectedPage" />
      <HomePageComponent v-if="selectedPage == 'Главная'" :search-clicked="changePageSearch" />
      <ApplicantsPageComponet v-if="selectedPage == 'Соискателям'" :home-page-search="homePageSearch" />
      <EmployersPageComponent v-if="selectedPage == 'Работодателям'"/>
    </div>
  </div>
</template>