<template>
    <div class="bigbox">
        <router-link to="/reg1" class="fan"></router-link>
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
               <div class="bb" style="opacity: 0.1"></div>
                <div class="bb" style="opacity: 0.2"></div>
                <div class="bb" style="opacity: 0.3"></div>
                <div class="bb" style="opacity: 0.5"></div>
                <div class="bb"></div>
            </div>
            <img src="../assets/img/liu.png" alt="">
        </div>
        <div class="zizi">选择头像上传</div>
         <div class="pic" style="margin-top: 0.8rem">
            <div class="quan">
                <div class="quan1">
                    <div class="quan2">
                        <img src="" alt="">
                    </div>
                </div>
            </div>
        </div>
        <div class="pai">
            <img src="../assets/img/xiang.png" alt="" width="60" height="50">
            <img src="../assets/img/wen.png" alt="" width="45" height="35" style="margin-top:0.05rem">
        </div>
        <div class="zi">
            <span style="margin-left: 0.15rem">拍照</span>
            <span>相册</span>
        </div>
        <button class="btn" type="button" @click="check">完成</button>
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
            }
        },
        methods:{
            check(){
                this.$router.push('/login')
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
    .pai{
        width: 4.5rem;
        height: 0.9rem;
        display: flex;
        justify-content: space-between;
        margin: 1rem auto 0;
    }
    .zi{
        width: 4.2rem;
        height: 1rem;
        display: flex;
        font-size: 11pt;
        justify-content: space-between;
        margin: 0 auto;
    }
    .zizi{
        width: 4rem;
        height: auto;
        font-family: "PingFang SC";
        font-size: 0.24rem;
        color: rgb(64,207,255);
        margin: 0.1rem 2.4rem;
        text-align: right;
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
    .bb{
        width: 0.1rem;
        height: 0.1rem;
        border-radius: 50%;
        background: rgb(64,207,255);
    }
    .bu{
        width:4.5rem ;
        height: 0.7rem;
        margin: 1.5rem auto 0;
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
        left:0;
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