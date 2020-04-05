<template lang="html">
  <div class="glass">
    <div class="container-fluid">
      <main role="main" class="inner cover">
        <h1 class="cover-heading">Welcome to JSF Recommend</h1>
        <p class="lead">JSF Recommend is a front-end JavaScript framework suggestion tool for developers. Using both academic and practitioner research, the software makes a recommendation in conjunction with your response. Take the quiz and find out what framework would best suit your next project!</p>
        <p class="lead">
          <a href="" class="btn btn-lg btn-primary" @click="getQuiz()">Take the quiz</a>
        </p>
      </main>
    </div>
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


.container-fluid {
  /* border-bottom: 1px solid;
  border-color: #dedcd7; */
}

main {
  text-align: center;
  margin: auto;
  padding: 40px;
  max-width: 80%;
  height: 100%;
}

.link {
  color: black;
  text-decoration: underline;
}

#bottom {

}

h1 {
  font-weight: 300;
}

p {
  margin-bottom: 4px;
}

.btn {
  margin-top: 1rem;
}
</style>
