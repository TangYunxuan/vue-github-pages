<script setup>
import { computed } from 'vue'
import { Motion } from '@vueuse/motion'
import { MapPin, Calendar, Camera } from 'lucide-vue-next'
import { format } from 'date-fns'

defineProps({
  trip: Object,
  onClick: Function
})

const formatDateRange = computed(() => {
  const start = format(new Date(trip.start_date), 'MMM d')
  const end = trip.end_date
    ? format(new Date(trip.end_date), 'MMM d, yyyy')
    : 'Present'
  return `${start} - ${end}`
})
</script>

<template>
  <Motion
    :initial="{ opacity: 0, y: 50 }"
    :enter="{ opacity: 1, y: 0 }"
    :hover="{ scale: 1.02, y: -5 }"
    class="group cursor-pointer"
    @click="onClick"
  >
    <div class="bg-white/80 backdrop-blur-sm rounded-3xl p-6 shadow-lg hover:shadow-2xl transition-all duration-300 border border-white/20 h-full flex flex-col">
      <!-- 封面图 -->
      <div
        v-if="trip.photos?.length"
        class="aspect-video overflow-hidden rounded-2xl mb-6 relative"
      >
        <img
          :src="trip.photos[0]"
          :alt="trip.location"
          class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
        />
        <div class="absolute inset-0 bg-gradient-to-t from-black/30 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
        <div
          v-if="trip.photos.length > 1"
          class="absolute top-4 right-4 bg-black/50 backdrop-blur text-white px-3 py-1 rounded-full text-sm flex items-center gap-1"
        >
          <Camera class="w-3 h-3" />
          {{ trip.photos.length }}
        </div>
      </div>

      <!-- 文本内容 -->
      <div class="flex-1 space-y-4">
        <div class="space-y-2">
          <div class="flex items-start justify-between">
            <h3 class="text-xl font-bold text-stone-800 group-hover:text-green-600 transition-colors leading-tight">
              {{ trip.location }}
            </h3>
            <div class="flex items-center text-green-600">
              <MapPin class="w-4 h-4" />
            </div>
          </div>

          <p class="text-stone-500 font-medium">{{ trip.country }}</p>

          <p class="text-stone-600 line-clamp-3 leading-relaxed">
            {{ trip.description }}
          </p>
        </div>

        <!-- 高光内容 -->
        <div v-if="trip.highlights?.length" class="space-y-2">
          <h4 class="text-sm font-semibold text-stone-700">Highlights:</h4>
          <ul class="text-sm text-stone-600 space-y-1">
            <li
              v-for="(highlight, index) in trip.highlights.slice(0, 3)"
              :key="index"
              class="flex items-start"
            >
              <span class="w-1.5 h-1.5 bg-green-500 rounded-full mt-2 mr-2 flex-shrink-0"></span>
              {{ highlight }}
            </li>
            <li
              v-if="trip.highlights.length > 3"
              class="text-green-600 font-medium"
            >
              +{{ trip.highlights.length - 3 }} more highlights
            </li>
          </ul>
        </div>

        <!-- 日期 -->
        <div class="flex items-center text-sm text-stone-500 pt-4 border-t border-stone-200">
          <Calendar class="w-4 h-4 mr-2" />
          <span>{{ formatDateRange }}</span>
        </div>
      </div>
    </div>
  </Motion>
</template>