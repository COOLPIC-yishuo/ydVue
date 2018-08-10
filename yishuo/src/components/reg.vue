<template>
    <div class="bigbox">
        <router-link to="/login" class="fan"></router-link>
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
            <img src="../assets/img/liucheng.png" alt="">
            <div class="aa">
                <div class="cc" style="opacity: 0.1"></div>
                <div class="cc" style="opacity: 0.2"></div>
                <div class="cc" style="opacity: 0.3"></div>
                <div class="cc" style="opacity: 0.5"></div>
                <div class="cc"></div>
            </div>
            <img src="../assets/img/liucheng.png" alt="">
        </div>
        <div class="zi">填写基本信息</div>
        <form action="" id="reg">
            <div class="user">
                <img src="../assets/img/denglu.png" alt="">
                <input type="text" placeholder="请输入您的用户名" name="user" v-model="user" autocomplete="off"
                       @blur.prevent="checkName">
                <div class="message">
                    <span v-if=" nmessage == 0 " class="tips">{{ ntips }}</span>
                    <div class="errorbox" v-if=" nmessage == 0 ">
                        <img class="error" src="../assets/img/error-1.png" alt="">
                    </div>
                    <img class="passimg" src="../assets/img/pass-r.png" alt="" v-else-if=" nmessage == 1 ">
                    <div v-else="nmessage == null"></div>
                </div>
            </div>
            <div class="pass">
                <img src="../assets/img/pass.png" alt="" width="40" height="40">
                <input type="password" placeholder="请输入您的密码" name="pass" autocomplete="off" v-model="pass"
                       @blur.prevent="checkPass">
                <div class="message" v-if="">
                    <span v-if=" pmessage == 0 " class="tips">{{ ptips }}</span>
                    <div class="errorbox" v-if=" pmessage == 0 ">
                        <img class="error" src="../assets/img/error-1.png" alt="">
                    </div>
                    <img class="passimg" src="../assets/img/pass-r.png" alt="" v-else-if=" pmessage == 1 ">

                    <div v-else="pmessage == null"></div>
                </div>
            </div>
            <div class="pass">
                <img src="../assets/img/pass.png" width="40" height="40" alt="">
                <input type="password" placeholder="请确认您的密码" name="pass1" autocomplete="off" v-model="pass1"
                       @blur.prevent="checkPassAgain">
                <div class="message">
                    <span v-if=" amessage == 0 " class="tips">{{ atips }}</span>
                    <div class="errorbox" v-if=" amessage == 0 ">
                        <img class="error" src="../assets/img/error-1.png" alt="" v-if=" amessage == 0 ">
                    </div>
                    <img class="passimg" src="../assets/img/pass-r.png" alt="" v-else-if=" amessage == 1 ">
                    <div v-else="amessage == null"></div>
                </div>
            </div>
            <button class="btn" @click="tijiao" type="button">下一步</button>
        </form>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                user: "",
                pass: "",
                pass1: "",
                nmessage: null,
                pmessage: null,
                amessage: null,
                ntips: "",
                ptips: "",
                atips: "",
            }
        },
        methods: {
            checkName() {
                //进行前台验证并发起后台请求
                if (this.user.value == "" || this.user.length < 5) {
                    this.nmessage = 0
                    this.ntips = "用户名格式不正确"
                } else {
                    this.nmessage = 1
                }
            },
            checkPass() {
                //进行前台验证
                if (this.pass.value == "" || this.pass.length < 5) {
                    this.pmessage = 0
                    this.ptips = "密码格式不正确"
                } else {
                    this.pmessage = 1
                }
            },
            checkPassAgain() {
                //进行前台验证
                if (this.pass != this.pass1) {
                    this.atips = '两次密码不一致'
                    this.amessage = 0
                } else {
                    this.amessage = 1
                }
            },
            tijiao() {
                this.$router.push("/reg1")
                if(this.nmessage && this.pmessage && this.amessage){
                    this.$router.push("/reg1")
                } else {
                    return
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

    .zi {
        width: 2rem;
        height: auto;
        font-family: "PingFang SC";
        font-size: 0.24rem;
        color: rgb(64, 207, 255);
        margin: 0.1rem 1.1rem;
        text-align: left;
        margin-bottom: 0.5rem;
    }

    .aa {
        width: 1rem;
        height: 0.2rem;
        display: flex;
        justify-content: space-around;
        margin-left: 0.1rem;
        margin-top: 0.3rem;
    }

    .cc {
        width: 0.1rem;
        height: 0.1rem;
        border-radius: 50%;
        background: rgb(96, 109, 115);
    }

    .bb {
        width: 0.1rem;
        height: 0.1rem;
        border-radius: 50%;
        background: rgb(64, 207, 255);
    }

    .bu {
        width: 4.5rem;
        height: 0.7rem;
        margin: 0.5rem auto 0;
        display: flex;
        justify-content: space-around;
    }

    .bu img {
        width: 0.65rem;
        height: 0.65rem;
    }

    .fan {
        display: block;
        width: 0.6rem;
        height: 0.6rem;
        margin: 0.8rem 0 0 0.3rem;
        background: url("../assets/img/back.png");
        background-size: 0.6rem 0.6rem;
    }

    .bigbox {
        width: 100%;
        height: 13.34rem;
        background-color: rgba(255, 255, 255, 0.2);
        position: fixed;
        top: 0;

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
        justify-content: center;
        position: relative;
    }

    .user input {
        width: 5rem;
        height: 0.8rem;
        font-family: "PingFang SC";
        font-size: 0.22rem;
        line-height: 0.8;
        margin-top: 0.1rem;
        margin-left: 0.1rem;
        outline: none;
    }

    .user .message {
        height: 0.5rem;
        font-size: 12pt;
        position: absolute;
        top: 13px;
        right: 10px;
        border-radius: 15px;
        background-color: #e94242;
    }

    .user .message img {
        display: block;
        float: left;
        width: 0.05rem;
        background-color: white;
        border-radius: 0.025rem;
    }

    .user .message .passimg {
        width: 0.5rem;
    }

    .user .message span {
        width: 2.5rem;
        height: 0.5rem;
        font-size: 11pt;
        float: right;
        margin-right: 0.05rem;
        font-family: "PingFang SC";
        font-size: 10pt;
        line-height: 0.5rem;
        font-weight: 500;
        color: #ffffff;
    }

    .user .message .error {
        position: absolute;
        display: block;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        margin: auto;
    }

    .pass {
        width: 6.1rem;
        height: 1.2rem;
        border-bottom: 0.04rem solid rgb(208, 211, 212);
        margin: 0 auto;
        display: flex;
        justify-content: center;
        position: relative;
    }

    .pass input {
        width: 4.8rem;
        height: 1.10rem;
        font-family: "PingFang SC";
        font-size: 0.22rem;
        line-height: 0.8;
        outline: none;
        margin-top: 0.1rem;
        margin-left: 0.2rem;
    }

    .pass img {
        margin-top: 0.23rem;
    }

    .pass .message {
        height: 0.5rem;
        font-size: 12pt;
        position: absolute;
        top: 0.5rem;
        right: 10px;
        border-radius: 15px;
        background-color: #e94242;
    }

    .pass .message img {
        display: block;
        float: left;
        width: 0.05rem;
        background-color: white;
        border-radius: 0.025rem;
        margin-top: 0rem;
    }

    .pass .message .passimg {
        width: 0.5rem;
    }

    .pass .message span {
        width: 2.5rem;
        height: 0.5rem;
        font-size: 11pt;
        float: right;
        margin-right: 0.05rem;
        font-family: "PingFang SC";
        font-size: 10pt;
        line-height: 0.5rem;
        font-weight: 500;
        color: #ffffff;
    }

    .pass .message .error {
        position: absolute;
        display: block;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        margin: auto;
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

    .errorbox {
        float: left;
        width: 0.3rem;
        height: 0.3rem;
        background-color: white;
        border-radius: 0.15rem;
        margin-top: 0.1rem;
        margin-left: 0.1rem;
        position: relative;
    }
</style>