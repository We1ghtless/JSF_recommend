<template lang="html">
  <nav class="navbar navbar-dark bg-dark navbar-expand">
    <a href="" @click="getHome()"><span class="navbar-brand mb-0"><h4>JSF Recommend</h4></span></a>
    <ul class="navbar-nav">
      <li nav-item active>
        <a class="nav-link" href="" @click="getQuiz()">Quiz <span class="sr-only">(current)</span></a>
      </li>
      <li nav-item active>
        <a class="nav-link" href="" @click="getAbout()">About <span class="sr-only">(current)</span></a>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  methods: {
    getQuiz() {
      this.$router.push({name:'Form'})
    },
    getAbout() {
      this.$router.push({name:'About'})
    },
    getHome() {
      this.$router.push({name:'Home'})
    }
  }
}
</script>

<style lang="css" scoped>

nav {
  margin-bottom: 4rem;
}

a {
  font-weight: 300;
}

h4 {
  font-weight: 300;
}


</style>
