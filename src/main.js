// src/main.js ✅
import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import { MotionPlugin } from '@vueuse/motion'

createApp(App)
  .use(router)         // 第一个插件：vue-router
  .use(MotionPlugin)   // 第二个插件：motion 动效
  .mount('#app')       // 最后挂载