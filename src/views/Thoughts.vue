<script setup>
//引入vue的响应式和生命周期相关的函数
import { ref, computed, onMounted, watch } from 'vue';

//引入BlogPost实体类，用于获取博客文章数据
import { BlogPost } from '@/entities/BlogPost';

//引入页面中的两个子组件：博客卡片和详情弹窗
import BlogCard from '@/components/thoughts/BlogCard.vue';
import BlogDetail from '@/components/thoughts/BlogDetail.vue';

//引入 ui 图标和输入组件
import { Search, Filter } from 'lucide-vue-next';
import  Input  from '@/components/ui/input.vue';
import  Button  from '@/components/ui/button.vue';

//声明响应式变量
const posts = ref([]);//所有已经发布的博客文章
const filteredPosts = ref([]);//搜索和筛选后的博客文章
const selectedPost = ref(null);//当前选中的文章（用于显示详情弹窗）
const searchTerm = ref('');//搜索关键词
const selectedTag = ref('');//当前选中的标签
const isLoading = ref(true);//加载状态

// 页面加载时获取博客文章数据
onMounted(async () => {
  const fetchedPosts = await BlogPost.list('-created_date');
  posts.value = fetchedPosts.filter(post => post.published);
  isLoading.value = false;
});

// 监听搜索关键词和选中标签的变化，动态更新过滤后的文章列表
watch([posts, searchTerm, selectedTag], () => {
  let filtered = posts.value;
  if (searchTerm.value) {
    const term = searchTerm.value.toLowerCase();
    filtered = filtered.filter(post =>
      post.title.toLowerCase().includes(term) ||
      post.excerpt.toLowerCase().includes(term)
    );
  }
  if (selectedTag.value) {
    filtered = filtered.filter(post => post.tags?.includes(selectedTag.value));
  }
  filteredPosts.value = filtered;
});

// 计算所有标签，用于筛选按钮
const allTags = computed(() => {
  const tags = posts.value.flatMap(post => post.tags || []);
  return [...new Set(tags)];
});
</script>

<template>
  <div class="min-h-screen px-6 py-12">
    <div class="max-w-7xl mx-auto">
      <!-- Header -->
      <div class="text-center mb-16">
        <h1 class="text-5xl md:text-6xl font-bold text-stone-800 mb-6">
          My
          <span class="block bg-gradient-to-r from-purple-500 to-indigo-500 bg-clip-text text-transparent">
            Thoughts
          </span>
        </h1>
        <p class="text-xl text-stone-600 max-w-2xl mx-auto mb-8">
          A collection of my personal reflections, insights, and stories.
        </p>
      </div>

      <!-- Search and Filter -->
      <div class="bg-white/80 backdrop-blur-sm rounded-3xl p-6 shadow-lg mb-12 border border-white/20">
        <div class="flex flex-col md:flex-row gap-4 items-center">
          <div class="relative flex-1 w-full">
            <Search class="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-stone-400" />
            <Input
              v-model="searchTerm"
              placeholder="Search thoughts..."
              class="pl-12 rounded-xl border-stone-200 focus:border-purple-400 w-full"
            />
          </div>
          
          <!-- 标签筛选按钮 -->
          <div class="flex items-center gap-2 flex-wrap">
            <Filter class="w-5 h-5 text-stone-500" />
            <Button
              :variant="selectedTag === '' ? 'default' : 'outline'"
              @click="selectedTag = ''"
              class="rounded-full"
            >
              All
            </Button>
            <Button
              v-for="tag in allTags"
              :key="tag"
              :variant="selectedTag === tag ? 'default' : 'outline'"
              @click="selectedTag = tag"
              class="rounded-full"
            >
              {{ tag }}
            </Button>
          </div>
        </div>
      </div>

      <!-- Blog Posts -->
       <!-- 加载状态时展示的骨架屏 -->
      <div v-if="isLoading" class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div v-for="i in 3" :key="i" class="bg-white/50 rounded-3xl p-6 animate-pulse">
          <div class="aspect-video bg-stone-200 rounded-2xl mb-4"></div>
          <div class="space-y-3">
            <div class="h-6 bg-stone-200 rounded w-3/4"></div>
            <div class="h-4 bg-stone-200 rounded w-full"></div>
            <div class="h-4 bg-stone-200 rounded w-2/3"></div>
            <div class="flex gap-2">
              <div class="h-6 bg-stone-200 rounded-full w-16"></div>
              <div class="h-6 bg-stone-200 rounded-full w-20"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- 正常加载完后展示的博客卡片 -->
      <div v-else class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <BlogCard
          v-for="post in filteredPosts"
          :key="post.id"
          :post="post"
          @click="selectedPost = post"
        />
      </div>

      <!-- Blog Detail Modal -->
      <BlogDetail
        v-if="selectedPost"
        :post="selectedPost"
        @close="selectedPost = null"
      />
    </div>
  </div>
</template>

<style scoped>
/* 当前无额外样式定义 */
</style>