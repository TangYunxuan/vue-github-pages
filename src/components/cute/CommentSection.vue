<script setup>
import { ref } from 'vue'
import { Motion } from '@vueuse/motion'
import { Send, MessageCircle } from 'lucide-vue-next'
import { format } from 'date-fns'

// 接收 props
defineProps({
  photoId: [String, Number],
  comments: Array,
  onComment: Function
})

// 新评论内容（响应式）
const newComment = ref({
  author_name: '',
  content: ''
})

// 提交处理函数
const handleSubmit = (e) => {
  e.preventDefault()
  if (!newComment.value.author_name.trim() || !newComment.value.content.trim()) return

  // 回调
  onComment(newComment.value)
  newComment.value = { author_name: '', content: '' }
}
</script>

<template>
  <div class="space-y-6">
    <h4 class="text-xl font-semibold text-stone-800 flex items-center gap-2">
      <MessageCircle class="w-5 h-5" />
      Comments ({{ comments.length }})
    </h4>

    <!-- 💬 评论表单 -->
    <form @submit="handleSubmit" class="space-y-4">
      <input
        type="text"
        placeholder="Your name"
        v-model="newComment.author_name"
        class="rounded-xl border border-stone-200 focus:border-pink-400 px-3 py-2 w-full"
      />
      <textarea
        placeholder="Write a comment..."
        v-model="newComment.content"
        class="rounded-xl border border-stone-200 focus:border-pink-400 px-3 py-2 min-h-[5rem] w-full"
      />
      <button
        type="submit"
        :disabled="!newComment.author_name.trim() || !newComment.content.trim()"
        class="w-full bg-gradient-to-r from-pink-500 to-rose-500 hover:from-pink-600 hover:to-rose-600 text-white rounded-xl font-semibold px-4 py-2 flex items-center justify-center gap-2 disabled:opacity-50"
      >
        <Send class="w-4 h-4" />
        Post Comment
      </button>
    </form>

    <!-- 📝 评论列表 -->
    <div class="space-y-4 max-h-60 overflow-y-auto">
      <p
        v-if="comments.length === 0"
        class="text-center text-stone-500 py-8"
      >
        No comments yet. Be the first to comment!
      </p>

      <Motion
        v-for="comment in comments"
        :key="comment.id"
        :initial="{ opacity: 0, y: 20 }"
        :enter="{ opacity: 1, y: 0 }"
        class="bg-stone-50 rounded-xl p-4"
      >
        <div class="flex justify-between items-start mb-2">
          <h5 class="font-semibold text-stone-800">{{ comment.author_name }}</h5>
          <span class="text-xs text-stone-500">
            {{ format(new Date(comment.created_date), 'MMM d, HH:mm') }}
          </span>
        </div>
        <p class="text-stone-600">{{ comment.content }}</p>
      </Motion>
    </div>
  </div>
</template>