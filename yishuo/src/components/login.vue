<template>
    <div class="bigbox">
        <div class="pic">
            <div class="quan">
                <div class="quan1">
                    <div class="quan2">
                        <img src="" alt="">
                    </div>
                </div>
            </div>
        </div>
        <form action="">
            <div class="user">
                <img src="../assets/img/denglu.png" alt="">
                <input type="text" placeholder="请输入您的用户名" v-model="name">
            </div>
            <div class="pass">
                <img src="../assets/img/pass.png" alt="" width="40" height="40" style="margin-top: 0.3rem;margin-left:0.15rem">
                <input type="password" placeholder="请输入您的密码" v-model="password" style="margin-top: 0.2rem;margin-left:0.15rem">
            </div>
            <div class="sub">
                <button class="btn" @click="check">立即登录</button>
            </div>
        </form>
        <div class="box">
            <div class="left">
                <div class="wen">?</div>
                <a href="">忘记密码</a>
            </div>
            <div class="right">
                <div class="wen1"></div>
                <router-link to="/reg" class="zhu">新用户注册</router-link>
            </div>
        </div>
        <div class="bai">
            第三方登录
        </div>
        <div class="deng">
            <div class="yuan">
                <img src="../assets/img/qq.png" width="40" alt="" class="qq">
            </div>
            <div class="yuan">
                <img src="../assets/img/wei.png" width="35" alt="">
            </div>
            <div class="yuan">
                <img src="../assets/img/weibo.png" width="40" alt="">
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data(){
        return {
            name:"",
            password:"",
            flag:0
        }
    },
    methods:{
        check(){
            if(this.name=="zhangsan" && this.password == "123456"){
                sessionStorage.setItem('user','yes')
                this.$router.push("/")
            }else{
                this.$router.push("/login")
            }
        }
    }
}
</script>
<style scoped>
    img {
        display: block;
    }

    * {
        margin: 0;
        padding: 0;
        list-style: none;
    }

    a {
        text-decoration: none;
    }

    .bigbox {
        width: 100%;
        height: 100%;
    }

    .bigbox .quan {
        width: 2rem;
        height: 2rem;
        border-radius: 50%;
        background: rgb(223, 223, 226);
        margin: 1rem auto;
        position: relative;
        opacity: 0.85;
    }

    .bigbox .quan .quan1 {
        width: 1.6rem;
        height: 1.6rem;
        border-radius: 50%;
        background: rgb(198, 201, 203);
        position: absolute;
        top: 0.2rem;
        left: 0.2rem;
        opacity: 0.85;
    }

    .bigbox .quan .quan1 .quan2 {
        width: 1.2rem;
        height: 1.2rem;
        border-radius: 50%;
        background: rgb(78, 136, 244);
        position: absolute;
        top: 0.2rem;
        left: 0.2rem;
    }

    .user {
        width: 6.1rem;
        height: 1rem;
        border-bottom: 0.04rem solid rgb(208, 211, 212);
        margin: 0 auto;
        display: flex;
        justify-content: center;
    }

    .user input {
        width: 5rem;
        height: 0.8rem;
        font-family: "PingFang SC";
        font-size: 0.22rem;
        line-height: 0.8;
        outline: none;
    }

    .pass {
        width: 6.1rem;
        height: 1.2rem;
        border-bottom: 0.04rem solid rgb(208, 211, 212);
        margin: 0 auto;
        display: flex;
        justify-content: center;
    }

    .pass input {
        width: 5rem;
        height: 0.8rem;
        font-family: "PingFang SC";
        font-size: 0.22rem;
        line-height: 0.8;
        outline: none;
    }
    .sub{
        position: relative;
        margin:0.5rem 0;
        height:1rem;
    }
    .btn {
        margin-top: 0.56rem;
        width: 6.1rem;
        height: 0.8rem;
        outline: none;
        font-family: "PingFang SC";
        font-size: 0.24rem;
        line-height: 0.8;
        background: rgba(70, 130, 244, 0.15);
        border-radius: 0.7rem;
        color: rgba(70, 130, 244, 0.5);
        border: none;
        position: absolute;
        top:0;
        left:0;right:0;
        margin:0 auto;
    }

    .box {
        margin-left: 0.7rem;
        width: 6.1rem;
        height: 0.8rem;
        margin-top: 0.3rem;
        display: flex;
        justify-content: space-between;
    }

    .box .left {
        width: 3rem;
        height: 0.8rem;
        display: flex;
        justify-content: left;
    }

    .box .right {
        width: 1.7rem;
        height: 0.8rem;
        display: flex;
        justify-content: left;
    }

    .box .right .wen1 {
        width: 0.4rem;
        height: 0.1rem;
        margin-top: 0.2rem;
        border-radius: 0.04rem;
        background: rgb(253, 193, 48);
        box-shadow: 0 0.02rem 0.2rem rgb(253, 193, 48);
    }

    .box .wen {
        width: 0.5rem;
        height: 0.5rem;
        background: #ffffff;
        border-radius: 50%;
        color: rgb(27, 103, 247);
        font-size: 0.4rem;
        text-align: center;
        line-height: 0.5rem;
    }

    .box a {
        font-family: "PingFang SC";
        font-size: 0.24rem;
        line-height: 0.5rem;
        opacity: 0.4;
        margin-left: 0.09rem;
        color: #000;
        font-weight: 800;
    }

    .bai {
        text-align: center;
        font-family: "PingFang SC";
        font-size: 0.24rem;
        line-height: 2rem;
        opacity: 0.4;
        color: #000;
        font-weight: 800;
    }

    .deng {
        width: 4.5rem;
        height: 1rem;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
    }

    .deng .yuan {
        width: 1rem;
        height: 1rem;
        background: rgba(70, 130, 244, 0.1);
        border-radius: 50%;
    }

    .deng .yuan img {
        margin: 0.23rem auto;
    }

    .deng .yuan .qq {
        margin-top: 0.15rem;
    }

</style>