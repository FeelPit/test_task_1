<template>
  <div>
    <h2>Log Action</h2>
    <form @submit.prevent="createAction">
      <input v-model="user_id" placeholder="User ID" />
      <input v-model="action_type" placeholder="Action type" />
      <input v-model="description" placeholder="Description" />
      <button type="submit">Add</button>
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'

const user_id = ref('')
const action_type = ref('')
const description = ref('')
const API_URL = import.meta.env.VITE_BACKEND_URL || 'http://localhost:8000/api'

function createAction() {
  axios.post(`http://localhost:8000/api/action/`, {
    user: user_id.value,
    action_type: action_type.value,
    description: description.value
  }).then(() => {
    alert('Action added!')
  }).catch(err => {
    console.error(err)
    alert('Error adding action')
  })
}
</script>
