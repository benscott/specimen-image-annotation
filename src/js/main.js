import Vue from 'vue'
Vue.use(require('vue-resource'));

import App from './components/App.vue'

// Set up jQuery and auxiliary libs 
window.$ = window.jQuery = require('jquery');

import Multiselect from 'vue-multiselect'

// register globally
Vue.component('multiselect', Multiselect);

// Set up config
const vueConfig = require('vue-config');
Vue.use(vueConfig, require('./config.js'));

// Set up fontawesome
import 'vue-awesome/icons';
const Icon = require('vue-awesome/components/Icon.vue');
Vue.component('icon', Icon);

new Vue({
    el: '#app',
    template: '<App/>',
    components: { App }
});
