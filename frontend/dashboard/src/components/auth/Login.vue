<style scoped>
</style>

<template>
  <div class="page page-center">
    <div class="container-tight py-4">
      <div class="text-center mb-4">
        <a href="." class="navbar-brand navbar-brand-autodark"><img :src=logo height="36" alt=""></a>
      </div>
      <div class="card card-md">
        <div class="card-body">
          <h2 class="card-title text-center mb-4">系统登录</h2>
          <div class="mb-3">
            <label class="form-label">用户名</label>
            <input v-model="username" type="text" name="username" class="form-control"
                   placeholder="请输入用户名...">
          </div>
          <div class="mb-2">
            <label class="form-label">
              密码
              <span class="form-label-description">
                <router-link to="forget_password">忘记密码</router-link>
                </span>
            </label>
            <div class="input-group input-group-flat">
              <input v-model="password" type="password" name="password" class="form-control" placeholder="Password"
                     autocomplete="off" @keyup.enter="submit">
              <span class="input-group-text">
                  <a href="#" class="link-secondary" title="Show password" data-bs-toggle="tooltip"><!-- Download SVG icon from http://tabler-icons.io/i/eye -->
                    <svg xmlns="http://www.w3.org/2000/svg" class="icon" width="24" height="24" viewBox="0 0 24 24"
                         stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round"
                         stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                      <circle cx="12" cy="12" r="2"/><path
                          d="M22 12c-2.667 4.667 -6 7 -10 7s-7.333 -2.333 -10 -7c2.667 -4.667 6 -7 10 -7s7.333 2.333 10 7"/></svg>
                  </a>
                </span>
            </div>
          </div>
          <div class="mb-2">
            <label class="form-check">
              <input type="checkbox" class="form-check-input"/>
              <span class="form-check-label">记住我</span>
            </label>
          </div>
          <div class="form-footer">
            <button type="submit" class="btn btn-primary w-100" v-on:click="submit">登录</button>
          </div>
        </div>
      </div>
      <div class="text-center text-muted mt-3">
        还没有账号？
        <router-link to="register" tabindex="-1">点我注册</router-link>
      </div>
    </div>
  </div>
  <!-- Libs JS -->
  <!-- Tabler Core -->
</template>

<script>
import qs from "qs";
import request from "../../util/request"
import router from "@/router/router.ts";

export default {
  name: "Login",
  data() {
    return {
      logo: "img/logo.svg",
      username: "",
      password: ""
    }
  },
  mounted() {
    document.getElementsByTagName('body')[0].className = "border-top-wide border-primary d-flex flex-column"
    document.getElementById('app').className = "page"
  },
  beforeUnmount() {
    document.body.removeAttribute('class')
  },
  methods: {
    submit() {
      request({
        url: "/users/login",
        method: "post",
        data: qs.stringify({
          username: this.username,
          password: this.password
        })
      }).then((res) => {
        if (res.status === 200) {
          localStorage.setItem("token", res.data.access_token)
          router.push('/')
        } else if (res.status === 401) {
          alert(res.data.detail)
        }
      })
    }
  }
}</script>