import Vue from 'vue'
import VueNumber from "vue-number-animation"
import App from './App.vue'
import VueRouter from 'vue-router'
import VueCookies from 'vue-cookies'
import axios from 'axios';
import Donut from 'vue-css-donut-chart';
import 'vue-css-donut-chart/dist/vcdonut.css';

Vue.use(VueCookies)
Vue.use(VueNumber)
Vue.use(VueRouter)
Vue.use(axios)
Vue.config.productionTip = false
Vue.use(Donut)

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
