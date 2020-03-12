<template lang="html">
  <div class="container">
    <div class="first">
      <h1>{{ first[0] }}</h1>
      <h2>{{ first[1]}} Match</h2>
    </div>
    <div class="row">
      <div class="col">
        <h2>{{ second[0] }}</h2>
        <h3>{{ second[1] }} Match</h3>
      </div>
      <div class="col">
        <h2>{{ third[0] }}</h2>
        <h3>{{ third[1] }} Match</h3>
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
      second: '',
      third: '',
    }
  },
  methods: {
    getFirst() {
      const path = 'http://localhost:5000/first'
      axios.get(path)
      .then((res) => {
        this.first = res.data
      })
    },
    getSecond() {
      const path = 'http://localhost:5000/second'
      axios.get(path)
      .then((res) => {
        this.second = res.data
      })
    },
    getThird() {
      const path = 'http://localhost:5000/third'
      axios.get(path)
      .then((res) => {
        this.third = res.data
      })
    }
  },
  created() {
    this.getFirst(),
    this.getSecond(),
    this.getThird()
  }
}
</script>

<style lang="css" scoped>
/* .first {
  margin: auto;
  padding: 40px;
  border-radius: 10px;
  background-color: #BBECD2;
  text-align: center;
  max-width: 600px;
} */
</style>
