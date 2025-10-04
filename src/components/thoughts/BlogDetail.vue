<template>
  <transition name="fade">
    <div
      v-if="post"
      class="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex items-center justify-center p-4"
      @click.self="onClose"
    >
      <transition name="scale-fade">
        <div
          class="bg-white rounded-3xl max-w-4xl w-full max-h-[90vh] overflow-hidden"
          @click.stop
        >
          <!-- Header -->
          <div class="relative">
            <div v-if="post.featured_image" class="aspect-[3/1] overflow-hidden">
              <img
                :src="post.featured_image"
                :alt="post.title"
                class="w-full h-full object-cover"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/50 via-transparent to-transparent" />
            </div>

            <button
              @click="onClose"
              class="absolute top-4 right-4 bg-white/90 backdrop-blur hover:bg-white p-2 rounded-full"
            >
              <XIcon class="w-6 h-6" />
            </button>

            <div
              class="p-8"
              :class="post.featured_image ? 'absolute bottom-0 left-0 right-0 text-white' : ''"
            >
              <h1
                class="text-4xl md:text-5xl font-bold mb-4 leading-tight"
                :class="post.featured_image ? 'drop-shadow-lg' : 'text-stone-800'"
              >
                {{ post.title }}
              </h1>

              <div class="flex flex-wrap items-center gap-4 text-sm">
                <div
                  class="flex items-center space-x-2"
                  :class="post.featured_image ? 'text-white/90' : 'text-stone-500'"
                >
                  <CalendarIcon class="w-4 h-4" />
                  <span>{{ formattedDate }}</span>
                </div>

                <div
                  class="flex items-center space-x-2"
                  :class="post.featured_image ? 'text-white/90' : 'text-stone-500'"
                >
                  <ClockIcon class="w-4 h-4" />
                  <span>{{ estimatedReadTime }} min read</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Content -->
          <div class="p-8 overflow-y-auto max-h-[60vh]">
            <div v-if="post.tags?.length" class="flex flex-wrap gap-2 mb-8">
              <span
                v-for="tag in post.tags"
                :key="tag"
                class="bg-purple-100 text-purple-700 border border-purple-200 rounded px-2 py-1 text-sm inline-flex items-center"
              >
                <TagIcon class="w-3 h-3 mr-1" /> {{ tag }}
              </span>
            </div>

            <div class="text-xl text-stone-600 mb-8 font-light leading-relaxed border-l-4 border-purple-200 pl-6 italic">
              {{ post.excerpt }}
            </div>

            <div class="prose prose-lg prose-stone max-w-none">
                <Markdown :source="post.content" />
            </div>
          </div>
        </div>
      </transition>
    </div>
  </transition>
</template>

<script setup>
import { computed } from 'vue'
import { format } from 'date-fns'
import { Calendar as CalendarIcon, Clock as ClockIcon, Tag as TagIcon, X as XIcon } from 'lucide-vue-next'
import VueMarkdown from 'vue-markdown-render'

const props = defineProps({
  post: Object,
  onClose: Function,
})

const estimatedReadTime = computed(() => {
  return Math.ceil(props.post?.content.split(' ').length / 200)
})

const formattedDate = computed(() => {
  return format(new Date(props.post?.created_date), 'MMMM d, yyyy')
})
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.scale-fade-enter-active,
.scale-fade-leave-active {
  transition: all 0.3s ease;
}
.scale-fade-enter-from,
.scale-fade-leave-to {
  opacity: 0;
  transform: scale(0.9);
}
</style>