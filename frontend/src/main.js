import Vue from 'vue'
import VueNumber from "vue-number-animation";
import App from './App.vue'
import VueRouter from 'vue-router'
import VueCookies from 'vue-cookies'

Vue.use(VueCookies)
Vue.use(VueNumber);
Vue.use(VueRouter)
Vue.config.productionTip = false

Vue.$cookies.config('7d')

const NotFoundComponent = { template: '<div>BAD</div>' }

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '*', component: NotFoundComponent }
  ]
});


new Vue({
  render: h => h(App),
  router
}).$mount('#app')
