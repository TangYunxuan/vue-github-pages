<script setup>
import { ref } from 'vue'
import { useMotion } from '@vueuse/motion'
import { format } from 'date-fns'
import { Calendar, Heart, MessageCircle } from 'lucide-vue-next'

defineProps({
  photo: Object,
  comments: Array,
  onLike: Function,
  onViewDetails: Function
})
</script>

<template>
  <Motion
    :initial="{ opacity: 0, y: 50 }"
    :enter="{ opacity: 1, y: 0 }"
    :leave="{ opacity: 0, y: -50 }"
    :hover="{ scale: 1.02, y: -5 }"
    class="group cursor-pointer"
    @click="onViewDetails"
  >
    <div class="bg-white/80 backdrop-blur-sm rounded-3xl p-4 shadow-lg hover:shadow-2xl transition-all duration-300 border border-white/20">
      <div class="aspect-square overflow-hidden rounded-2xl mb-4 relative">
        <img
          :src="photo.image_url"
          :alt="photo.caption"
          class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
        />
        <div class="absolute inset-0 bg-gradient-to-t from-black/20 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
      </div>

      <div class="space-y-3">
        <h3 class="font-semibold text-stone-800 line-clamp-2 group-hover:text-pink-600 transition-colors">
          {{ photo.caption }}
        </h3>

        <div class="flex items-center justify-between text-sm text-stone-500">
          <div class="flex items-center space-x-4">
            <button
              class="flex items-center space-x-1 text-pink-600 hover:text-pink-700 transition-colors"
              @click.stop="onLike"
            >
              <Heart class="w-4 h-4" />
              <span>{{ photo.likes || 0 }}</span>
            </button>

            <div class="flex items-center space-x-1">
              <MessageCircle class="w-4 h-4" />
              <span>{{ comments.length }}</span>
            </div>
          </div>

          <div class="flex items-center space-x-1">
            <Calendar class="w-4 h-4" />
            <span>{{ format(new Date(photo.created_date), 'MMM d') }}</span>
          </div>
        </div>
      </div>
    </div>
  </Motion>
</template>