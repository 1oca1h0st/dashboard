<template>
  <div class="wrapper">
    <Navbar></Navbar>
    <div class="page-wrapper">
      <div class="container-fluid">
        <!-- Page title -->
        <div class="page-header d-print-none">
          <div class="row align-items-center">
            <div class="col">
              <!-- Page pre-title -->
              <div class="page-pretitle">
                Overview
              </div>
              <h2 class="page-title">
                总览视图
              </h2>
            </div>
            <!-- Page title actions -->
            <div class="col-auto ms-auto d-print-none">
              <div class="btn-list">
                  <span class="d-none d-sm-inline">
                  </span>
                <a href="#" class="btn btn-primary d-none d-sm-inline-block" data-bs-toggle="modal"
                   data-bs-target="#modal-report">
                  <!-- Download SVG icon from http://tabler-icons.io/i/plus -->
                  <svg xmlns="http://www.w3.org/2000/svg" class="icon" width="24" height="24" viewBox="0 0 24 24"
                       stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round"
                       stroke-linejoin="round">
                    <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                    <line x1="12" y1="5" x2="12" y2="19"/>
                    <line x1="5" y1="12" x2="19" y2="12"/>
                  </svg>
                  创建新任务
                </a>
                <a href="#" class="btn btn-primary d-sm-none btn-icon" data-bs-toggle="modal"
                   data-bs-target="#modal-report" aria-label="Create new report">
                  <!-- Download SVG icon from http://tabler-icons.io/i/plus -->
                  <svg xmlns="http://www.w3.org/2000/svg" class="icon" width="24" height="24" viewBox="0 0 24 24"
                       stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round"
                       stroke-linejoin="round">
                    <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                    <line x1="12" y1="5" x2="12" y2="19"/>
                    <line x1="5" y1="12" x2="19" y2="12"/>
                  </svg>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="page-body">
        <div class="container-fluid">
          <div class="row row-deck row-cards">
            <div class="col-sm-6 col-lg-3">
              <div class="card">
                <div class="card-body">
                  <div class="d-flex align-items-center">
                    <div class="subheader">域名数量</div>
                    <div class="ms-auto lh-1">
                      <div class="dropdown">
                        <a class="dropdown-toggle text-muted" href="#" data-bs-toggle="dropdown" aria-haspopup="true"
                           aria-expanded="false">Last 7 days</a>
                        <div class="dropdown-menu dropdown-menu-end">
                          <a class="dropdown-item active" href="#">Last 7 days</a>
                          <a class="dropdown-item" href="#">Last 30 days</a>
                          <a class="dropdown-item" href="#">Last 3 months</a>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="h1 mb-3">75%</div>
                  <div class="d-flex mb-2">
                    <div>Conversion rate</div>
                    <div class="ms-auto">
                        <span class="text-green d-inline-flex align-items-center lh-1">
                          7% <!-- Download SVG icon from http://tabler-icons.io/i/trending-up -->
                          <svg xmlns="http://www.w3.org/2000/svg" class="icon ms-1" width="24" height="24"
                               viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
                               stroke-linecap="round" stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z"
                                                                                    fill="none"/><polyline
                              points="3 17 9 11 13 15 21 7"/><polyline points="14 7 21 7 21 14"/></svg>
                        </span>
                    </div>
                  </div>
                  <div class="progress progress-sm">
                    <div class="progress-bar bg-blue" style="width: 75%" role="progressbar" aria-valuenow="75"
                         aria-valuemin="0" aria-valuemax="100">
                      <span class="visually-hidden">75% Complete</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-sm-6 col-lg-3">
              <div class="card">
                <div class="card-body">
                  <div class="d-flex align-items-center">
                    <div class="subheader">IP数量</div>
                    <div class="ms-auto lh-1">
                      <div class="dropdown">
                        <a class="dropdown-toggle text-muted" href="#" data-bs-toggle="dropdown" aria-haspopup="true"
                           aria-expanded="false">Last 7 days</a>
                        <div class="dropdown-menu dropdown-menu-end">
                          <a class="dropdown-item active" href="#">Last 7 days</a>
                          <a class="dropdown-item" href="#">Last 30 days</a>
                          <a class="dropdown-item" href="#">Last 3 months</a>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="d-flex align-items-baseline">
                    <div class="h1 mb-0 me-2">$4,300</div>
                    <div class="me-auto">
                        <span class="text-green d-inline-flex align-items-center lh-1">
                          8% <!-- Download SVG icon from http://tabler-icons.io/i/trending-up -->
                          <svg xmlns="http://www.w3.org/2000/svg" class="icon ms-1" width="24" height="24"
                               viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
                               stroke-linecap="round" stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z"
                                                                                    fill="none"/><polyline
                              points="3 17 9 11 13 15 21 7"/><polyline points="14 7 21 7 21 14"/></svg>
                        </span>
                    </div>
                  </div>
                </div>
                <div id="chart-revenue-bg" class="chart-sm"></div>
              </div>
            </div>
            <div class="col-sm-6 col-lg-3">
              <div class="card">
                <div class="card-body">
                  <div class="d-flex align-items-center">
                    <div class="subheader">端口数量</div>
                    <div class="ms-auto lh-1">
                      <div class="dropdown">
                        <a class="dropdown-toggle text-muted" href="#" data-bs-toggle="dropdown" aria-haspopup="true"
                           aria-expanded="false">Last 7 days</a>
                        <div class="dropdown-menu dropdown-menu-end">
                          <a class="dropdown-item active" href="#">Last 7 days</a>
                          <a class="dropdown-item" href="#">Last 30 days</a>
                          <a class="dropdown-item" href="#">Last 3 months</a>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="d-flex align-items-baseline">
                    <div class="h1 mb-3 me-2">6,782</div>
                    <div class="me-auto">
                        <span class="text-yellow d-inline-flex align-items-center lh-1">
                          0% <!-- Download SVG icon from http://tabler-icons.io/i/minus -->
                          <svg xmlns="http://www.w3.org/2000/svg" class="icon ms-1" width="24" height="24"
                               viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
                               stroke-linecap="round" stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z"
                                                                                    fill="none"/><line x1="5" y1="12"
                                                                                                       x2="19" y2="12"/></svg>
                        </span>
                    </div>
                  </div>
                  <div id="chart-new-clients" class="chart-sm"></div>
                </div>
              </div>
            </div>
            <div class="col-sm-6 col-lg-3">
              <div class="card">
                <div class="card-body">
                  <div class="d-flex align-items-center">
                    <div class="subheader">漏洞数量</div>
                    <div class="ms-auto lh-1">
                      <div class="dropdown">
                        <a class="dropdown-toggle text-muted" href="#" data-bs-toggle="dropdown" aria-haspopup="true"
                           aria-expanded="false">Last 7 days</a>
                        <div class="dropdown-menu dropdown-menu-end">
                          <a class="dropdown-item active" href="#">Last 7 days</a>
                          <a class="dropdown-item" href="#">Last 30 days</a>
                          <a class="dropdown-item" href="#">Last 3 months</a>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="d-flex align-items-baseline">
                    <div class="h1 mb-3 me-2">2,986</div>
                    <div class="me-auto">
                        <span class="text-green d-inline-flex align-items-center lh-1">
                          4% <!-- Download SVG icon from http://tabler-icons.io/i/trending-up -->
                          <svg xmlns="http://www.w3.org/2000/svg" class="icon ms-1" width="24" height="24"
                               viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
                               stroke-linecap="round" stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z"
                                                                                    fill="none"/><polyline
                              points="3 17 9 11 13 15 21 7"/><polyline points="14 7 21 7 21 14"/></svg>
                        </span>
                    </div>
                  </div>
                  <div id="chart-active-users" class="chart-sm"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <Footer></Footer>
    </div>
  </div>
  <NewTask></NewTask>
</template>

<script>
import Navbar from "@/layouts/Navbar.vue";
import Footer from "@/layouts/Footer.vue";
import NewTask from "@/layouts/modal/NewTask.vue";
import VueApexcharts from "vue3-apexcharts"

export default {
  name: "HomePage",
  components: {NewTask, Footer, Navbar, VueApexcharts},
  data() {
    return {
      logo: "img/logo-white.svg"
    }
  },
  mounted() {
    let apexcharts = document.createElement('script')
    apexcharts.type = "text/javascript"
    apexcharts.src = "./public/apexcharts/apexcharts.min.js"

    let homepage = document.createElement('script')
    homepage.type = "text/javascript"
    homepage.src = "./src/js/homepage.js"

    document.body.appendChild(apexcharts)

    this.$nextTick(() => {
      document.body.appendChild(homepage)
    })
  }
}
</script>

<style scoped>

</style>