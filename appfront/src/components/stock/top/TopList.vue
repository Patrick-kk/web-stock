<template>
    <el-container>
    <el-header><navigator ref='nav'></navigator></el-header>
      <el-main>
        <el-container>
          <el-header class="query">
            <el-date-picker v-model="date" align="left" type="date" placeholder="选择日期" :picker-options="pickerOptions">
            </el-date-picker>
            <el-button type="primary" icon="el-icon-search" @click="search(date)">搜索</el-button>
          </el-header>
          <el-main>
            <el-row>
                <el-table v-loading="loading" element-loading-text="拼命加载中" element-loading-spinner="el-icon-loading" element-loading-background="rgba(0,0,0,0.8)" :data="topList" style="width: 100%" border max-height="800" :row-class-name="tableRowClassName" :default-sort="{prop:'pchange', order: 'descending'}">
                    <el-table-column fixed prop="code" label="代码" sortable min-width="100"></el-table-column>
                    <el-table-column fixed prop="name" label="名称" sortable min-width="110"></el-table-column>
                    <el-table-column prop="pchange" label="当日涨跌幅" sortable min-width="120"></el-table-column>
                    <el-table-column prop="amount" label="成交额(万)" min-width="100"></el-table-column>
                    <el-table-column prop="buy" label="买入额(万)" min-width="100"></el-table-column>
                    <el-table-column prop="bratio" label="买入比例" min-width="100"></el-table-column>
                    <el-table-column prop="sell" label="卖出额(万)" min-width="100"></el-table-column>
                    <el-table-column prop="sratio" label="卖出占比" min-width="100"></el-table-column>
                    <el-table-column prop="reason" label="上榜原因" min-width="300"></el-table-column>
                    <el-table-column prop="date" label="日期" sortable min-width="120"></el-table-column>
                </el-table>
            </el-row>
          </el-main>
        </el-container>
      </el-main>
    </el-container>
</template>

<script>
import navigator from '@/components/navigator.vue'
export default {
  name: 'TopList',
  data () {
    return {
      loading: false,
      input: '',
      topList: [{'code': '600', 'pchange': '123'}, {'pchange': '-34'}],
      pickerOptions: {
        disabledDate (time) {
          return time.getTime() > Date.now()
        },
        shortcuts: [{
          text: '今天',
          onClick (picker) {
            picker.$emit('pick', new Date())
          }
        }, {
          text: '昨天',
          onClick (picker) {
            const date = new Date()
            date.setTime(date.getTime() - 3600 * 1000 * 24)
            picker.$emit('pick', date)
          }
        }, {
          text: '一周前',
          onClick (picker) {
            const date = new Date()
            date.setTime(date.getTime() - 3600 * 1000 * 24 * 7)
            picker.$emit('pick', date)
          }
        }]
      },
      date: ''
    }
  },
  components: {
    navigator
  },
  mounted: function () {
    this.$refs.nav.setActiveIndex('/stock/toplist')
  },
  methods: {
    tableRowClassName ({row, rowIndex}) {
      if (parseInt(row.pchange) < 0) {
        return 'down-row'
      } else if (parseInt(row.pchange) > 0) {
        return 'up-row'
      }
      return ''
    },
    toggleLoading (show = true) {
      this.loading = show
    },
    search (date) {
      let totalSeconds = ''
      if (date !== null && date !== '') {
        totalSeconds = Math.floor(date.getTime() / 1000)
      }
      this.showTopList(totalSeconds)
    },
    showTopList (totalSeconds) {
      this.toggleLoading(true)
      this.$http.post('http://127.0.0.1:8000/api/stock/top/toplist', {date: totalSeconds})
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          if (res.error_num === 0) {
            this.topList = res['list']
          } else {
            this.$message.error('查询失败')
            console.log(res['msg'])
          }
          this.toggleLoading(false)
        }).catch(function (response) {
          // 响应错误
          console.log(response.status)
          this.$message({
            showClose: true,
            message: '数据获取异常：' + response.status + ' ' + response.statusText,
            type: 'warning',
            center: true
          })
          this.toggleLoading(false)
        })
    }
  }
}
</script>

<style>
body {
  margin: 0;
}

.el-footer {
  background-color: #B3C0D1;
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-table .up-row {
  background: oldlace;
}
.el-table .down-row {
  background: #f0f9eb;
}

</style>
