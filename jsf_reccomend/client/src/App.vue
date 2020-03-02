<template>
  <div id="app">
    <navBar/>
    <transition name="moveInUp">
    <router-view></router-view>
  </transition>
  </div>
</template>

<script>
import navBar from './components/Nav.vue'

export default {
  name: 'App',
  components: {
    'navBar': navBar
  }
}
</script>

<style>
#app {
}

.moveInUp-enter-active {
  opacity: 0;
  transition: opacity 1s ease-in;
}

.moveInUp-enter-active {
  animation: fadeIn 1s ease-in;
}
@keyframes fadeIn {
  0%{    opacity: 0;  }
  50%{    opacity: 0.5;  }
  100%{    opacity: 1;  }
}

.moveInUp-leave-active{  animation: moveInUp .3s ease-in;}@keyframes moveInUp{ 0%{  transform: translateY(0); }  100%{  transform: translateY(-400px); }}

</style>
