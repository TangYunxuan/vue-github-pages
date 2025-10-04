<template>
  <section class="intro">
    <img 
      class="avatar" 
      :src="avatarUrl" 
      alt="Yunxuan's Avatar"
      loading=" lazy" />
    <h1>汤昀暄</h1>
    <p class="slogan">喜欢你来造访昀暄的小宇宙💫<br />飞船和偏见停外面哦～</p>
  </section>
</template>

<script setup>
const avatarUrl = "https://cdn.jsdelivr.net/gh/TangYunxuan/tangyunxuan-assets@main/images/avatar.webp"
</script>

<style scoped>
/* ✨ 设置默认字体大小：桌面优先 */
html {
  font-size: 18px;
}

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
  font-size: 1.2rem;
  color: #444;
  line-height: 1.6;
}

/* ✨ 手机端适配：小屏幕设备调整排版 */
@media (max-width: 430px) {
  html {
    font-size: 20px; 
  }

  .avatar {
    width: 130px;
    height: 130px;
  }

  h1 {
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
  }

  .slogan {
    font-size: 1rem;
    padding: 0 1rem;
  }
}
</style>