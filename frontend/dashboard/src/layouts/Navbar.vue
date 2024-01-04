<template>
  <aside class="navbar navbar-vertical navbar-expand-lg navbar-dark">
    <div class="container-fluid">
      <h1 class="navbar-brand navbar-brand-autodark">
        <router-link :to="{name:'home'}">
          <img :src=logo width="110" height="32" alt="Tabler" class="navbar-brand-image">
        </router-link>
      </h1>
      <div class="collapse navbar-collapse" id="navbar-menu">
        <ul class="navbar-nav pt-lg-3">
          <li class="nav-item" id="li-home">
            <router-link :to="{name:'home'}" class="nav-link">
              <span class="nav-link-icon d-md-none d-lg-inline-block">
                    <svg xmlns="http://www.w3.org/2000/svg" class="icon" width="24" height="24" viewBox="0 0 24 24"
                         stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round"
                         stroke-linejoin="round">
                      <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                      <polyline points="5 12 3 12 12 3 21 12 19 12"/>
                      <path d="M5 12v7a2 2 0 0 0 2 2h10a2 2 0 0 0 2 -2v-7"/>
                      <path d="M9 21v-6a2 2 0 0 1 2 -2h2a2 2 0 0 1 2 2v6"/>
                    </svg>
              </span>
              <span class="nav-link-title">
                    首页
                  </span>
            </router-link>
          </li>
          <li class="nav-item" id="li-project">
            <a class="nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown"
               data-bs-auto-close="false" role="button" aria-expanded="true">
                  <span class="nav-link-icon d-md-none d-lg-inline-block">
                    <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-chart-treemap"
                         width="24"
                         height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
                         stroke-linecap="round" stroke-linejoin="round">
                      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                      <rect x="4" y="4" width="16" height="16" rx="2"></rect>
                       <path d="M12 4v16"></path>
                       <path d="M4 15h8"></path>
                       <path d="M12 12h8"></path>
                       <path d="M16 12v8"></path>
                       <path d="M16 16h4"></path>
                    </svg>
                  </span>
              <span class="nav-link-title">
                    项目管理
                  </span>
            </a>
            <div class="dropdown-menu" id="div-project">
              <div class="dropdown-menu-columns">
                <div class="dropdown-menu-column">
                  <router-link :to="{name:'project_create'}" class="dropdown-item">
                    新建项目
                  </router-link>
                  <router-link :to="{name:'project_list'}" class="dropdown-item">查看项目</router-link>
                </div>
              </div>
            </div>
          </li>
          <li class="nav-item">
            <a class="nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown"
               data-bs-auto-close="false" role="button" aria-expanded="false">
                  <span class="nav-link-icon d-md-none d-lg-inline-block">
                    <svg xmlns="http://www.w3.org/2000/svg" class="icon" width="24" height="24" viewBox="0 0 24 24"
                         stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round"
                         stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><polyline
                        points="12 3 20 7.5 20 16.5 12 21 4 16.5 4 7.5 12 3"/><line x1="12" y1="12" x2="20" y2="7.5"/>
                      <line x1="12" y1="12" x2="12" y2="21"/><line x1="12" y1="12" x2="4" y2="7.5"/>
                      <line x1="16" y1="5.25" x2="8" y2="9.75"/></svg>
                  </span>
              <span class="nav-link-title">
                    资产管理
                  </span>
            </a>
            <div class="dropdown-menu">
              <div class="dropdown-menu-columns">
                <div class="dropdown-menu-column">
                  <a class="dropdown-item" href="./empty.html">
                    Empty page
                  </a>
                  <a class="dropdown-item" href="./accordion.html">
                    Accordion
                  </a>
                  <a class="dropdown-item" href="./blank.html">
                    Blank page
                  </a>
                  <a class="dropdown-item" href="./buttons.html">
                    Buttons
                  </a>
                  <a class="dropdown-item" href="./cards.html">
                    Cards
                  </a>
                  <a class="dropdown-item" href="./cards-masonry.html">
                    Cards Masonry
                  </a>
                  <a class="dropdown-item" href="./colors.html">
                    Colors
                  </a>
                  <a class="dropdown-item" href="./dropdowns.html">
                    Dropdowns
                  </a>
                  <a class="dropdown-item" href="./icons.html">
                    Icons
                  </a>
                  <a class="dropdown-item" href="./modals.html">
                    Modals
                  </a>
                  <a class="dropdown-item" href="./maps.html">
                    Maps
                  </a>
                  <a class="dropdown-item" href="./map-fullsize.html">
                    Map fullsize
                  </a>
                  <a class="dropdown-item" href="./maps-vector.html">
                    Vector maps
                  </a>
                </div>
                <div class="dropdown-menu-column">
                  <a class="dropdown-item" href="./navigation.html">
                    Navigation
                  </a>
                  <a class="dropdown-item" href="./charts.html">
                    Charts
                  </a>
                  <a class="dropdown-item" href="./pagination.html">
                    Pagination
                  </a>
                  <a class="dropdown-item" href="./skeleton.html">
                    Skeleton
                  </a>
                  <a class="dropdown-item" href="./tabs.html">
                    Tabs
                  </a>
                  <a class="dropdown-item" href="./tables.html">
                    Tables
                  </a>
                  <a class="dropdown-item" href="./carousel.html">
                    Carousel
                  </a>
                  <a class="dropdown-item" href="./lists.html">
                    Lists
                  </a>
                  <a class="dropdown-item" href="./typography.html">
                    Typography
                  </a>
                  <a class="dropdown-item" href="./offcanvas.html">
                    Offcanvas
                  </a>
                  <a class="dropdown-item" href="./markdown.html">
                    Markdown
                  </a>
                  <div class="dropend">
                    <a class="dropdown-item dropdown-toggle" href="#sidebar-authentication" data-bs-toggle="dropdown"
                       data-bs-auto-close="false" role="button" aria-expanded="false">
                      Authentication
                    </a>
                    <div class="dropdown-menu">
                      <a href="./sign-in.html" class="dropdown-item">Sign in</a>
                      <a href="./sign-up.html" class="dropdown-item">Sign up</a>
                      <a href="./forgot-password.html" class="dropdown-item">Forgot password</a>
                      <a href="./terms-of-service.html" class="dropdown-item">Terms of service</a>
                      <a href="./auth-lock.html" class="dropdown-item">Lock screen</a>
                    </div>
                  </div>
                  <div class="dropend">
                    <a class="dropdown-item dropdown-toggle" href="#sidebar-error" data-bs-toggle="dropdown"
                       data-bs-auto-close="false" role="button" aria-expanded="false">
                      Error pages
                    </a>
                    <div class="dropdown-menu">
                      <a href="./error-404.html" class="dropdown-item">404 page</a>
                      <a href="./error-500.html" class="dropdown-item">500 page</a>
                      <a href="./error-maintenance.html" class="dropdown-item">Maintenance page</a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="">
                  <span class="nav-link-icon d-md-none d-lg-inline-block">
                    <svg xmlns="http://www.w3.org/2000/svg" class="icon" width="24" height="24" viewBox="0 0 24 24"
                         stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round"
                         stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><polyline
                        points="9 11 12 14 20 6"/><path
                        d="M20 12v6a2 2 0 0 1 -2 2h-12a2 2 0 0 1 -2 -2v-12a2 2 0 0 1 2 -2h9"/></svg>
                  </span>
              <span class="nav-link-title">
                    任务管理
                  </span>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown"
               data-bs-auto-close="false" role="button" aria-expanded="false">
                  <span class="nav-link-icon d-md-none d-lg-inline-block">
                    <svg xmlns="http://www.w3.org/2000/svg" class="icon" width="24" height="24" viewBox="0 0 24 24"
                         stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round"
                         stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path
                        d="M12 17.75l-6.172 3.245l1.179 -6.873l-5 -4.867l6.9 -1l3.086 -6.253l3.086 6.253l6.9 1l-5 4.867l1.179 6.873z"/>
                    </svg>
                  </span>
              <span class="nav-link-title">
                    Poc管理
                  </span>
            </a>
            <div class="dropdown-menu">
              <div class="dropdown-menu-columns">
                <div class="dropdown-menu-column">
                  <router-link to="/poc/nuclei" class="dropdown-item">Nuclei</router-link>
                  <router-link to="/poc/kunpeng" class="dropdown-item">Kunpeng</router-link>
                </div>
              </div>
            </div>
          </li>
          <li class="nav-item">
            <a class="nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown"
               data-bs-auto-close="false" role="button" aria-expanded="true">
                  <span class="nav-link-icon d-md-none d-lg-inline-block">
                    <svg xmlns="http://www.w3.org/2000/svg" class="icon" width="24" height="24" viewBox="0 0 24 24"
                         stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round"
                         stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                      <rect x="4" y="4"
                            width="6"
                            height="5"
                            rx="2"/><rect
                          x="4" y="13" width="6" height="7" rx="2"/><rect x="14" y="4" width="6" height="7" rx="2"/><rect
                          x="14" y="15" width="6" height="5" rx="2"/></svg>
                  </span>
              <span class="nav-link-title">
                    工具设置
                  </span>
            </a>
            <div class="dropdown-menu">
              <div class="dropdown-menu-columns">
                <div class="dropdown-menu-column">
                  <router-link :to="{name:'tools_sub_domain_brute'}" class="dropdown-item">域名爆破</router-link>
                  <router-link :to="{name:'tools_scan'}" class="dropdown-item">端口扫描</router-link>
                  <router-link :to="{name:'tools_sub_dir_brute'}" class="dropdown-item">子目录爆破</router-link>
                  <router-link :to="{name:'tools_crawler'}" class="dropdown-item">主动爬虫</router-link>
                </div>
              </div>
            </div>
          </li>
          <li class="nav-item" id="li-code">
            <a class="nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown"
               data-bs-auto-close="false" role="button" aria-expanded="true">
                  <span class="nav-link-icon d-md-none d-lg-inline-block">
                    <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-brand-github" width="24"
                         height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
                         stroke-linecap="round" stroke-linejoin="round">
                      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                      <path
                          d="M9 19c-4.3 1.4 -4.3 -2.5 -6 -3m12 5v-3.5c0 -1 .1 -1.4 -.5 -2c2.8 -.3 5.5 -1.4 5.5 -6a4.6 4.6 0 0 0 -1.3
                          -3.2a4.2 4.2 0 0 0 -.1 -3.2s-1.1 -.3 -3.5 1.3a12.3 12.3 0 0 0 -6.2 0c-2.4 -1.6 -3.5 -1.3 -3.5 -1.3a4.2 4.2 0 0 0
                          -.1 3.2a4.6 4.6 0 0 0 -1.3 3.2c0 4.6 2.7 5.7 5.5 6c-.6 .6 -.6 1.2 -.5 2v3.5"></path>
                    </svg>
                  </span>
              <span class="nav-link-title">
                    代码泄露
                  </span>
            </a>
            <div class="dropdown-menu" id="div-code">
              <div class="dropdown-menu-columns">
                <div class="dropdown-menu-column">
                  <router-link :to="{name:'code_monitor'}" class="dropdown-item">Github监控</router-link>
                  <router-link :to="{name:'code_setting'}" class="dropdown-item">Github管理</router-link>
                </div>
              </div>
            </div>
          </li>
          <li class="nav-item">
            <a class="nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown"
               data-bs-auto-close="false" role="button" aria-expanded="true">
                  <span class="nav-link-icon d-md-none d-lg-inline-block">
                    <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-bell-ringing" width="24"
                         height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
                         stroke-linecap="round" stroke-linejoin="round">
                      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                      <path
                          d="M10 5a2 2 0 0 1 4 0a7 7 0 0 1 4 6v3a4 4 0 0 0 2 3h-16a4 4 0 0 0 2 -3v-3a7 7 0 0 1 4 -6"></path>
                      <path d="M9 17v1a3 3 0 0 0 6 0v-1"></path>
                      <path d="M21 6.727a11.05 11.05 0 0 0 -2.794 -3.727"></path>
                      <path d="M3 6.727a11.05 11.05 0 0 1 2.792 -3.727"></path>
                    </svg>
                  </span>
              <span class="nav-link-title">
                    通知设置
                  </span>
            </a>
            <div class="dropdown-menu">
              <div class="dropdown-menu-columns">
                <div class="dropdown-menu-column">
                  <router-link :to="{name:'notification_webhook'}" class="dropdown-item">Webhook</router-link>
                  <router-link :to="{name:'notification_mail'}" class="dropdown-item">邮件设置</router-link>
                </div>
              </div>
            </div>
          </li>
          <li class="nav-item">
            <a class="nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown"
               data-bs-auto-close="false" role="button" aria-expanded="true">
                  <span class="nav-link-icon d-md-none d-lg-inline-block">
                    <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-settings" width="24"
                         height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
                         stroke-linecap="round" stroke-linejoin="round">
                      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                      <path
                          d="M10.325 4.317c.426 -1.756 2.924 -1.756 3.35 0a1.724 1.724 0 0 0 2.573 1.066c1.543 -.94 3.31 .826 2.37 2.37a1.724 1.724 0 0 0 1.065 2.572c1.756 .426 1.756 2.924 0 3.35a1.724 1.724 0 0 0 -1.066 2.573c.94 1.543 -.826 3.31 -2.37 2.37a1.724 1.724 0 0 0 -2.572 1.065c-.426 1.756 -2.924 1.756 -3.35 0a1.724 1.724 0 0 0 -2.573 -1.066c-1.543 .94 -3.31 -.826 -2.37 -2.37a1.724 1.724 0 0 0 -1.065 -2.572c-1.756 -.426 -1.756 -2.924 0 -3.35a1.724 1.724 0 0 0 1.066 -2.573c-.94 -1.543 .826 -3.31 2.37 -2.37c1 .608 2.296 .07 2.572 -1.065z"></path>
                      <circle cx="12" cy="12" r="3"></circle>
                    </svg>
                  </span>
              <span class="nav-link-title">
                    系统设置
                  </span>
            </a>
            <div class="dropdown-menu">
              <div class="dropdown-menu-columns">
                <div class="dropdown-menu-column">
                  <router-link :to="{name:'settings_users'}" class="dropdown-item">用户管理</router-link>
                  <router-link :to="{name:'settings_roles'}" class="dropdown-item">权限管理</router-link>
                  <router-link :to="{name:'settings_logs'}" class="dropdown-item">日志管理</router-link>
                </div>
              </div>
            </div>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">
                  <span class="nav-link-icon d-md-none d-lg-inline-block">
                    <svg xmlns="http://www.w3.org/2000/svg" class="icon" width="24" height="24" viewBox="0 0 24 24"
                         stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round"
                         stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path
                        d="M14 3v4a1 1 0 0 0 1 1h4"/><path
                        d="M17 21h-10a2 2 0 0 1 -2 -2v-14a2 2 0 0 1 2 -2h7l5 5v11a2 2 0 0 1 -2 2z"/>
                      <line x1="9" y1="9"
                            x2="10"
                            y2="9"/><line
                          x1="9" y1="13" x2="15" y2="13"/><line x1="9" y1="17" x2="15" y2="17"/></svg>
                  </span>
              <span class="nav-link-title">
                    Documentation
                  </span>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </aside>
</template>

<script>
export default {
  name: "Navbar",
  data() {
    return {
      logo: "img/logo-white.svg"
    }
  },
  methods: {
    getMe: function () {
      console.log("111")
    }
  },
  created() {
    this.getMe()
  }
}
</script>

<style scoped>
.dropdown-menu-column .dropdown-item {
  padding-left: 2rem;
}
</style>