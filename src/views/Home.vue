<template>

  <div class="min-h-screen bg-white text-stone-800">
    <!-- Hero Section -->
    <section class="relative px-6 py-20 md:py-24 overflow-hidden">
      <div class="grid lg:grid-cols-2 gap-16 items-center max-w-7xl mx-auto">
        <!-- Left Text -->
        <div
          v-motion
          :initial="{ opacity: 0, x: -40 }"
          :enter="{ opacity: 1, x: 0, transition: { duration: 0.7 } }"
          class="space-y-6 max-w-2xl"
        >
          <h1 class="text-4xl md:text-6xl font-bold leading-tight">
            Hi, I'm <span class="text-amber-600">Yunxuan Tang</span>
          </h1>
          <p class="text-lg text-stone-600 leading-relaxed">
            A <span class="font-semibold text-stone-800">Computer Science MSc student</span> in Amsterdam 🇳🇱,<br />
            currently seeking a <strong class="text-amber-600">Thesis Internship (2025)</strong>.<br />
            I build things at the intersection of <em>software engineering</em> and <em>digital twins</em>.
          </p>
          <div class="flex flex-wrap gap-4">
            <RouterLink
              :to="createPageUrl('Projects')"
              class="px-6 py-3 bg-amber-500 hover:bg-amber-600 text-white rounded-full font-semibold transition-all"
            >
              View My Work
            </RouterLink>
            <RouterLink
              :to="createPageUrl('Cute')"
              class="px-6 py-3 bg-white text-stone-700 border border-stone-300 rounded-full font-semibold hover:bg-stone-100 transition-all"
            >
              Meet My Cat
            </RouterLink>
          </div>
        </div>


<!-- Centered Circular Avatar -->
<div
  class="flex justify-center items-center"
  v-motion
  :initial="{ opacity: 0, y: 20 }"
  :enter="{ opacity: 1, y: 0, transition: { duration: 0.7, delay: 0.2 } }"
>
  <div
    class="overflow-hidden rounded-full shadow-md border border-stone-200 "
    style="flex: 0 0 auto; width: min(40vw, 296px); max-width: 296px; aspect-ratio: 1 / 1;"
  >
    <img
      src="https://cdn.jsdelivr.net/gh/TangYunxuan/tangyunxuan-assets@main/images/tyx.jpg"
      alt="Yunxuan Tang"
      style="width: 100%; height: 100%; object-fit: cover; display: block;"
    />
  </div>
</div>
      </div>

      <!-- background blobs -->
      <div class="absolute top-10 left-10 w-32 h-32 bg-amber-300/20 rounded-full blur-3xl"></div>
      <div class="absolute bottom-10 right-10 w-40 h-40 bg-orange-400/20 rounded-full blur-3xl"></div>
    </section>

    <!-- Feature Section -->
    <section class="px-6 py-20 bg-stone-50">
      <div class="max-w-7xl mx-auto">
        <div
          class="text-center mb-16"
          v-motion
          :initial="{ opacity: 0, y: 40 }"
          :enter="{ opacity: 1, y: 0, transition: { duration: 0.6 } }"
        >
          <h2 class="text-3xl md:text-4xl font-bold">Explore My Site</h2>
          <p class="text-stone-600 mt-4">Discover what makes my world unique – from cat photos to real projects.</p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          <div
            v-for="(feature, index) in features"
            :key="feature.title"
            class="group"
            v-motion
            :initial="{ opacity: 0, y: 30 }"
            :enter="{ opacity: 1, y: 0, transition: { duration: 0.5, delay: index * 0.1 } }"
          >
            <RouterLink :to="feature.url" class="block h-full">
              <div class="h-full bg-white rounded-2xl p-6 shadow-md hover:shadow-xl transition-all border border-stone-100">
                <div
                  :class="`w-12 h-12 rounded-xl bg-gradient-to-r ${feature.color} flex items-center justify-center mb-4`"
                >
                  <component :is="feature.icon" class="w-6 h-6 text-white" />
                </div>
                <h3 class="text-xl font-semibold mb-2 group-hover:text-amber-600">{{ feature.title }}</h3>
                <p class="text-stone-600 text-sm">{{ feature.description }}</p>
              </div>
            </RouterLink>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { RouterLink } from 'vue-router';
import { Heart, PenTool, MapPin, Briefcase } from 'lucide-vue-next';
import { createPageUrl } from '@/utils';

const features = ref([
  {
    icon: Heart,
    title: 'Cute',
    description: 'Photos of my adorable cat and life moments.',
    color: 'from-pink-500 to-rose-500',
    url: createPageUrl('Cute')
  },
  {
    icon: PenTool,
    title: 'Thoughts',
    description: 'Reflections, essays, and tech explorations.',
    color: 'from-purple-500 to-indigo-500',
    url: createPageUrl('Thoughts')
  },
  {
    icon: MapPin,
    title: 'Travels',
    description: 'Maps and stories from trips around the world.',
    color: 'from-green-500 to-teal-500',
    url: createPageUrl('Travels')
  },
  {
    icon: Briefcase,
    title: 'Projects',
    description: 'Academic and side projects I’ve worked on.',
    color: 'from-blue-500 to-cyan-500',
    url: createPageUrl('Projects')
  }
]);
</script>