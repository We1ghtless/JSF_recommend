<template>
  <div class="form-group">
    <form class="needs-validation" novalidate>
      <div class="formBox" name="box">
        <h3>{{ question.question }}</h3>
        <div class="form-group">
          <select class="custom-select browser-default" v-model='selected' required>
            <option hidden value="" selected disabled>Select an option...</option>
            <option v-bind:key="answer" v-for="answer in question.answers" :value="answer">{{ answer }}</option>
          </select>
          <div class="invalid-feedback">Select answer</div>
        </div>
        <button type="button" class="btn btn-primary" @click="postAnswer(), getQuestion(), getResult()">Next</button>
      </div>
    </form>
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
    postAnswer() {
      const path = 'http://localhost:5000/answers'
      axios.post(path, {
        answer: this.selected
      })
      .then(function (response) {
        console.log(response);
      })
      this.i = this.i + 1
      if (this.i > 3) {
        this.i = 0
      }
    },
    getQuestion() {
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
      if (this.i == 4) {
        this.$router.push({name:'Result'})
      }
    }
  },
  created() {
    this.getQuestion();
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

.form-control {
  margin-top: 20px;
  margin-bottom: 20px;
}

</style>
