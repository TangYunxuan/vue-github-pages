<script setup>
import { ref, onMounted } from 'vue'
// import { useRoute, useRouter } from 'vue-router'
import { Heart, MessageCircle, LogIn, X } from 'lucide-vue-next'

import PhotoCard from '@/components/cute/PhotoCard.vue'
import CommentSection from '@/components/cute/CommentSection.vue'

import { User } from '@/api/User'
import { CatPhoto } from '@/api/CatPhoto'
import { Comment } from '@/api/Comment'

const photos = ref([])
const comments = ref([])
const selectedPhoto = ref(null)
const isLoading = ref(true)
const user = ref(null)

onMounted(async () => { //页面加载完成。。。
  try {
    const currentUser = await User.me() //调用user.me()，判断当前用户是谁
    user.value = currentUser
  } catch {
    user.value = null
  } finally {
    await loadPhotos() //然后加载照片列表和评论列表
    await loadComments()
  }
})

// 封装的函数
// 加载照片列表
const loadPhotos = async () => { //定义了一个异步函数 loadPhotos，用于加载猫猫照片。
  const data = await CatPhoto.list('-created_date')
  //调用 CatPhoto 模块中的 list 方法，获取照片列表。
  //这个 -created_date 表示按创建时间降序排序（新 → 旧）。
  photos.value = data
  //把获取到的数据赋值给响应式变量 photos。
  // 注意 Vue 的响应式变量（通过 ref() 创建的）要通过 .value 获取和设置值。
  isLoading.value = false
  //设置加载状态为“已完成”。
}
// 加载评论列表
const loadComments = async () => {
  const data = await Comment.list('-created_date')
  comments.value = data
}
//点赞处理逻辑
const handleLike = async (photo) => {//接收一个照片对象 photo，处理它的点赞事件。
  await CatPhoto.update(photo.id, {// 是向服务器发送 PUT 请求，更新该照片数据
    ...photo,//...photo 表示保留原有信息
    likes: (photo.likes || 0) + 1
    //表示将 likes 字段加 1（如果原本没有点赞数则为 0）
  })
  await loadPhotos()
  //点赞后重新加载照片列表（刷新页面状态）
}
// 发表评论逻辑
const handleComment = async (photoId, commentData) => { 
  await Comment.create({ ...commentData, photo_id: photoId })//调用 Comment.create(...) 创建新评论
  await loadComments()//成功后刷新评论列表
}
//获取某张照片的评论
const getCommentsForPhoto = (photoId) =>
  comments.value.filter((c) => c.photo_id === photoId)
  //接收一张照片的 photoId
  //返回 comments.value 中所有 photo_id 匹配的评论



//控制展示哪些照片
const displayedPhotos = computed(() => //这是一个计算属性 computed()，它的值会根据 user 和 photos 的变化自动更新。
  user.value?.role === 'admin' ? photos.value : photos.value.slice(0, 3)
  //如果当前用户是管理员（user.value?.role === 'admin'）
    //显示全部照片
    //否则（普通游客）
    //只展示前 3 张照片
)
</script>


