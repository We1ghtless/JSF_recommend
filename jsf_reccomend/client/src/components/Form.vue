<template>
  <div class="formBox" name="box">
    <h3>{{ question.question }}</h3>
    <select class="form-control">
      <option hidden value="" selected>Select an option...</option>
      <option v-bind:key="answer" v-for="answer in question.answers" :value="answer">{{ answer }}</option>
    </select>
    <button type="button" class="btn btn-primary" @click="i += 1, getQuestions(), getResult()">Next</button>
    <p>{{i}}</p>
  </div>

  <!-- <div class="container">
  <transition name="fade" >
  <button type="button" class="btn btn-primary" v-on:click="show = !show, hide = !hide" v-if="hide">This</button>
</transition>
<transition name="fade" >
<button type="button" class="btn btn-primary" v-if="show" v-on:click="hide = !hide, show = !show">That</button>
</transition>
</div> -->
</template>

<script>
import axios from 'axios';
export default {
  name: 'Form',
  data() {
    return {
      show: false,
      hide: true,
      selected: '',
      result: '',
      question: [],
      i: 0
    };
  },
  methods: {
    getQuestions() {
      const path = 'http://localhost:5000/'+this.i;
      axios.get(path)
      .then((res) => {
        this.question = res.data;
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
      });
    },
    getResult() {
      if (this.i == 10) {
        this.$router.push({name:'Result'})
      }
    }
  },
  created() {
    this.getQuestions();
  },
}
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 1s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}

.formBox {
  margin: auto;
  padding: 40px;
  border-radius: 10px;
  background-color: #BBECD2;
  text-align: center;
  max-width: 600px;
}
</style>
