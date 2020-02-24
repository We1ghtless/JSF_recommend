<template>
  <div id="app">
    <Form />
  </div>
</template>

<script>
import Form from './components/Form'

export default {
  name: 'app',
  components: {
    Form,
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, Helvetica, sans-serif;
  line-height: 1.4;
}
</style>
