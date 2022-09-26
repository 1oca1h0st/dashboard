import {createApp} from 'vue'
import router from './router/router'
import App from './App.vue'

createApp(App).use(router).mount('#app')
router.beforeEach(async (to, from, next) => {
    document.title = (to.meta.title ? to.meta.title : '') + ' - Dashboard'
})