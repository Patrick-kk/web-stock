import Vue from 'vue'
import Router from 'vue-router'

import NotFound from '@/components/404NotFound.vue'

import home from '@/components/Home.vue'

import realtime from '@/components/movie/realtime.vue'
import daily from '@/components/movie/daily.vue'
import monthly from '@/components/movie/monthly.vue'
import cinemadaily from '@/components/movie/cinemadaily.vue'

import Stockhome from '@/components/stock/Stockhome.vue'
import TopList from '@/components/stock/top/TopList.vue'

Vue.use(Router)

const subrouter = {
  template: '<router-view></router-view>'
}

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: home,
      meta: {
        title: '主页'
      }
    },
    {
      path: '/movie',
      name: 'movie',
      component: subrouter,
      children: [
        {
          path: 'realtime',
          name: 'realtime',
          component: realtime,
          meta: {
            title: '实时票房'
          }
        },
        {
          path: 'daily',
          name: 'daily',
          component: daily,
          meta: {
            title: '每日票房'
          }
        },
        {
          path: 'monthly',
          name: 'monthly',
          component: monthly,
          meta: {
            title: '月度票房'
          }
        },
        {
          path: 'cinemadaily',
          name: 'cinemadaily',
          component: cinemadaily,
          meta: {
            title: '影院日度票房'
          }
        }
      ]
    },
    {
      path: '/stock',
      name: 'stock',
      component: subrouter,
      children: [
        {
          path: '',
          name: 'stockhome',
          component: Stockhome
        },
        {
          path: 'toplist',
          name: 'toplist',
          component: TopList,
          meta: {
            title: '每日龙虎榜'
          }
        }
      ]
    },
    {
      path: '*',
      component: NotFound
    }
  ]
})

router.beforeEach((to, from, next) => {
  /* 路由发生变化修改页面title */
  if (to.meta.title) {
    document.title = to.meta.title
  }
  next()
})

export default router
