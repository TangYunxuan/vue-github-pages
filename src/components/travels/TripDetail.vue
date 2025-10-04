<script setup>
import { Motion } from '@vueuse/motion'
import { X, MapPin, Calendar, Camera, Star } from 'lucide-vue-next'
import { format } from 'date-fns'

defineProps({
  trip: Object,
  onClose: Function
})

const formatDateRange = () => {
  const start = format(new Date(trip.start_date), 'MMMM d, yyyy')
  const end = trip.end_date
    ? format(new Date(trip.end_date), 'MMMM d, yyyy')
    : 'Present'
  return trip.end_date ? `${start} - ${end}` : `Since ${start}`
}
</script>

<template>
  <!-- Modal Overlay -->
  <Motion
    :initial="{ opacity: 0 }"
    :enter="{ opacity: 1 }"
    :leave="{ opacity: 0 }"
    class="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex items-center justify-center p-4"
    @click="onClose"
  >
    <!-- Modal Card -->
    <Motion
      :initial="{ scale: 0.9, opacity: 0 }"
      :enter="{ scale: 1, opacity: 1 }"
      :leave="{ scale: 0.9, opacity: 0 }"
      class="bg-white rounded-3xl max-w-4xl w-full max-h-[90vh] overflow-hidden"
      @click.stop
    >
      <!-- Header -->
      <div class="relative">
        <!-- Header image -->
        <div v-if="trip.photos?.length" class="aspect-[3/1] overflow-hidden">
          <img
            :src="trip.photos[0]"
            :alt="trip.location"
            class="w-full h-full object-cover"
          />
          <div class="absolute inset-0 bg-gradient-to-t from-black/50 via-transparent to-transparent" />
        </div>

        <!-- Close Button -->
        <button
          @click="onClose"
          class="absolute top-4 right-4 bg-white/90 backdrop-blur hover:bg-white p-2 rounded-full"
        >
          <X class="w-6 h-6" />
        </button>

        <!-- Title & Meta -->
        <div
          class="p-8"
          :class="trip.photos?.length ? 'absolute bottom-0 left-0 right-0 text-white' : ''"
        >
          <h1
            class="text-4xl md:text-5xl font-bold mb-4 leading-tight"
            :class="trip.photos?.length ? 'drop-shadow-lg' : 'text-stone-800'"
          >
            {{ trip.location }}
          </h1>

          <div class="flex flex-wrap items-center gap-4 text-sm">
            <div
              class="flex items-center space-x-2"
              :class="trip.photos?.length ? 'text-white/90' : 'text-stone-500'"
            >
              <MapPin class="w-4 h-4" />
              <span>{{ trip.country }}</span>
            </div>

            <div
              class="flex items-center space-x-2"
              :class="trip.photos?.length ? 'text-white/90' : 'text-stone-500'"
            >
              <Calendar class="w-4 h-4" />
              <span>{{ formatDateRange() }}</span>
            </div>

            <div
              v-if="trip.photos?.length"
              class="flex items-center space-x-2"
              :class="trip.photos?.length ? 'text-white/90' : 'text-stone-500'"
            >
              <Camera class="w-4 h-4" />
              <span>{{ trip.photos.length }} photos</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Content -->
      <div class="p-8 overflow-y-auto max-h-[60vh]">
        <!-- Description -->
        <div class="mb-8">
          <p class="text-lg text-stone-600 leading-relaxed">
            {{ trip.description }}
          </p>
        </div>

        <!-- 可以继续添加 highlights / gallery / buttons 等内容 -->
        <!-- ... -->
      </div>
    </Motion>
  </Motion>
</template>