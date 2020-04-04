<template>
  <div id="app">
    <navBar/>
    <transition name="fade" mode="out-in">
      <router-view></router-view>
    </transition>
    <foooter/>
  </div>
</template>

<script>
import navBar from './components/Nav.vue'
import foooter from './components/Footer.vue'

export default {
  name: 'App',
  components: {
    'navBar': navBar,
    'foooter': foooter
  }
}
</script>

<style>
#app {
  font-size: 100%;
  min-height: 100vh;
  width: 100%;
  background-color: #f7f7f7;
  background-image: url('./assets/bg.svg');
  background-repeat: no-repeat;
  background-size: cover;
}

router-view {

}

.fade-enter-active,
.fade-leave-active {
  transition-duration: 0.3s;
  transition-property: opacity;
  transition-timing-function: ease;
}

.fade-enter,
.fade-leave-active {
  opacity: 0
}
</style>
