// 从 Vite 中导入 defineConfig 方法，用于创建配置对象，带类型提示
import { defineConfig } from 'vite'

// 引入 Vue 插件，让 Vite 能识别并处理 .vue 文件
import vue from '@vitejs/plugin-vue'

// Node.js 内置的 path 模块，用于处理文件路径（跨平台友好）
import path from 'path'

/**
 * 导出默认配置（Vite 会读取这个配置来启动项目）
 */
export default defineConfig({
  // 使用的插件列表（这里只有 vue）
  plugins: [vue()],

  // 解析器相关配置
  resolve: {
    alias: {
      // 给路径设置别名：@代表 ./src 文件夹
      // 以后你就可以用 @/views/Home.vue 代替 ../../views/Home.vue 这种复杂路径
      '@': path.resolve(__dirname, './src'),
    },
  },
})