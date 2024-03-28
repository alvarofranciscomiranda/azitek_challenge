import { createApp } from 'vue';
import 'bootstrap/dist/css/bootstrap.min.css';
import App from './App.vue';
import store from './store'; // Import your Vuex store

const app = createApp(App);
app.use(store)

app.directive('focus', {
  // Directive definition
  mounted(el) {
    el.focus()
  }
})

app.mount('#app')