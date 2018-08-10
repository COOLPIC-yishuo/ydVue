<template>
    <div class="bigbox">
        <router-link to="/reg" class="fan"></router-link>
        <div class="pic">
            <div class="quan">
                <div class="quan1">
                    <div class="quan2">
                        <img src="" alt="">
                    </div>
                </div>
            </div>
        </div>
        <div class="bu">
            <img src="../assets/img/liu.png" alt="">
            <div class="aa">
                <div class="bb" style="opacity: 0.1"></div>
                <div class="bb" style="opacity: 0.2"></div>
                <div class="bb" style="opacity: 0.3"></div>
                <div class="bb" style="opacity: 0.5"></div>
                <div class="bb"></div>
            </div>
            <img src="../assets/img/liu.png" alt="">
            <div class="aa">
                <div class="cc" style="opacity: 0.1"></div>
                <div class="cc" style="opacity: 0.2"></div>
                <div class="cc" style="opacity: 0.3"></div>
                <div class="cc" style="opacity: 0.5"></div>
                <div class="cc"></div>
            </div>
            <img src="../assets/img/liucheng.png" alt="">
        </div>
        <div class="zizi">绑定手机号</div>
        <div v-text="message" style="font-size: 12px"></div>
        <form action="" id="reg">
        <div class="user">
            <img src="../assets/img/shouji.png" alt="" width="35" height="40" style="margin-top: 0.1rem">
            <img src="../assets/img/shou.png" alt="" width="25" height="10" style="margin-left: -0.2rem;margin-top: 0.4rem">
            <input type="text" placeholder="请填写您的手机号码" name="user" v-model="user" style="width:2.8rem;text-indent:0.2em" autocomplete="off">
            <div class="huo">
                获取验证码
            </div>
        </div>
        <div class="pass">
            <img src="../assets/img/xian.png" alt="" width="40" height="25">
            <input type="text" placeholder="请输入四位验证码" name="pass" autocomplete="off" v-model="pass">
        </div>
        <router-link to="/reg2" class="sub">
            <button class="btn" v-bind:disabled="dis" @click="tijiao" type="button">提交</button>
        </router-link>
        </form>
    </div>
</template>
<script>
    export default {
        data(){
            return {
                user: "",
                pass: "",
                pass1: "",
                message: "",
                dis: false
            }
        },
        methods:{
            tijiao(){
                if (this.user == "") {
                    this.message = "请输入用户名"
                    return false
                } else if (this.pass == "") {
                    this.message = "请输入密码"
                    return false
                } else if (this.pass1 != this.pass) {
                    this.message = "请确保两次输入密码一致"
                    return
                } else if (this.message == "注册成功") {
                    this.$router.push("/logn")
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
    .huo{
        width: 1.6rem;
        height: 0.6rem;
        background: rgba(195,216,233,0.4);
        color: rgb(64,207,255);
        border-radius: 0.5rem;
        margin-top: 0.16rem;
        font-size: 0.24rem;
        line-height: 0.6rem;
        text-align: center;
    }
    .zizi{
        width: 2rem;
        height: auto;
        font-family: "PingFang SC";
        font-size: 0.24rem;
        color: rgb(64,207,255);
        margin: 0.1rem 3.1rem;
        text-align: left;
        margin-bottom: 0.5rem;
    }
    .aa{
        width: 1rem;
        height: 0.2rem;
        display: flex;
        justify-content: space-around;
        margin-left: 0.1rem;
        margin-top: 0.3rem;
    }
    .cc{
        width: 0.1rem;
        height: 0.1rem;
        border-radius: 50%;
        background: rgb(96,109,115);
    }
    .bb{
        width: 0.1rem;
        height: 0.1rem;
        border-radius: 50%;
        background: rgb(64,207,255);
    }
    .bu{
        width:4.5rem ;
        height: 0.7rem;
        margin: 0.5rem auto 0;
        display: flex;
        justify-content: space-around;
    }
    .bu img{
        width: 0.65rem;
        height: 0.65rem;
    }
    .fan{
        display: block;
        width: 0.6rem;
        height: 0.6rem;
        margin: 0.8rem 0 0 0.3rem;
        background: url("../assets/img/back.png");
        background-size:0.6rem 0.6rem ;
    }
    .bigbox {
        width: 100%;
        height: 13.34rem;
        background-color: rgba(255,255,255,0.2);
        position: fixed;
        top: 0;
        left: 0;
    }
    .big {
        width: 100%;
        height: 13.34rem;
        background: url("../assets/img/bg.png");
        background-position: center;
        background-repeat: repeat;
        background-size: cover;
    }
    .bigbox .quan {
        width: 2rem;
        height: 2rem;
        border-radius: 50%;
        background: rgb(223, 223, 226);
        margin: 0.3rem auto;
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
        justify-content: space-between;
    }

    .user input {
        width: 5rem;
        height: 0.96rem;
        font-family: "PingFang SC";
        line-height: 0.8;
        font-size: 0.24rem;
        outline: none;
        margin-left:-0.2rem;
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
        width: 4.8rem;
        height: 1.1rem;
        font-family: "PingFang SC";
        font-size: 0.22rem;
        line-height: 0.8;
        outline: none;
        margin-left: 0.2rem;
    }
    .pass img{
        margin-top: 0.45rem;
        margin-left:-0.4rem;
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
    }
</style>