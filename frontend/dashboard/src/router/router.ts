import {createRouter, createWebHashHistory} from 'vue-router'
import jwt_decode from "jwt-decode"

const Base = () => import('../layouts/Base.vue')

const Login = () => import('../components/auth/Login.vue')
const ForgetPassword = () => import('../components/auth/ForgetPassword.vue')
const Register = () => import('../components/auth/Register.vue')
const HomePage = () => import('../components/HomePage.vue')
const ProjectCreate = () => import('../components/project/Create.vue')

const routes = [
    {
        path: '/',
        component: HomePage,
        name: 'home',
        meta: {
            title: "首页",
            auth: true
        }
    },
    {
        path: '/project',
        component: Base,
        children: [
            {
                path: 'create',
                component: ProjectCreate,
                meta: {
                    title: "创建项目"
                }
            }
        ]
    },
    {
        path: '/login',
        component: Login,
        name: 'login',
        meta: {
            title: '登录',
            auth: false
        }
    },
    {
        path: '/forget_password',
        component: ForgetPassword,
        meta: {
            title: "忘记密码",
            auth: false
        }
    },
    {
        path: '/register',
        component: Register,
        meta: {
            title: "注册",
            auth: false
        }
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes: routes
})

router.beforeEach((to, from, next) => {
    document.title = (to.meta.title ? to.meta.title : '') + ' - Dashboard'
    // 判断登录
    if (to.meta.auth) {
        const jwt = localStorage.getItem('token') || ""
        // 这里只是尝试解码了jwt，符合标准的就跳转，未真正验证token
        try {
            jwt_decode(jwt)
        } catch (e) {
            next({
                path: '/login',
                query: {
                    redirect: to.fullPath
                }
            })
        }
    }
    next()
})

export default router