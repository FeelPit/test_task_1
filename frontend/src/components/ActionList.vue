<template>
  <div>
    <h2>User Actions</h2>
    <form @submit.prevent="fetchActions">
      <input v-model="user_id" placeholder="User ID" />
      <button type="submit">Get Actions</button>
    </form>
    <ul>
      <li v-for="a in actions" :key="a.id">
        {{ a.timestamp }} — {{ a.action_type }} — {{ a.description }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'

const user_id = ref('')
const actions = ref([])
const API_URL = import.meta.env.VITE_BACKEND_URL || 'http://localhost:8000/api'

function fetchActions() {
  axios.get(`http://localhost:8000/api/action/user/${user_id.value}/`)
    .then(res => {
      actions.value = res.data
    }).catch(err => {
      console.error(err)
      alert('Error fetching actions')
    })
}
</script>
