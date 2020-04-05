<template lang="html">
  <div class="">
    <h1>Result</h1>
    <div class="container">
      <div class="first" id="1">
        <img :src="result[3]" alt="">
        <div class="text">
          <h1>{{ result[0] }}</h1>
          <h2>{{ result[1]}}</h2>
          <p>{{ result[4]}}</p>
          <a :href="result[5]" target="_blank">{{ result[5] }}</a>
        </div>
      </div>
      <div class="row">
        <div class="col" id="2">
          <img :src="result[9]" alt="">
          <div class="text">
            <h3>{{ result[6] }}</h3>
            <h4>{{ result[7] }}</h4>
            <a :href="result[11]" target="_blank">{{ result[11]}}</a>
          </div>
        </div>
        <div class="col" id="3">
          <img :src="result[15]" alt="">
          <div class="text">
            <h3>{{ result[12] }}</h3>
            <h4>{{ result[13] }}</h4>
            <a :href="result[17]" target="_blank">{{ result[17] }}</a>
          </div>
        </div>
      </div>
      <div class="formBox" >
        <h1>Answers</h1>
        <ul class="list-group list-group-flush">
          <li class="list-group-item">
            <div class="container">
              {{ result[21] }}
            </div>
          </li>
          <li class="list-group-item">
            <div class="container">
              {{ result[20] }}
            </div>
          </li>
          <li class="list-group-item">
            <div class="container">
              {{ result[19] }}
            </div>
          </li>
          <li class="list-group-item">
            <div class="container">
              {{ result[18] }}
            </div>
          </li>
        </ul>
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
      result: '',
    }
  },
  methods: {
    getResult() {
      const path = 'http://localhost:5000/first'
      axios.get(path)
      .then((res) => {
        this.result = res.data
        document.getElementById("1").style.backgroundColor = this.result[2];
        document.getElementById("2").style.backgroundColor = this.result[8];
        document.getElementById("3").style.backgroundColor = this.result[14];
      })
    }
  },
  created() {
    this.getResult()
  },
}

</script>

<style lang="css" scoped>

img {
  width: 100px;
  height: 100px;
}

.first {
  padding: 40px;
  /* border-radius: 10px; */
  text-align: center;
}

.col {
  padding: 10px;
  /* border-radius: 10px; */
  text-align: center;
  margin: 15px;
}

.text {
  background-color: white;
  /* border-radius: 10px; */
  margin-top: 10px;
  padding: 10px;
}

a {
  color: black;
  text-decoration: underline;
}

.formBox {
  margin: auto;
  padding: 40px;
  border-radius: 10px;
  text-align: center;
  max-width: 600px;
}
h1 {
  font-weight: 300;
  text-align: center;
}

h2 {
  font-weight: 300;
}

h3 {
  font-weight: 300;
}

h4 {
  font-weight: 300;
}

.list-group-item {
  border: 0px;
  background-color: rgba(255, 255, 255, 0.8);
}
</style>
