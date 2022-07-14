import {createRouter, createWebHashHistory} from 'vue-router'

const Login = () => import('../components/auth/Login.vue')
const ForgetPassword = () => import('../components/auth/ForgetPassword.vue')
const Register = () => import('../components/auth/Register.vue')
const Test1 = () => import('../components/Test1.vue')
const Test2 = () => import('../components/Test2.vue')
const HomePage = () => import('../components/HomePage.vue')

const routes = [
    {
        path: '/',
        component: Login
    },
    {
        path: '/test1',
        component: Test1
    },
    {
        path: '/test2',
        component: Test2
    },
    {
        path: '/forget_password',
        component: ForgetPassword
    },
    {
        path: '/register',
        component: Register
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes: routes
})

export default router