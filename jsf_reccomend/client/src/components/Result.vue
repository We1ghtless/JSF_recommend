<template lang="html">
  <div class="">
    <span>
      {{ result }}
    </span>
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
        alert(this.result)
      })
    }
  },
  created() {
    this.getResult()
  }

}
</script>

<style lang="css" scoped>
span {
  margin: auto;
  text-align: center;
}
</style>
