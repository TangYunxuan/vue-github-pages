<template>
  <div :class="['p-6 rounded-3xl text-white', bgColor]">
    <component :is="iconComponent" class="w-10 h-10 mb-4" />
    <h3 class="text-3xl font-bold">{{ count }}</h3>
    <p class="text-white/80">{{ label }}</p>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import * as icons from 'lucide-vue-next'; // 用于动态加载图标

const props = defineProps({
  icon: String,       // 比如 "Folder"
  count: Number,      // 数值
  label: String,      // 显示标签
  color: String       // 比如 "indigo", "emerald", "rose"
});

const iconComponent = computed(() => icons[props.icon] || icons["Circle"]);
const bgColor = computed(() => `bg-${props.color}-500`);
</script>