<!--页面结构-->
<template>
  <div class="min-h-screen px-6 py-12">
    <div class="max-w-7xl mx-auto">
      <!-- Header -->
      <div
        class="text-center mb-16"
        v-motion="{
          initial: { opacity: 0, y: 30 },
          enter: { opacity: 1, y: 0, transition: { duration: 0.8 } }
        }"
      >
        <h1 class="text-5xl md:text-6xl font-bold text-stone-800 mb-6">
          Meet My
          <span
            class="block bg-gradient-to-r from-pink-500 to-rose-500 bg-clip-text text-transparent"
          >
            Adorable Cat
          </span>
        </h1>
        <p class="text-xl text-stone-600 max-w-2xl mx-auto mb-8">
          Welcome to my cat's photo gallery! Each photo captures a special
          moment of cuteness. Feel free to like and comment on your favorites.
        </p>
      </div>

      <!-- Loading Skeleton -->
      <div v-if="isLoading" class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div
          v-for="i in 3"
          :key="i"
          class="bg-white/50 rounded-3xl p-4 animate-pulse"
        >
          <div class="aspect-square bg-stone-200 rounded-2xl mb-4"></div>
          <div class="space-y-2">
            <div class="h-4 bg-stone-200 rounded w-3/4"></div>
            <div class="h-3 bg-stone-200 rounded w-1/2"></div>
          </div>
        </div>
      </div>

      <!-- Photo Gallery -->
      <div
        v-else
        v-motion="{
          initial: { opacity: 0 },
          enter: { opacity: 1, transition: { duration: 0.6, delay: 0.3 } }
        }"
        class="grid md:grid-cols-2 lg:grid-cols-3 gap-8"
      >
        <PhotoCard
          v-for="photo in displayedPhotos"
          :key="photo.id"
          :photo="photo"
          :comments="getCommentsForPhoto(photo.id)"
          :onLike="() => handleLike(photo)"
          :onViewDetails="() => (selectedPhoto = photo)"
        />
      </div>

      <!-- Empty state (for admin only) -->
      <!-- <div
        v-if="photos.length === 0 && !isLoading && user?.role === 'admin'"
        v-motion="{ initial: { opacity: 0, y: 30 }, enter: { opacity: 1, y: 0 } }"
        class="text-center py-16"
      >
        <div
          class="w-32 h-32 mx-auto mb-6 bg-gradient-to-r from-pink-500 to-rose-500 rounded-full flex items-center justify-center"
        >
          <Heart class="w-16 h-16 text-white" />
        </div>
        <h3 class="text-2xl font-semibold text-stone-800 mb-4">No Photos Yet</h3>
        <p class="text-stone-600">But they’ll be here soon 💖</p>
      </div> -->

      <!-- Login Prompt -->
      <!-- <div
        v-if="!user && photos.length > 3"
        v-motion="{ initial: { opacity: 0, y: 30 }, enter: { opacity: 1, y: 0 } }"
        class="text-center py-16 bg-stone-50 rounded-3xl mt-16"
      >
        <div
          class="w-24 h-24 mx-auto mb-6 bg-gradient-to-r from-amber-500 to-orange-500 rounded-full flex items-center justify-center"
        >
          <LogIn class="w-12 h-12 text-white" />
        </div>
        <h3 class="text-2xl font-semibold text-stone-800 mb-4">Want to see more?</h3>
        <p class="text-stone-600 mb-8">
          Log in as admin to view all photos and manage content.
        </p>
        <button
          @click="User.login()"
          class="bg-gradient-to-r from-amber-500 to-orange-500 text-white px-8 py-3 rounded-full font-semibold"
        >
          Admin Login
        </button>
      </div> -->

      <!-- Photo Detail Modal -->
      <Teleport to="body">
        <transition name="fade">
          <div
            v-if="selectedPhoto"
            class="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 flex items-center justify-center p-4"
            @click="selectedPhoto = null"
          >
            <transition name="scale-fade">
              <div
                class="bg-white rounded-3xl p-6 max-w-4xl w-full max-h-[90vh] overflow-y-auto"
                @click.stop
              >
                <div class="flex justify-between items-start mb-6">
                  <h3 class="text-2xl font-bold text-stone-800">
                    {{ selectedPhoto.caption }}
                  </h3>
                  <button @click="selectedPhoto = null">
                    <X class="w-6 h-6 text-stone-500" />
                  </button>
                </div>

                <div class="grid lg:grid-cols-2 gap-8">
                  <div>
                    <img
                      :src="selectedPhoto.image_url"
                      :alt="selectedPhoto.caption"
                      class="w-full aspect-square object-cover rounded-2xl"
                    />
                    <div
                      class="flex items-center justify-between mt-4 p-4 bg-stone-50 rounded-xl"
                    >
                      <button
                        @click="handleLike(selectedPhoto)"
                        class="flex items-center space-x-2 text-pink-600 hover:text-pink-700"
                      >
                        <Heart class="w-5 h-5" />
                        <span>{{ selectedPhoto.likes || 0 }} Likes</span>
                      </button>
                      <span class="text-stone-500">
                        <MessageCircle class="w-5 h-5 inline mr-1" />
                        {{ getCommentsForPhoto(selectedPhoto.id).length }} Comments
                      </span>
                    </div>
                  </div>

                  <CommentSection
                    :photoId="selectedPhoto.id"
                    :comments="getCommentsForPhoto(selectedPhoto.id)"
                    :onComment="(data) => handleComment(selectedPhoto.id, data)"
                  />
                </div>
              </div>
            </transition>
          </div>
        </transition>
      </Teleport>
    </div>
  </div>
</template>