<template>
  <div class="common-layout">
    <el-container>
      <el-aside>
        <img
          alt="UMEL"
          src="../assets/Logo_of_the_University_of_Melbourne.svg.png"
        />
        <el-menu
          active-text-color="#ffd04b"
          background-color="#003D86"
          class="el-menu-vertical-demo"
          default-active="home"
          text-color="#fff"
          width="270px"
          router
        >
          <el-menu-item index="home">
            <el-icon><HomeFilled /></el-icon>
            <span>Home</span>
          </el-menu-item>
          <el-menu-item index="map">
            <el-icon><LocationFilled /></el-icon>
            <span>Map</span>
          </el-menu-item>
          <el-menu-item index="statistics">
            <el-icon><Histogram /></el-icon>
            <span>Statistics</span>
          </el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Layout",
};
</script>

<style scoped>
img {
  width: 100%;
}
.common-layout {
  width: 100vw;
  height: 100vh;
  display: flex;
  position: relative;
}
.el-aside {
  background-color: #003d86;
  width: 200px;
}
.el-main {
  background-color: #c6d4e3;
}
</style>
