<template>
  <div
    class="group cursor-pointer"
    @click="() => emit('click', post)"
    v-motion
    v-motion-fade-slide
    v-motion-hover="hoverEffect"
  >
    <div
      class="bg-white/80 backdrop-blur-sm rounded-3xl p-6 shadow-lg hover:shadow-2xl transition-all duration-300 border border-white/20 h-full flex flex-col"
    >
      <!-- Featured Image -->
      <div
        v-if="post.featured_image"
        class="aspect-video overflow-hidden rounded-2xl mb-6 relative"
      >
        <img
          :src="post.featured_image"
          :alt="post.title"
          class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
        />
        <div class="absolute inset-0 bg-gradient-to-t from-black/20 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
      </div>

      <!-- Content -->
      <div class="flex-1 space-y-4">
        <div class="space-y-3">
          <h3 class="text-xl font-bold text-stone-800 line-clamp-2 group-hover:text-purple-600 transition-colors leading-tight">
            {{ post.title }}
          </h3>

          <p class="text-stone-600 line-clamp-3 leading-relaxed">
            {{ post.excerpt }}
          </p>
        </div>

        <!-- Tags -->
        <div class="flex flex-wrap gap-2">
          <Badge
            v-for="tag in post.tags?.slice(0, 3)"
            :key="tag"
            variant="secondary"
            class="bg-purple-100 text-purple-700 border-purple-200 hover:bg-purple-200 transition-colors"
          >
            <TagIcon class="w-3 h-3 mr-1" />
            {{ tag }}
          </Badge>
          <Badge v-if="post.tags?.length > 3" variant="outline">
            +{{ post.tags.length - 3 }} more
          </Badge>
        </div>

        <!-- Footer -->
        <div class="flex items-center justify-between text-sm text-stone-500 pt-4 border-t border-stone-200">
          <div class="flex items-center space-x-1">
            <CalendarIcon class="w-4 h-4" />
            <span>{{ formattedDate }}</span>
          </div>

          <div class="flex items-center space-x-1">
            <ClockIcon class="w-4 h-4" />
            <span>{{ estimatedReadTime }} min read</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { format } from 'date-fns'
import { Calendar as CalendarIcon, Tag as TagIcon, Clock as ClockIcon } from 'lucide-vue-next'
import { Badge } from '@/components/ui/badge'
import { useMotion } from '@vueuse/motion'

const props = defineProps({
  post: Object
})
const emit = defineEmits(['click'])

const estimatedReadTime = computed(() =>
  Math.ceil((props.post?.content || '').split(' ').length / 200)
)

const formattedDate = computed(() =>
  format(new Date(props.post?.created_date), 'MMM d, yyyy')
)

// Optional hover animation
const hoverEffect = {
  scale: 1.02,
  y: -5
}
</script>