<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col-sm" v-bind:key="poo" v-for="poo in result" name="result">
        {{ poo }}
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
    getResult(){
      const path = 'http://localhost:5000/result'
      axios.get(path)
      .then((res) => {
        this.result = res.data
      })
    }
  },
  created() {
    this.getResult()
  }

}
</script>

<style lang="css" scoped>

</style>
