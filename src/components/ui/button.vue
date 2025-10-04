<template>
  <button class="Button">
    <slot />
  </button>
</template>

<script setup>
// 暂时无逻辑
</script>

<style scoped>
.Button {
  background-color: #0057FF;
  color: white;
  padding: 8px 16px;
  border-radius: 8px;
  font-weight: bold;
}
</style>