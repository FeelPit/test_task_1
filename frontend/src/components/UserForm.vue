<template>
  <div>
    <h2>Create User</h2>
    <form @submit.prevent="createUser">
      <input v-model="username" placeholder="Username" />
      <input v-model="email" placeholder="Email" />
      <button type="submit">Create</button>
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'

const username = ref('')
const email = ref('')
const API_URL = import.meta.env.VITE_BACKEND_URL || 'http://localhost:8000/api'

function createUser() {
  axios.post('http://localhost:8000/api/user/', {
    username: username.value,
    email: email.value
  }).then(() => {
    alert('User created!')
  }).catch(err => {
    console.error(err)
    alert('Error creating user')
  })
}
</script>
