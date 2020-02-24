<template lang="html">
  <div class="block">
    <h1>Form</h1>

    <label for="">New or existing project</label>
    <select class="" name="">
      <option value="New">New</option>
      <option value="Existing">Existing</option>
    </select>

    <form class="" action="" method="">
      <label for="website-type">Website Type</label>
      <select class="" name="website-type">
        <option value="" disabled selected>Select your option</option>
        <option value="blog">Blog</option>
        <option value="corporate">Corporate</option>
        <option value="ecommerce">Ecommerce</option>
        <option value="portfolio">Portfolio</option>
        <option value="brochure">Brochure</option>
        <option value="crowdfunding">Crowdfunding</option>
        <option value="news">News or Magazine</option>
        <option value="streaming">Tv or Video Streaming</option>
        <option value="educational">Educational</option>
        <option value="portal">Portal</option>
        <option value="wiki">Wiki or community forum</option>
      </select>

      <label for="">Experience with Javascript</label>
      <select class="" name="">
        <option value="beginner">Beginner</option>
        <option value="intermediate">Intermediate</option>
        <option value="expert">Expert</option>
      </select>

      <label for="">Project scope</label>
      <select class="" name="">
        <option value="small">Small/personal project</option>
        <option value="medium">Medium/small business project</option>
        <option value="large">Large enterprise scale project</option>
      </select>

      <button type="button" name="button">Submit</button>
    </form>


  </div>
</template>

<script>


export default {

}

</script>

<style lang="css" scoped>

</style>
