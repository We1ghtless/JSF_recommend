<template>
  <div class="">
    <div class="container">
      <h1 class="">The quiz</h1>
      <p class="lead" id="text">Answer all the questions to receive a suggestion.</p>
    </div>
    <div class="container">
      <div class="form-group">
        <form class="needs-validation" novalidate>
          <div class="formBox" name="box">
            <h2>{{ question.question }}</h2>
            <div class="form-group">
              <select class="custom-select browser-default" v-model='selected' required>
                <option hidden value="" selected disabled>Select an option...</option>
                <option v-bind:key="answer" v-for="answer in question.answers" :value="answer">{{ answer }}</option>
              </select>
              <div class="invalid-feedback">Select answer</div>
            </div>
            <button type="button" class="btn btn-primary" @click="action()">Next</button>
          </div>
        </form>
      </div>
    </div>
    <div class="formBox" >
      <h1>Answers</h1>
      <ul class="list-group list-group-flush">
        <li class="list-group-item" v-bind:key="item" v-for="item in this.answers">
          <div class="container">
            {{ item }}
          </div>
        </li>
      </ul>
    </div>
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
      i: 0,
      answers: [],
    };
  },
  methods: {
    action() {
      if (this.selected != '') {
        this.postAnswer(),
        this.getQuestion(),
        this.getResult()
      }
    },
    postAnswer() {
      const path = 'http://localhost:5000/answers'
      axios.post(path, {
        answer: this.selected
      })
      .then(function (response) {
        console.log(response);
      })
      this.i = this.i + 1
      if (this.i > 4) {
        this.i = 0
      }
      if (this.answers.length < 4) {
        this.answers.push(this.selected)
      }
      if (this.answers.length >= 4) {
        this.answers = []
      }
      this.selected = ''
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
    },
    setName(value) {
      this.selected = value
      this.$v.selected.$touch()
    }
  },
  created() {
    this.getQuestion();
  },
}
</script>

<style scoped>
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
  text-align: center;
  max-width: 600px;
}

.form-control {
  margin-top: 20px;
  margin-bottom: 20px;
}

#text {
  text-align: center;
}

h1 {
  font-weight: 300;
  text-align: center;
}

h2 {
  font-weight: 400;
}

.list-group-item {
  border: 0px;
  background-color: rgba(255, 255, 255, 0.8);
}
</style>
