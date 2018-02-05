import Library from './components/Library.vue'
import NotFound from './components/404NotFound.vue'

import home from './components/Home.vue'
import TopList from './components/stock/top/TopList.vue'

const routers = [
  {
    path: '/Lib',
    name: 'lib',
    component: Library
  },
  {
    path: '/',
    name: 'home',
    component: home,
    meta: {
      title: '主页'
    }
  },
  {
    path: '/toplist',
    name: 'toplist',
    component: TopList,
    meta: {
      title: '每日龙虎榜'
    }
  },
  {
    path: '/Stock',
    name: 'stock',
    children: [
      {
        path: 'Top',
        name: 'top',
        children: [
          {
            path: 'TopList',
            name: 'toplist',
            component: TopList
          }
        ]
      }
    ]
  },
  {
    path: '*',
    component: NotFound
  }
]

export default routers
