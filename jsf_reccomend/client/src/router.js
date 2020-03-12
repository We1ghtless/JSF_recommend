import Vue from 'vue';
import Router from 'vue-router';
import Form from './components/Form.vue';
import Result from './components/Result.vue';
import Home from './components/Home.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/form',
      name: 'Form',
      component: Form,
    },
    {
      path: '/result',
      name: 'Result',
      component: Result,
    }
  ],
});
