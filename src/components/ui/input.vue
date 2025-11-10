<script setup>
const props = defineProps({
  modelValue: [String, Number],
  placeholder: String,
  type: { type: String, default: 'text' },
  disabled: { type: Boolean, default: false }
})
const emit = defineEmits(['update:modelValue'])
</script>

<template>
  <input
    :type="type"
    :value="modelValue"
    :placeholder="placeholder"
    :disabled="disabled"
    @input="emit('update:modelValue', $event.target.value)"
    class="block w-full rounded-xl border border-stone-300 bg-white text-stone-800
           placeholder-stone-400 px-4 py-2 transition
           focus:outline-none focus:ring-2 focus:ring-amber-200 focus:border-amber-500
           disabled:opacity-50 disabled:cursor-not-allowed"
  />
</template>