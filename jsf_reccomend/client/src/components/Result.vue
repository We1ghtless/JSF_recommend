<template lang="html">
  <div class="container">
    <div class="first">
      <h1>{{ first[0] }}</h1>
      <h2>{{ first[1]}} Match</h2>
    </div>
    <div class="row">
      <div class="col">

      </div>
      <div class="col">

      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Result',
  data() {
    return {
      first: '',
    }
  },
  methods: {
    getFirst(){
      const path = 'http://localhost:5000/result'
      axios.get(path)
      .then((res) => {
        this.first = res.data
      })
    }
  },
  created() {
    this.getFirst()
  }
}
</script>

<style lang="css" scoped>
.first {
  margin: auto;
  padding: 40px;
  border-radius: 10px;
  background-color: #BBECD2;
  text-align: center;
  max-width: 600px;
}
</style>
