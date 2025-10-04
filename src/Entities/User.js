export default {
  async me() {
    // 假设你以后会和真实后端 API 打通
    // 暂时返回一个假的 admin 用户
    return {
      id: 1,
      name: 'Admin User',
      role: 'admin',  // 用于控制权限判断
    };
  },
};