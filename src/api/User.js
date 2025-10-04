export const User = {
  async me() {
    // 模拟获取当前用户（可替换为真实 API）
    return {
      id: 1,
      name: 'Admin',
      role: 'admin', // 或 'guest'
    }
  },
  login() {
    // 模拟登录
    alert('Login function triggered!')
  }
}