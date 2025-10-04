<template>
  <div class="min-h-screen px-6 py-12">
    <div class="max-w-7xl mx-auto">
      <div class="text-center mb-16">
        <h1 class="text-5xl md:text-6xl font-bold text-stone-800 mb-6">
          My
          <span class="block bg-gradient-to-r from-green-500 to-teal-500 bg-clip-text text-transparent">
            Adventures
          </span>
        </h1>
        <p class="text-xl text-stone-600 max-w-2xl mx-auto mb-8">
          Explore the places I've been and the journeys that have shaped my perspective.
          Click on any location on the map to jump to that journey in my travel timeline.
        </p>
      </div>

      <div class="bg-white/80 backdrop-blur-sm rounded-3xl p-8 shadow-lg mb-16 border border-white/20">
        <div class="flex items-center justify-between mb-6">
          <h2 class="text-2xl font-bold text-stone-800 flex items-center gap-3">
            <Globe class="w-7 h-7 text-green-500" />
            Interactive Travel Map
          </h2>
          <div class="text-sm text-stone-500">
            {{ trips.length }} destinations explored
          </div>
        </div>
        <div class="rounded-2xl overflow-hidden shadow-inner">
          <TravelMap :trips="trips" @trip-select="handleTripSelect" />
        </div>
      </div>

      <div ref="timelineRef" class="mb-16">
        <div class="flex items-center justify-center mb-8 gap-3">
          <History class="w-8 h-8 text-green-500" />
          <h2 class="text-3xl font-bold text-stone-800 text-center">
            My Travel Journal
          </h2>
        </div>
        <TripTimeline :trips="displayedTrips" @trip-select="handleTripDetail" />
      </div>

      <div class="grid md:grid-cols-3 gap-6 mb-16">
        <div class="bg-white/80 backdrop-blur-sm rounded-3xl p-8 shadow-lg border border-white/20 text-center">
          <div class="w-16 h-16 mx-auto mb-4 bg-gradient-to-r from-green-500 to-teal-500 rounded-full flex items-center justify-center">
            <MapPin class="w-8 h-8 text-white" />
          </div>
          <h3 class="text-3xl font-bold text-stone-800">{{ trips.length }}</h3>
          <p class="text-stone-600">Destinations</p>
        </div>

        <div class="bg-white/80 backdrop-blur-sm rounded-3xl p-8 shadow-lg border border-white/20 text-center">
          <div class="w-16 h-16 mx-auto mb-4 bg-gradient-to-r from-blue-500 to-cyan-500 rounded-full flex items-center justify-center">
            <Globe class="w-8 h-8 text-white" />
          </div>
          <h3 class="text-3xl font-bold text-stone-800">
            {{ countryCount }}
          </h3>
          <p class="text-stone-600">Countries</p>
        </div>

        <div class="bg-white/80 backdrop-blur-sm rounded-3xl p-8 shadow-lg border border-white/20 text-center">
          <div class="w-16 h-16 mx-auto mb-4 bg-gradient-to-r from-purple-500 to-pink-500 rounded-full flex items-center justify-center">
            <Camera class="w-8 h-8 text-white" />
          </div>
          <h3 class="text-3xl font-bold text-stone-800">
            {{ totalPhotos }}
          </h3>
          <p class="text-stone-600">Photos</p>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { MapPin, Calendar, Camera, Plus, Globe, History, LogIn } from 'lucide-vue-next';
import TravelMap from '@/components/travels/TravelMap.vue';
import TripTimeline from '@/components/travels/TripTimeline.vue';
import TripDetail from '@/components/travels/TripDetail.vue';


const trips = ref([]);
const selectedTrip = ref(null);
const showEditor = ref(false);
const showDetail = ref(false);
const isLoading = ref(true);
const timelineRef = ref(null);

const loadTrips = async () => {
  // Replace with your API
  const fetched = await fetchTrips();
  trips.value = fetched;
  isLoading.value = false;
};

const handleTripSelect = (trip) => {
  const tripElement = document.getElementById(`trip-${trip.id}`);
  if (tripElement && timelineRef.value) {
    tripElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
    tripElement.classList.add('ring-4', 'ring-green-400', 'ring-opacity-75');
    setTimeout(() => {
      tripElement.classList.remove('ring-4', 'ring-green-400', 'ring-opacity-75');
    }, 2000);
  }
};

const handleTripDetail = (trip) => {
  selectedTrip.value = trip;
  showDetail.value = true;
};

onMounted(() => {
  loadTrips();
});

const displayedTrips = computed(() => trips.value);
const countryCount = computed(() => new Set(trips.value.map(t => t.country)).size);
const totalPhotos = computed(() => trips.value.reduce((acc, t) => acc + (t.photos?.length || 0), 0));

async function fetchTrips() {
  return [
    {
      id: 1,
      country: 'Italy',
      photos: [1, 2],
    },
    {
      id: 2,
      country: 'Japan',
      photos: [1],
    },
  ];
}
</script>

<style scoped>
</style>