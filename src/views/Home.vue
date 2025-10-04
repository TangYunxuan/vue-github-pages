<template>
  <div class="min-h-screen">
    <!-- Hero Section -->
    <section class="relative px-6 py-24 overflow-hidden">
      <div class="max-w-7xl mx-auto">
        <div class="grid lg:grid-cols-2 gap-16 items-center">
          <!-- Left Content -->
          <div
            v-motion
            :initial="{ opacity: 0, x: -50 }"
            :enter="{ opacity: 1, x: 0, transition: { duration: 0.8 } }"
            class="space-y-8"
          >
            <div class="space-y-4">
              <h1
                class="text-5xl md:text-7xl font-bold text-stone-800 leading-tight"
                v-motion
                :initial="{ opacity: 0, y: 30 }"
                :enter="{ opacity: 1, y: 0, transition: { duration: 0.8, delay: 0.2 } }"
              >
                Hello, I'm
                <span class="block bg-gradient-to-r from-amber-500 to-orange-500 bg-clip-text text-transparent">
                  Creative
                </span>
              </h1>
              <p
                class="text-xl text-stone-600 leading-relaxed max-w-lg"
                v-motion
                :initial="{ opacity: 0, y: 30 }"
                :enter="{ opacity: 1, y: 0, transition: { duration: 0.8, delay: 0.4 } }"
              >
                Welcome to my personal corner of the internet. Here I share my passions,
                adventures, thoughts, and the projects that shape my journey.
              </p>
            </div>
            <div
              class="flex flex-col sm:flex-row gap-4"
              v-motion
              :initial="{ opacity: 0, y: 30 }"
              :enter="{ opacity: 1, y: 0, transition: { duration: 0.8, delay: 0.6 } }"
            >
              <RouterLink
                :to="createPageUrl('Cute')"
                class="group inline-flex items-center justify-center px-8 py-4 bg-gradient-to-r from-amber-500 to-orange-500 text-white font-semibold rounded-full hover:from-amber-600 hover:to-orange-600 transition-all duration-300 shadow-lg hover:shadow-xl transform hover:-translate-y-1"
              >
                <Heart class="w-5 h-5 mr-2" />
                Meet My Cat
                <ArrowRight class="w-5 h-5 ml-2 group-hover:translate-x-1 transition-transform" />
              </RouterLink>
              <RouterLink
                :to="createPageUrl('Projects')"
                class="group inline-flex items-center justify-center px-8 py-4 bg-white/80 backdrop-blur text-stone-700 font-semibold rounded-full hover:bg-white transition-all duration-300 shadow-lg hover:shadow-xl border border-stone-200 transform hover:-translate-y-1"
              >
                View My Work
                <ArrowRight class="w-5 h-5 ml-2 group-hover:translate-x-1 transition-transform" />
              </RouterLink>
            </div>
          </div>

          <!-- Right Image -->
          <div
            class="relative"
            v-motion
            :initial="{ opacity: 0, x: 50 }"
            :enter="{ opacity: 1, x: 0, transition: { duration: 0.8, delay: 0.3 } }"
          >
            <div class="relative w-full h-96 lg:h-[500px] rounded-3xl overflow-hidden shadow-2xl">
              <div class="absolute inset-0 bg-gradient-to-br from-amber-400/20 to-orange-500/20 z-10"></div>
              <img
                src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=600&h=800&fit=crop&crop=face"
                alt="Profile"
                class="w-full h-full object-cover"
              />
            </div>
          </div>
        </div>
      </div>
      <div class="absolute top-20 left-20 w-32 h-32 bg-gradient-to-r from-amber-400/10 to-orange-500/10 rounded-full blur-3xl"></div>
      <div class="absolute bottom-20 right-20 w-40 h-40 bg-gradient-to-r from-pink-400/10 to-purple-500/10 rounded-full blur-3xl"></div>
    </section>

    <!-- Features Section -->
    <section class="px-6 py-24 bg-white/50 backdrop-blur">
      <div class="max-w-7xl mx-auto">
        <div
          class="text-center mb-16"
          v-motion
          :initial="{ opacity: 0, y: 50 }"
          :enter="{ opacity: 1, y: 0, transition: { duration: 0.8 } }"
        >
          <h2 class="text-4xl md:text-5xl font-bold text-stone-800 mb-4">Explore My World</h2>
          <p class="text-xl text-stone-600 max-w-2xl mx-auto">
            Dive into different aspects of my life, from adorable cat photos to academic projects and travel adventures.
          </p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          <div
            v-for="(feature, index) in features"
            :key="feature.title"
            class="group"
            v-motion
            :initial="{ opacity: 0, y: 50 }"
            :enter="{ opacity: 1, y: 0, transition: { duration: 0.6, delay: index * 0.1 } }"
          >
            <RouterLink :to="feature.url" class="block h-full">
              <div class="h-full bg-white/80 backdrop-blur-sm rounded-3xl p-8 shadow-lg hover:shadow-2xl transition-all duration-300 border border-white/20">
                <div :class="`w-16 h-16 rounded-2xl bg-gradient-to-r ${feature.color} flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300`">
                  <component :is="feature.icon" class="w-8 h-8 text-white" />
                </div>
                <h3 class="text-2xl font-bold text-stone-800 mb-4 group-hover:text-amber-600 transition-colors">
                  {{ feature.title }}
                </h3>
                <p class="text-stone-600 leading-relaxed mb-6">
                  {{ feature.description }}
                </p>
                <div class="flex items-center text-amber-600 font-semibold group-hover:translate-x-2 transition-transform duration-300">
                  <span>Explore</span>
                  <ArrowRight class="w-4 h-4 ml-2" />
                </div>
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
import { Heart, PenTool, MapPin, Briefcase, ArrowRight } from 'lucide-vue-next';
import { useMotion } from '@vueuse/motion';
import { createPageUrl } from '@/utils';

// 功能卡片（cute，thoughts，travels，projects）
const features = ref([
  // •	通过 v-for 渲染四个卡片
	// •	每个卡片中：
	// •	有彩色背景 icon（<component :is="feature.icon" />）
	// •	有标题、描述、探索按钮
  {
    icon: Heart,
    title: 'Cute',
    description: 'Meet my adorable cat through a beautiful photo gallery',
    color: 'from-pink-500 to-rose-500',
    url: createPageUrl('Cute')
  },

  {
    icon: PenTool,
    title: 'Thoughts',
    description: 'Personal reflections, stories, and insights from my journey',
    color: 'from-purple-500 to-indigo-500',
    url: createPageUrl('Thoughts')
  },

  {
    icon: MapPin,
    title: 'Travels',
    description: 'Interactive maps and stories from my adventures around the world',
    color: 'from-green-500 to-teal-500',
    url: createPageUrl('Travels')
  },

  {
    icon: Briefcase,
    title: 'Projects',
    description: 'Academic work, thesis research, and creative endeavors',
    color: 'from-blue-500 to-cyan-500',
    url: createPageUrl('Projects')
  }
]);
</script>

<style scoped></style>