<template lang="html">
  <div class="container">
    <h1>About</h1>
    <p class="lead">This web-app is a result of planning, research and development for the requirements of an Edinburgh Napier University Honors project.</p>

    <div class="card">
      <div class="row">
        <div class="col-md-3">
          <img class="card-img-left" src="../assets/img2.jpeg" alt="Card image cap">
        </div>
        <div class="col-md px-3">
          <div class="card-block px-3">
            <h4 class="card-title">From the Developer</h4>
            <p class="card-text">Hi, my name is Peter. This web-app is the result of my Web design and development studies at Edinburgh Napier University and is the deliverable for my project which focused on JavaScript front-end frameworks in an attempt to compare their strengths and weaknesses to help developers better understand their differences and benefits. </p>
            <p class="card-text">To find my research paper as well as the design and development report please visit my <a target="_blank" href="https://github.com/We1ghtless/JSF_recommend">github</a>.</p>
          </div>
        </div>
      </div>
    </div>
    <img src="/assets/img2.jpg" alt="">
  </div>
</template>

<script>
export default {
}
</script>

<style lang="css" scoped>
h1 {
  font-weight: 300;
}

img {
  width: 100%;
  height: auto;
  padding: 10px;

}

.card-block {
  padding: 20px;
}
</style>
