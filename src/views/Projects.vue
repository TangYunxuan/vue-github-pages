<template>
  <div class="min-h-screen px-6 py-12">
    <div class="max-w-6xl mx-auto">
      <!-- Header -->
      <div
        class="text-center mb-16"
        v-motion
        v-motion-fade-slide-y
      >
        <h1 class="text-5xl md:text-6xl font-bold text-stone-800 mb-6">
          My
          <span class="block bg-gradient-to-r from-indigo-500 to-purple-500 bg-clip-text text-transparent">
            Projects
          </span>
        </h1>
        <p class="text-xl text-stone-600 max-w-2xl mx-auto">
          A collection of the works I've built, the ideas I've developed, and the lessons I’ve learned.
        </p>
      </div>

      <!-- Filter Buttons -->
      <div class="flex justify-center gap-4 mb-12">
        <Button
          v-for="filter in filters"
          :key="filter"
          :variant="activeFilter === filter ? 'default' : 'outline'"
          @click="activeFilter = filter"
          class="capitalize"
        >
          {{ filter }}
        </Button>
      </div>

      <!-- Project Cards -->
      <div v-if="isLoading" class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div
          v-for="i in 3"
          :key="i"
          class="bg-white/50 rounded-3xl p-6 animate-pulse"
        >
          <div class="w-3/4 h-6 bg-slate-300 mb-4 rounded" />
          <div class="h-4 bg-slate-200 mb-2 rounded" />
          <div class="h-4 bg-slate-200 w-5/6 rounded" />
        </div>
      </div>

      <div
        v-else
        class="grid md:grid-cols-2 lg:grid-cols-3 gap-8"
        v-motion
        v-motion-fade
      >
        <ProjectCard
          v-for="project in displayedProjects"
          :key="project.id"
          :project="project"
          @click="selectedProject = project"
        />
      </div>

      <!-- Statistics -->
      <div
        v-if="!isLoading && projects.length > 0"
        class="grid md:grid-cols-3 gap-6 mt-16"
        v-motion
        v-motion-fade-slide-y
      >
        <StatCard icon="Folder" :count="projects.length" label="Total Projects" color="indigo" />
        <StatCard icon="GraduationCap" :count="countByCategory('course')" label="Course Projects" color="emerald" />
        <StatCard icon="UserCheck" :count="countByCategory('thesis')" label="Thesis Projects" color="rose" />
      </div>

      <!-- Login Prompt -->
      <div
        v-if="!user && projects.length > 3"
        class="text-center py-16 bg-stone-50 rounded-3xl mt-16"
        v-motion
        v-motion-fade-slide-y
      >
        <div class="w-24 h-24 mx-auto mb-6 bg-gradient-to-r from-amber-500 to-orange-500 rounded-full flex items-center justify-center">
          <LogIn class="w-12 h-12 text-white" />
        </div>
        <h3 class="text-2xl font-semibold text-stone-800 mb-4">Want to see more projects?</h3>
        <p class="text-stone-600 mb-8">Log in as admin to access the full list and details.</p>
        <Button class="bg-gradient-to-r from-amber-500 to-orange-500 text-white px-8 py-3 rounded-full font-semibold" @click="User.login">
          Admin Login
        </Button>
      </div>

      <!-- Project Detail Modal -->
      <ProjectDetail v-if="selectedProject" :project="selectedProject" @close="selectedProject = null" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import Project from '@/Entities/Project.json'
import User from '@/Entities/User.js'
import ProjectCard from '@/components/projects/ProjectCard.vue';
import ProjectDetail from '@/components/projects/ProjectDetail.vue';
import StatCard from '@/components/projects/StatCard.vue';
import  Button  from '@/components/ui/button.vue';
import { LogIn } from 'lucide-vue-next';

const projects = ref([]);
const selectedProject = ref(null);
const isLoading = ref(true);
const user = ref(null);
const activeFilter = ref('all');
const filters = ['all', 'course', 'thesis', 'personal'];

onMounted(async () => {
  try {
    user.value = await User.me();
  } catch (e) {
    user.value = null;
  }
  const fetched = await Project.list('-created');
  projects.value = fetched;
  isLoading.value = false;
});

const filteredProjects = computed(() => {
  return activeFilter.value === 'all'
    ? projects.value
    : projects.value.filter(p => p.category === activeFilter.value);
});

const displayedProjects = computed(() => {
  return user.value && user.value.role === 'admin'
    ? filteredProjects.value
    : filteredProjects.value.slice(0, 3);
});

const countByCategory = (cat) => {
  return projects.value.filter(p => p.category === cat).length;
};
</script>

<style scoped>
/* Optional styling */
</style>