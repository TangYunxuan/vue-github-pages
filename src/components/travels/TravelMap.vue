<script setup>
import { ref, watchEffect } from 'vue'
import {
  LMap,
  LTileLayer,
  LMarker,
  LPopup,
  LIcon
} from '@vue-leaflet/vue-leaflet'
import L from 'leaflet'
import { format } from 'date-fns'

const props = defineProps({
  trips: Array,
  onTripSelect: Function
})

const mapRef = ref(null)

// 自定义图标
const customIcon = new L.Icon({
  iconUrl:
    'data:image/svg+xml;base64,' +
    btoa(`
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#10b981" stroke="#065f46" stroke-width="1">
      <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
      <circle cx="12" cy="10" r="3" fill="#ffffff"/>
    </svg>
  `),
  iconSize: [30, 30],
  iconAnchor: [15, 30],
  popupAnchor: [0, -30]
})

// 自动 fitBounds
watchEffect(() => {
  if (props.trips.length > 0 && mapRef.value?.leafletObject) {
    const bounds = L.latLngBounds(
      props.trips.map(trip => [trip.latitude, trip.longitude])
    )
    mapRef.value.leafletObject.fitBounds(bounds, { padding: [30, 30] })
  }
})
</script>

<template>
  <div class="h-96 w-full relative">
    <LMap
      ref="mapRef"
      :zoom="2"
      :center="[20, 0]"
      class="rounded-2xl z-10"
      style="height: 100%; width: 100%"
    >
      <LTileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />

      <LMarker
        v-for="trip in trips"
        :key="trip.id"
        :lat-lng="[trip.latitude, trip.longitude]"
        :icon="customIcon"
        @click="() => onTripSelect(trip)"
      >
        <LPopup :options="{ closeButton: false }">
          <div class="p-3 min-w-60">
            <div class="flex justify-between items-start mb-3">
              <h3 class="font-bold text-stone-800 text-lg">
                {{ trip.location }}
              </h3>
              <span class="text-xs bg-green-100 text-green-700 px-2 py-1 rounded-full font-medium">
                {{ trip.country }}
              </span>
            </div>

            <p class="text-sm text-stone-600 mb-3 line-clamp-2">
              {{ trip.description }}
            </p>

            <div class="flex items-center justify-between">
              <p class="text-xs text-stone-500">
                📅 {{ format(new Date(trip.start_date), 'MMM yyyy') }}
              </p>
              <button
                @click="() => onTripSelect(trip)"
                class="text-xs bg-green-500 hover:bg-green-600 text-white px-3 py-1 rounded-full font-medium transition-colors"
              >
                View in Timeline →
              </button>
            </div>

            <img
              v-if="trip.photos?.length"
              :src="trip.photos[0]"
              :alt="trip.location"
              class="w-full h-24 object-cover rounded-lg mt-3"
            />
          </div>
        </LPopup>
      </LMarker>
    </LMap>

    <!-- 说明文字 -->
    <div
      class="absolute top-4 left-4 bg-white/90 backdrop-blur-sm px-3 py-2 rounded-lg shadow-lg text-sm text-stone-600 z-20"
    >
      💡 Click any pin to jump to that journey in the timeline
    </div>
  </div>
</template>