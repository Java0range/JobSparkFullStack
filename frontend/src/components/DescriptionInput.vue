<template>
  <div class="mb-6">
    <label
      for="resumeDescription"
      class="block text-gray-700 text-sm font-bold mb-2"
    >
      Краткое описание {{ desc_type == "resume" ? "резюме" : "вакансии" }}
    </label>
    <textarea
      name="resumeDescription"
      :value="modelValue"
      @input="emit('update:modelValue', ($event.target as HTMLTextAreaElement).value)"
      :placeholder="desc_type == 'resume' ? placeholder_resume : placeholder_employer"
      rows="8"
      class="
        shadow-sm
        appearance-none
        border
        rounded
        w-full
        py-2
        px-3
        text-gray-700
        leading-tight
        focus:outline-none
        focus:shadow-outline
        focus:border-blue-500
        transition
        duration-200
        ease-in-out
        resize-none
        placeholder-gray-400
      "
    />
    <p class="text-gray-600 text-xs italic mt-1">
      {{ desc_type == "resume" ? p_text_resume : p_text_employer }}
    </p>
  </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits } from 'vue';

defineProps({
  modelValue: {
    type: String,
    required: true,
  },
  desc_type: String
});

const p_text_resume = "(Опишите свои ключевые навыки, опыт и карьерные цели. До 250 символов.)"
const p_text_employer = "(Опишите свои ключевые моменты по вашей вакансии. До 250 символов.)"

const placeholder_resume = "Напишите краткое описание своей профессиональной деятельности, навыков и целей. Это поможет работодателю быстро оценить ваш профиль."
const placeholder_employer = "Напишите краткое описание своей вакансии, требования, условия, чем предстоит заниматся."

const emit = defineEmits(['update:modelValue']);
</script>