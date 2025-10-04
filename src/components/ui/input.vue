<template>
  <input
    :type="type"
    :placeholder="placeholder"
    :value="modelValue"
    @input="$emit('update:modelValue', $event.target.value)"
    class="input"
  />
</template>

<script setup>
defineProps({
  modelValue: String,
  placeholder: {
    type: String,
    default: '',
  },
  type: {
    type: String,
    default: 'text',
  },
})
defineEmits(['update:modelValue'])
</script>

<style scoped>
.input {
  padding: 8px 12px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 14px;
  width: 100%;
  box-sizing: border-box;
  outline: none;
  transition: border-color 0.3s ease;
}

.input:focus {
  border-color: #0077ff;
}
</style>