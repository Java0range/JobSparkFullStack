<template>
  <div class="flex flex-col items-center w-full p-3 bg-slate-100 rounded-lg">
    <div class="flex items-center justify-center w-full border-b border-sky-500">
      <h3 class="text-lg mb-1">Описание:</h3>
    </div>
    <div class="flex items-center justify-start w-full mt-3">
      <div class="font-mono whitespace-pre-wrap wrap-break-word">
        <pre v-html="internalDescription"></pre>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'

interface Props {
  description: string;
}

const props = defineProps<Props>();

const internalDescription = ref(props.description || 'Описание отсутствует');

watch(props, () => {
  internalDescription.value = props.description;
  internalDescription.value = internalDescription.value
    .replace(/ /g, '&nbsp;')
    .replace(/\t/g, '&nbsp;&nbsp;&nbsp;&nbsp;')
    .replace(/\n/g, '<br>');
})
</script>