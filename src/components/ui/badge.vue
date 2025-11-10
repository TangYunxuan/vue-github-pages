<script setup>
const props = defineProps({
  variant: { type: String, default: 'default' }, // default | secondary | success | danger
  size: { type: String, default: 'md' },         // sm | md | lg
  rounded: { type: Boolean, default: true },
})
</script>

<template>
  <span
    :class="[
      'inline-flex items-center font-medium',
      size === 'sm' ? 'text-xs px-2 py-0.5' :
      size === 'lg' ? 'text-sm px-3 py-1.5' : 'text-sm px-2.5 py-1',
      rounded ? 'rounded-full' : 'rounded-md',
      {
        'bg-amber-100 text-amber-800': variant === 'default',
        'bg-stone-100 text-stone-700': variant === 'secondary',
        'bg-green-100 text-green-700': variant === 'success',
        'bg-red-100 text-red-700': variant === 'danger',
      }
    ]"
  >
    <slot />
  </span>
</template>