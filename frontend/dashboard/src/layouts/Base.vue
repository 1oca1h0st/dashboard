<template>
  <div class="wrapper">
    <Navbar></Navbar>
    <div class="page-wrapper">
      <div class="container-fluid">
        <div class="page-header d-print-none">
          <div class="row align-items-center">
            <div class="col">
              <!-- Page pre-title -->
              <div class="page-pretitle">
                {{ $route.meta.main_title }}
              </div>
              <h2 class="page-title" id="page-title">
                {{ $route.meta.title }}
              </h2>
            </div>
          </div>
        </div>
      </div>
      <div class="page-body">
        <div class="container-fluid">
          <router-view></router-view>
        </div>
      </div>
      <Footer></Footer>
    </div>
  </div>
</template>

<script>
import Navbar from "@/layouts/Navbar.vue";
import Footer from "@/layouts/Footer.vue"

export default {
  name: "Base",
  components: {Footer, Navbar},
}
</script>

<style scoped>

</style>