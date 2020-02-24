import Vue from 'vue';
import Router from 'vue-router';
import Form from './components/Form.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Form',
      component: Form,
    }
  ],
});
