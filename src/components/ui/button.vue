<script setup>
const props = defineProps({
  variant: { type: String, default: 'primary' },  // 'primary' | 'secondary' | 'ghost' | 'danger'
  size:    { type: String, default: 'md' },       // 'sm' | 'md' | 'lg'
  block:   { type: Boolean, default: false },
  disabled:{ type: Boolean, default: false },
  loading: { type: Boolean, default: false },
  as:      { type: String,  default: 'button' },  // 'button' | 'a'
  href:    { type: String,  default: undefined }
})

const base =
  'inline-flex items-center justify-center gap-2 rounded-xl font-medium transition ' +
  'focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed'

const variants = {
  primary:  'bg-amber-600 text-white hover:bg-amber-700 focus:ring-amber-600',
  secondary:'border border-stone-300 bg-white text-stone-800 hover:bg-stone-50 focus:ring-stone-400',
  ghost:    'bg-transparent text-stone-700 hover:bg-stone-100 focus:ring-stone-300',
  danger:   'bg-red-600 text-white hover:bg-red-700 focus:ring-red-600'
}

const sizes = {
  sm: 'text-sm px-3 py-1.5',
  md: 'text-sm px-4 py-2',
  lg: 'text-base px-5 py-2.5'
}

function classes () {
  return [
    base,
    variants[props.variant] || variants.primary,
    sizes[props.size] || sizes.md,
    props.block ? 'w-full' : ''
  ].join(' ')
}
</script>

<template>
  <component
    :is="as"
    :href="as === 'a' ? href : undefined"
    :disabled="as === 'button' ? (disabled || loading) : undefined"
    :class="classes()"
  >
    <slot name="icon-left" />
    <span v-if="!loading"><slot /></span>
    <span v-else class="inline-flex items-center gap-2">
      <svg class="h-4 w-4 animate-spin" viewBox="0 0 24 24" fill="none" aria-hidden="true">
        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"/>
        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"/>
      </svg>
      Loading…
    </span>
    <slot name="icon-right" />
  </component>
</template>