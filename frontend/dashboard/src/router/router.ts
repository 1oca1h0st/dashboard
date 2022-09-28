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
        }
    },
    {
        path: '/project',
        component: Base,
        children: [
            {
                path: 'create',
                component: ProjectCreate,
                name: 'project_create',
                meta: {
                    title: "创建项目",
                    main_title: "项目管理"
                }
            },
            {
                path: 'list',
                component: Base,
                name: 'project_list',
                meta: {
                    title: "查看项目",
                    main_title: "项目管理"
                }
            }
        ]
    },
    {
        path: '/poc',
        component: Base,
        children: [
            {
                path: 'nuclei',
                component: Base,
                name: 'poc_nuclei',
                meta: {
                    title: "nuclei",
                    main_title: "PoC管理"
                }
            },
            {
                path: 'kunpeng',
                component: Base,
                name: 'poc_kunpeng',
                meta: {
                    title: "Kunpeng",
                    main_title: "PoC管理"
                }
            }
        ]
    },
    {
        path: '/tools',
        component: Base,
        children: [
            {
                path: 'scan',
                component: Base,
                name: 'tools_scan',
                meta: {
                    title: "端口扫描",
                    main_title: "工具设置"
                }
            },
            {
                path: 'sub_domain_brute',
                component: Base,
                name: 'tools_sub_domain_brute',
                meta: {
                    title: "域名爆破",
                    main_title: "工具设置"
                }
            },
            {
                path: 'sub_dir_brute',
                component: Base,
                name: 'tools_sub_dir_brute',
                meta: {
                    title: "子目录爆破",
                    main_title: "工具设置"
                }
            },
            {
                path: 'crawler',
                component: Base,
                name: 'tools_crawler',
                meta: {
                    title: "主动爬虫",
                    main_title: "工具设置"
                }
            },
        ]
    },
    {
        path: '/code',
        name: 'code',
        component: Base,
        children: [
            {
                path: 'monitor',
                component: Base,
                name: 'code_monitor',
                meta: {
                    title: "Github监控",
                    main_title: "代码泄露"
                }
            },
            {
                path: 'setting',
                component: Base,
                name: 'code_setting',
                meta: {
                    title: "Github管理",
                    main_title: "代码泄露"
                }
            }
        ]
    },
    {
        path: '/notification',
        component: Base,
        children: [
            {
                path: 'webhook',
                component: Base,
                name: 'notification_webhook',
                meta: {
                    title: "Webhook",
                    main_title: "通知设置"
                }
            },
            {
                path: 'mail',
                component: Base,
                name: 'notification_mail',
                meta: {
                    title: "邮件设置",
                    main_title: "通知设置"
                }
            }
        ]
    },
    {
        path: '/settings',
        component: Base,
        children: [
            {
                path: 'users',
                component: Base,
                name: 'settings_users',
                meta: {
                    title: "用户管理",
                    main_title: "系统设置"
                }
            },
            {
                path: 'roles',
                component: Base,
                name: 'settings_roles',
                meta: {
                    title: "权限管理",
                    main_title: "系统设置"
                }
            },
            {
                path: 'logs',
                component: Base,
                name: 'settings_logs',
                meta: {
                    title: "日志管理",
                    main_title: "系统设置"
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
    routes: routes,
    linkActiveClass: "active"
})

router.beforeEach((to, from, next) => {
    document.title = (to.meta.title ? to.meta.title : '') + ' - Dashboard'
    // 判断登录
    if (to.meta.auth !== false) {
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