<template lang="html">
  <div class="container">
    <div class="first" id="1">
      <img :src="first[3]" alt="">
      <div class="text">
        <h1>{{ first[0] }}</h1>
        <h2>{{ first[1]}}</h2>
      </div>
    </div>
    <div class="row">
      <div class="col" id="2">
        <img :src="second[3]" alt="">
        <div class="text">
          <h3>{{ second[0] }}</h3>
          <h4>{{ second[1] }}</h4>
        </div>
      </div>
      <div class="col" id="3">
        <img :src="third[3]" alt="">
        <div class="text">
          <h3>{{ third[0] }}</h3>
          <h4>{{ third[1] }}</h4>
        </div>
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
        document.getElementById("1").style.backgroundColor = this.first[2];
      })
    },
    getSecond() {
      const path = 'http://localhost:5000/second'
      axios.get(path)
      .then((res) => {
        this.second = res.data
        document.getElementById("2").style.backgroundColor = this.second[2];

      })
    },
    getThird() {
      const path = 'http://localhost:5000/third'
      axios.get(path)
      .then((res) => {
        this.third = res.data
        document.getElementById("3").style.backgroundColor = this.third[2];
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

img {
  width: 100px;
  height: 100px;
}

.first {
  padding: 40px;
  border-radius: 10px;
  text-align: center;
}

.col {
  padding: 10px;
  border-radius: 10px;
  text-align: center;
  margin: 15px;
}

.text {
  background-color: white;
  border-radius: 10px;
  margin-top: 10px;
  padding: 10px;
}
</style>
