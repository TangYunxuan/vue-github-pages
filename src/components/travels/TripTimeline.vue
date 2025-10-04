<script setup>
import { computed } from 'vue'
import { Motion } from '@vueuse/motion'
import { format, differenceInDays } from 'date-fns'
import {
  MapPin,
  Calendar,
  Camera,
  Clock
} from 'lucide-vue-next'

defineProps({
  trip: Object,
  onTripSelect: Function,
  isLast: Boolean
})

const tripDuration = computed(() => {
  if (!trip.end_date) return null
  return (
    differenceInDays(new Date(trip.end_date), new Date(trip.start_date)) + 1
  )
})

const formatDateRange = () => {
  const start = format(new Date(trip.start_date), 'MMM d, yyyy')
  const end = trip.end_date
    ? format(new Date(trip.end_date), 'MMM d, yyyy')
    : 'Present'
  return trip.end_date ? `${start} - ${end}` : `Since ${start}`
}
</script>

<template>
  <div class="relative flex items-start" :id="`trip-${trip.id}`">
    <!-- Connecting Line -->
    <div
      v-if="!isLast"
      class="absolute top-16 left-6 w-0.5 h-full bg-gradient-to-b from-green-300 via-teal-300 to-cyan-300"
    />

    <!-- Timeline Dot -->
    <div
      class="flex-shrink-0 w-12 h-12 rounded-full bg-gradient-to-r from-green-400 to-teal-500 border-4 border-white shadow-lg flex items-center justify-center z-10 mt-4"
    >
      <MapPin class="w-6 h-6 text-white" />
    </div>

    <!-- Card -->
    <Motion
      :initial="{ opacity: 0, x: -30 }"
      :enter="{ opacity: 1, x: 0 }"
      transition="{ duration: 0.6 }"
      class="ml-8 flex-1 mb-12"
    >
      <div
        class="bg-white/90 backdrop-blur-sm rounded-3xl p-8 shadow-xl hover:shadow-2xl transition-all duration-500 border border-white/30 cursor-pointer group"
        @click="() => onTripSelect(trip)"
      >
        <!-- Header -->
        <div class="mb-6">
          <div class="flex justify-between items-start mb-3">
            <h3 class="text-2xl font-bold text-stone-800 group-hover:text-green-600 transition-colors">
              {{ trip.location }}
            </h3>
            <span
              class="bg-green-100 text-green-700 border border-green-200 text-sm font-medium px-2 py-1 rounded-full"
            >
              {{ trip.country }}
            </span>
          </div>

          <div class="flex flex-wrap items-center gap-4 text-sm text-stone-500 mb-4">
            <div class="flex items-center space-x-1">
              <Calendar class="w-4 h-4" />
              <span>{{ formatDateRange() }}</span>
            </div>

            <div v-if="tripDuration" class="flex items-center space-x-1">
              <Clock class="w-4 h-4" />
              <span>{{ tripDuration }} {{ tripDuration === 1 ? 'day' : 'days' }}</span>
            </div>

            <div v-if="trip.photos?.length" class="flex items-center space-x-1">
              <Camera class="w-4 h-4" />
              <span>{{ trip.photos.length }} photos</span>
            </div>
          </div>
        </div>

        <!-- Gallery -->
        <div v-if="trip.photos?.length" class="mb-6">
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            <div
              v-for="(photo, index) in trip.photos.slice(0, 3)"
              :key="index"
              class="aspect-video overflow-hidden rounded-xl relative group/photo"
            >
              <img
                :src="photo"
                :alt="`${trip.location} ${index + 1}`"
                class="w-full h-full object-cover transition-transform duration-500 group-hover/photo:scale-105"
              />
            </div>
          </div>
        </div>
      </div>
    </Motion>
  </div>
</template>