import {createRouter, createWebHashHistory} from 'vue-router'

const App = () => import('../App.vue')
const Test1 = () => import('../components/Test1.vue')
const Test2 = () => import('../components/Test2.vue')

const routes = [
    {
        path: '/',
        component: App
    },
    {
        path: '/test1',
        component: Test1
    },
    {
        path: '/test2',
        component: Test2
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes: routes
})

export default router