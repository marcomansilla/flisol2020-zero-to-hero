import Vue from 'vue'
import './plugins/axios'
import App from './App.vue'
import router from './router'
import Buefy from 'buefy'
import './assets/scss/app.scss'

Vue.use(Buefy)

Vue.config.productionTip = false

new Vue({
  router,
  render: function (h) { return h(App) }
}).$mount('#app')
