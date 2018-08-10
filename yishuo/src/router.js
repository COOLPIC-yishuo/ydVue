import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Login from '@/components/login.vue'
import Reg from '@/components/reg.vue'
import Reg1 from '@/components/reg1.vue'
import Reg2 from '@/components/reg2.vue'
import Pre from '@/components/personal.vue'
import Index from '@/components/index.vue'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home,
            beforeEnter: (to, from, next) => {
                if (sessionStorage["user"] == 'yes') {
                    next()
                } else {
                    next('/login')
                }
            },
            children: [
                {
                    path: '',
                    component: Index
                },
                {
                    path: '/pre',
                    component: Pre
                },
                {
                    path: '/index',
                    component: Index
                },
            ]
        },
        {
            path: '/login',
            component: Login
        },
        {
            path: '/reg',
            name: Reg,
            component: Reg
        },
        {
            path: '/reg1',
            component: Reg1
        },
        {
            path: '/reg2',
            component: Reg2
        },
        {
            path: "*",
            redirect: "/"
        }
    ]
})
// qqq.beforeEnter((to,from,next)=> {
//           if( sessionStorage["user"] == 'yes' ){
//               next()
//           }else {
//               next('/login')
//           }
//       });
