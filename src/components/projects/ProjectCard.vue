<script setup>
import { computed } from 'vue'
import { Motion } from '@vueuse/motion'
import {
  Calendar,
  Github,
  ExternalLink,
  Code,
  GraduationCap,
  User,
  Search
} from 'lucide-vue-next'
import { format } from 'date-fns'

defineProps({
  project: Object,
  onClick: Function
})

// 图标映射
const typeIcons = {
  course: GraduationCap,
  thesis: Search,
  research: Search,
  personal: User
}

// 颜色映射
const typeColors = {
  course: 'bg-green-100 text-green-700 border-green-200',
  thesis: 'bg-purple-100 text-purple-700 border-purple-200',
  research: 'bg-blue-100 text-blue-700 border-blue-200',
  personal: 'bg-orange-100 text-orange-700 border-orange-200'
}

const statusColors = {
  completed: 'bg-green-100 text-green-700',
  'in-progress': 'bg-yellow-100 text-yellow-700',
  planned: 'bg-gray-100 text-gray-700'
}

// 当前图标组件
const TypeIcon = computed(() => typeIcons[project.type] || Code)
</script>

<template>
  <Motion
    :initial="{ opacity: 0, y: 50 }"
    :enter="{ opacity: 1, y: 0 }"
    :leave="{ opacity: 0, y: -50 }"
    :hover="{ scale: 1.02, y: -5 }"
    class="group cursor-pointer"
    @click="onClick"
  >
    <div class="bg-white/80 backdrop-blur-sm rounded-3xl p-6 shadow-lg hover:shadow-2xl transition-all duration-300 border border-white/20 h-full flex flex-col">
      <!-- 封面图 -->
      <div
        v-if="project.images?.length"
        class="aspect-video overflow-hidden rounded-2xl mb-6 relative"
      >
        <img
          :src="project.images[0]"
          :alt="project.title"
          class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
        />
        <div class="absolute inset-0 bg-gradient-to-t from-black/20 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
      </div>

      <div class="flex-1 space-y-4">
        <!-- 标题和图标 -->
        <div class="space-y-3">
          <div class="flex items-start justify-between">
            <h3 class="text-xl font-bold text-stone-800 line-clamp-2 group-hover:text-blue-600 transition-colors leading-tight flex-1">
              {{ project.title }}
            </h3>
            <component :is="TypeIcon" class="w-5 h-5 text-blue-600 ml-2 flex-shrink-0" />
          </div>

          <p class="text-stone-600 line-clamp-3 leading-relaxed">
            {{ project.description }}
          </p>
        </div>

        <!-- 类型 & 状态 -->
        <div class="flex flex-wrap gap-2">
          <span
            class="border rounded-full px-2 py-1 text-xs font-medium"
            :class="typeColors[project.type]"
          >
            {{ project.type.replace('_', ' ') }}
          </span>
          <span
            class="rounded-full px-2 py-1 text-xs font-medium"
            :class="statusColors[project.status]"
          >
            {{ project.status.replace('-', ' ') }}
          </span>
        </div>

        <!-- 技术栈 & 时间 -->
        <div class="space-y-3">
          <div
            v-if="project.technologies?.length"
            class="flex flex-wrap gap-1"
          >
            <span
              v-for="tech in project.technologies.slice(0, 4)"
              :key="tech"
              class="text-xs bg-stone-100 text-stone-700 hover:bg-stone-200 rounded-full px-2 py-0.5"
            >
              {{ tech }}
            </span>
            <span
              v-if="project.technologies.length > 4"
              class="text-xs border rounded-full px-2 py-0.5"
            >
              +{{ project.technologies.length - 4 }}
            </span>
          </div>

          <div class="flex items-center justify-between text-sm text-stone-500 pt-4 border-t border-stone-200">
            <div class="flex items-center space-x-1">
              <Calendar class="w-4 h-4" />
              <span>
                {{
                  project.start_date
                    ? format(new Date(project.start_date), 'MMM yyyy')
                    : format(new Date(project.created_date), 'MMM yyyy')
                }}
              </span>
            </div>

            <div class="flex items-center space-x-2">
              <a
                v-if="project.github_url"
                :href="project.github_url"
                target="_blank"
                rel="noopener noreferrer"
              >
                <Github class="w-4 h-4 text-stone-400 hover:text-stone-600 transition-colors" />
              </a>
              <a
                v-if="project.demo_url"
                :href="project.demo_url"
                target="_blank"
                rel="noopener noreferrer"
              >
                <ExternalLink class="w-4 h-4 text-stone-400 hover:text-stone-600 transition-colors" />
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </Motion>
</template>