<template>
  <div class="container">

    <div class="formBox" name="box">
        <h3>{{ msg }}</h3>
        <select class="form-control" name="">

        </select>
    </div>

    <transition name="fade" >
      <button type="button" class="btn btn-primary" v-on:click="show = !show, hide = !hide" v-if="hide">This</button>
    </transition>
    <transition name="fade" >
      <button type="button" class="btn btn-primary" v-if="show" v-on:click="hide = !hide, show = !show">That</button>
    </transition>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Form',
  data() {
    return {
      msg:'',
      show: false,
      hide: true,
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
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
  }
</style>
