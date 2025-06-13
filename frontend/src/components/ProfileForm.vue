<template>
  <div>
    <h2>Create Profile</h2>
    <form @submit.prevent="createProfile">
      <input v-model="user_id" placeholder="User ID" />
      <input v-model="bio" placeholder="Bio" />
      <button type="submit">Create</button>
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'

const user_id = ref('')
const bio = ref('')
const API_URL = import.meta.env.VITE_BACKEND_URL || 'http://localhost:8000/api'

function createProfile() {
  axios.post(`http://localhost:8000/api/profile/`, {
    user: user_id.value,
    bio: bio.value
  }).then(() => {
    alert('Profile created!')
  }).catch(err => {
    console.error(err)
    alert('Error creating profile')
  })
}
</script>
