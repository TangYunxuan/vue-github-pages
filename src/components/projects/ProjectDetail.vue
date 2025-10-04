<script setup>
import { computed } from 'vue'
import { Motion } from '@vueuse/motion'
import {
  X,
  Calendar,
  Github,
  ExternalLink,
  Code,
  Tag,
  Image as ImageIcon
} from 'lucide-vue-next'
import { format } from 'date-fns'

defineProps({
  project: Object,
  onClose: Function
})

const statusColors = {
  completed: 'bg-green-100 text-green-700 border-green-200',
  'in-progress': 'bg-yellow-100 text-yellow-700 border-yellow-200',
  planned: 'bg-gray-100 text-gray-700 border-gray-200'
}

// 计算日期范围
const formatDateRange = () => {
  if (!project.start_date) return 'Date not specified'

  const start = format(new Date(project.start_date), 'MMMM yyyy')
  const end = project.end_date
    ? format(new Date(project.end_date), 'MMMM yyyy')
    : 'Present'

  return project.end_date && project.start_date !== project.end_date
    ? `${start} - ${end}`
    : start
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
      class="bg-white rounded-3xl max-w-5xl w-full max-h-[90vh] overflow-hidden"
      @click.stop
    >
      <!-- Header -->
      <div class="relative">
        <!-- Header Image -->
        <div v-if="project.images?.length" class="aspect-[3/1] overflow-hidden">
          <img
            :src="project.images[0]"
            :alt="project.title"
            class="w-full h-full object-cover"
          />
          <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent" />
        </div>

        <!-- Close Button -->
        <button
          @click="onClose"
          class="absolute top-4 right-4 bg-white/90 backdrop-blur hover:bg-white p-2 rounded-full"
        >
          <X class="w-6 h-6" />
        </button>

        <!-- Title Section -->
        <div
          class="p-8"
          :class="project.images?.length ? 'absolute bottom-0 left-0 right-0 text-white' : ''"
        >
          <div class="flex flex-wrap items-center gap-3 mb-4">
            <span
              class="border px-2 py-1 text-sm font-medium rounded-full"
              :class="statusColors[project.status]"
            >
              {{ project.status.replace('-', ' ') }}
            </span>
            <span
              class="px-2 py-1 text-sm font-medium rounded-full border"
              :class="project.images?.length ? 'bg-white/20 text-white' : 'text-stone-500 border-stone-200'"
            >
              {{ project.type.replace('_', ' ') }}
            </span>
          </div>

          <h1
            class="text-4xl md:text-5xl font-bold mb-4 leading-tight"
            :class="project.images?.length ? 'drop-shadow-lg' : 'text-stone-800'"
          >
            {{ project.title }}
          </h1>

          <div class="flex flex-wrap items-center gap-6 text-sm">
            <div
              class="flex items-center space-x-2"
              :class="project.images?.length ? 'text-white/90' : 'text-stone-500'"
            >
              <Calendar class="w-4 h-4" />
              <span>{{ formatDateRange() }}</span>
            </div>

            <a
              v-if="project.github_url"
              :href="project.github_url"
              target="_blank"
              rel="noopener noreferrer"
              class="flex items-center space-x-2 hover:underline"
              :class="project.images?.length ? 'text-white/90 hover:text-white' : 'text-stone-500 hover:text-stone-700'"
            >
              <Github class="w-4 h-4" />
              <span>View Code</span>
            </a>

            <a
              v-if="project.demo_url"
              :href="project.demo_url"
              target="_blank"
              rel="noopener noreferrer"
              class="flex items-center space-x-2 hover:underline"
              :class="project.images?.length ? 'text-white/90 hover:text-white' : 'text-stone-500 hover:text-stone-700'"
            >
              <ExternalLink class="w-4 h-4" />
              <span>Live Demo</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Content Section -->
      <div class="p-8 overflow-y-auto max-h-[60vh]">
        <!-- Description -->
        <div class="mb-8">
          <p class="text-lg text-stone-600 leading-relaxed whitespace-pre-line">
            {{ project.description }}
          </p>
        </div>

        <!-- Technologies -->
        <div v-if="project.technologies?.length" class="mb-8">
          <h3 class="text-2xl font-bold text-stone-800 mb-4 flex items-center gap-2">
            <Code class="w-6 h-6 text-blue-500" />
            Technologies Used
          </h3>
          <div class="flex flex-wrap gap-2">
            <span
              v-for="tech in project.technologies"
              :key="tech"
              class="bg-blue-100 text-blue-700 border border-blue-200 text-sm rounded-full px-2 py-1 flex items-center gap-1"
            >
              <Tag class="w-3 h-3" />
              {{ tech }}
            </span>
          </div>
        </div>

        <!-- Gallery -->
        <div v-if="project.images?.length > 1" class="mb-8">
          <h3 class="text-2xl font-bold text-stone-800 mb-4 flex items-center gap-2">
            <ImageIcon class="w-6 h-6 text-purple-500" />
            Project Gallery
          </h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div
              v-for="(image, index) in project.images.slice(1)"
              :key="index"
              class="aspect-video overflow-hidden rounded-xl"
            >
              <img
                :src="image"
                :alt="`${project.title} ${index + 2}`"
                class="w-full h-full object-cover hover:scale-110 transition-transform duration-300"
              />
            </div>
          </div>
        </div>

        <!-- Project Links -->
        <div
          v-if="project.github_url || project.demo_url"
          class="bg-stone-50 rounded-2xl p-6"
        >
          <h3 class="text-xl font-bold text-stone-800 mb-4">Project Links</h3>
          <div class="flex flex-wrap gap-4">
            <a
              v-if="project.github_url"
              :href="project.github_url"
              target="_blank"
              rel="noopener noreferrer"
              class="flex items-center gap-2 px-4 py-2 bg-gray-900 text-white rounded-xl hover:bg-gray-800 transition-colors"
            >
              <Github class="w-4 h-4" />
              View on GitHub
            </a>
            <a
              v-if="project.demo_url"
              :href="project.demo_url"
              target="_blank"
              rel="noopener noreferrer"
              class="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-xl hover:bg-blue-700 transition-colors"
            >
              <ExternalLink class="w-4 h-4" />
              Live Demo
            </a>
          </div>
        </div>
      </div>
    </Motion>
  </Motion>
</template>