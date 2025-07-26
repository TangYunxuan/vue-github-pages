<template>
  <section class="intro">
    <img class="avatar" :src="avatarUrl" alt="Yunxuan's Avatar" />
    <h1>汤昀暄</h1>
    <p class="slogan">喜欢你来造访昀暄的小宇宙💫<br />飞船和偏见停外面哦～</p>
  </section>
</template>

<script setup>
import avatar from '../assets/avatar.jpg' // 你那张经典头像
const avatarUrl = avatar
</script>

<style scoped>
.intro {
  text-align: center;
  padding: 2rem;
}
.avatar {
  width: 160px;
  height: 160px;
  object-fit: cover;
  border-radius: 50%;
  border: 3px solid #eee;
  margin-bottom: 1rem;
}
.slogan {
  font-style: italic;
  color: #555;
  font-size: 1.2rem;
}
</style>