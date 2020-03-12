<template lang="html">
  <div class="container-fluid">
    <main role="main" class="inner cover">
      <h1 class="cover-heading">JSF Recommend</h1>
      <p class="lead">JSF Recommend is a framework suggestion tool for developers. Take the quiz and find out what framework would best suit your next project!</p>
      <p class="lead">
        <a href="#" class="btn btn-lg btn-primary" @click="getQuiz()">Take the quiz</a>
      </p>
    </main>
  </div>
</template>

<script>
export default {
  methods: {
    getQuiz() {
      this.$router.push({name:'Form'})
    },
  }
}
</script>

<style lang="css" scoped>
div {
  text-align: center;
  margin: auto;
  padding: 40px;
}
</style>
