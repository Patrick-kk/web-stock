<template>
  <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b" router>
    <el-submenu index="1">
      <template slot="title">电影</template>
      <el-menu-item index="daily">实时票房</el-menu-item>
      <el-menu-item index="1-2">每日票房</el-menu-item>
      <el-menu-item index="1-3">月度票房</el-menu-item>
      <el-menu-item index="1-4">影院日度票房</el-menu-item>
    </el-submenu>
    <el-submenu index="2">
      <template slot="title">交易数据</template>
      <el-menu-item index="2-1">实时行情</el-menu-item>
      <el-menu-item index="2-2">历史行情</el-menu-item>
      <el-menu-item index="2-3">实时分笔</el-menu-item>
      <el-menu-item index="xxx">历史分笔</el-menu-item>
    </el-submenu>
    <el-menu-item index="3"><a href="https://www.ele.me" target="_blank">订单管理</a></el-menu-item>
    <el-submenu index="4">
      <template slot="title">龙虎榜</template>
      <el-menu-item index="/stock/toplist">每日龙虎榜</el-menu-item>
      <el-menu-item index="/stock/caplist">个股上榜</el-menu-item>
    </el-submenu>
  </el-menu>
</template>

<script>
export default {
  name: 'navigator',
  data () {
    return {
      activeIndex: '0'
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
    },
    setActiveIndex (index) {
      this.activeIndex = index
    }
  }
}
</script>
