<template>
    <div class="bigbox">
        <div class="top">
            <div class="tit">
                <img src="../assets/img/fenlei.png" alt="" width="40" height="40"
                     style=" margin-left: 0.15rem;margin-top: 0.1rem">
                <span>COOLPic</span>
                <img src="../assets/img/camer.png" alt="" width="40" height="35"
                     style="margin-right: 0.15rem;margin-top: 0.1rem">
            </div>
            <div class="sou">
                <div class="dian"></div>
                <input type="text" placeholder="请输入您要搜索的内容">
                <img src="../assets/img/yuyin.png" alt="" width="18" height="25">
            </div>
        </div>
        <div class="lun">
            <div class="slideshow">
                <transition-group tag="ul" name="image">
                    <li v-for="(img, index) in imgArray" v-show="index===mark" :key="index" >
                        <a href="/">
                            <img src='../assets/img/1.png' alt="" width="83%" style="border-radius:0.2rem">
                            <!--<img :src='img'>-->
                        </a>
                    </li>
                </transition-group>
            </div>
        </div>
        <div class="bai">
            <div class="dian1">
                <div class="yuan" style="opacity: 0.3"></div>
                <div class="yuan" style="opacity: 0.5"></div>
                <div class="yuan"></div>
            </div>
            <span>HOT&nbsp&nbspTEST</span>
            <div class="dian1">
                <div class="yuan" style="opacity: 1"></div>
                <div class="yuan" style="opacity: 0.5"></div>
                <div class="yuan" style="opacity: 0.3"></div>
            </div>
        </div>
        <div class="zi">
            <span>猜你</span>
            <span style="color: rgb(73,135,254)">喜欢</span>
        </div>
        <div class="con">
            <div class="xiaobox" style="margin-bottom:0.3rem " v-for="item in guess">
                <div class="tu">
                    <img src="../assets/img/2.png" alt="">
                </div>
                <span class="tname">{{ item.ctitle }}</span>
                <div class="user">
                    <div class="tou">
                        <img src="../assets/img/9.png" alt="">
                    </div>
                    <span>{{ item.cname }}</span>
                </div>
                <div class="zan">
                    <div class="zan1">
                        <img class="aa" src="../assets/img/pinglun.png" alt="">
                        <span class="znum">{{ item.zannum }}</span>
                    </div>
                    <div class="zan1">
                        <img class="aa" src="../assets/img/xiazai.png" alt="">
                        <span class="xnum">{{ item.downloadnum }}</span>
                    </div>
                </div>
            </div>
        </div>
        <div class="sheji">
            <div class="dian2">
                <div class="yuan"></div>
                <div class="yuan" style="opacity: 0.5"></div>
                <div class="yuan" style="opacity: 0.3"></div>
            </div>
            <div class="zixun">
                <span>设计</span>
                <span style="color: rgb(73,135,254)">资讯</span>
                <div class="geng">
                    <button>MORE</button>
                </div>
            </div>
        </div>
        <span class="info">Information</span>
        <div class="son">
            <div class="son1" v-for="item in information">
                <div class="left">
                    <div class="tu">
                        <img src="../assets/img/4.png" alt="">
                    </div>
                </div>
                <div class="right">
                    <span class="bb">{{ item.ctitle }}</span>
                    <div class="user cc">
                        <div class="tou">
                            <img src="../assets/img/9.png" alt="">
                        </div>
                        <span>{{ item.cname }}</span>
                    </div>
                    <div class="shou">
                        <div class="bei">
                            <img src="../assets/img/dianzan.png" alt="">
                        </div>
                        <span class="znum1">{{ item.zannum }}</span>
                    </div>
                </div>
            </div>
        </div>
        <div class="bai bai1">
            <div class="dian1">
                <div class="yuan" style="opacity: 0.3"></div>
                <div class="yuan" style="opacity: 0.5"></div>
                <div class="yuan"></div>
            </div>
            <span>HOT&nbsp;&nbsp;TEST</span>
            <div class="dian1">
                <div class="yuan" style="opacity: 1"></div>
                <div class="yuan" style="opacity: 0.5"></div>
                <div class="yuan" style="opacity: 0.3"></div>
            </div>
        </div>
        <div class="zi">
            <span>最新</span>
            <span style="color: rgb(73,135,254)">资讯</span>
        </div>
        <div class="con con1">
            <div class="xiaobox" style="margin-bottom:0.3rem " v-for="item in newText">
                <div class="tu">
                    <img src="../assets/img/2.png" alt="">
                </div>
                <span class="tname">{{ item.ctitle }}</span>
                <div class="user">
                    <div class="tou">
                        <img src="../assets/img/9.png" alt="">
                    </div>
                    <span>{{ item.cname }}</span>
                </div>
                <div class="zan">
                    <div class="zan1">
                        <img class="aa" src="../assets/img/pinglun.png" alt="">
                        <span class="znum">{{item.zannum}}</span>
                    </div>
                    <div class="zan1">
                        <img class="aa" src="../assets/img/xiazai.png" alt="">
                        <span class="xnum">{{item.downloadnum}}</span>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                newText: [
                    {'cid': 1, 'cname': 'BeckHam', 'ctitle': '悉尼歌剧院插画作品集', 'zannum': 15, 'downloadnum': 28},
                    {'cid': 2, 'cname': 'Chritina', 'ctitle': 'Metro Design', 'zannum': 11, 'downloadnum': 26}
                ],
                information: [
                    {'cid': 1, 'cname': 'BeckHam', 'ctitle': '2018中央美院研究生毕业展现场报道', 'zannum': 1866},
                    {'cid': 2, 'cname': 'Chritina', 'ctitle': 'Metro Design', 'zannum': 1886}
                ],
                guess: [
                    {'cid': 1, 'cname': 'BeckHam', 'ctitle': '悉尼歌剧院插画作品集', 'zannum': 15, 'downloadnum': 28},
                    {'cid': 2, 'cname': 'Chritina', 'ctitle': 'Metro Design', 'zannum': 11, 'downloadnum': 26},
                    {'cid': 3, 'cname': 'BeckHam', 'ctitle': '悉尼歌剧院插画作品集', 'zannum': 15, 'downloadnum': 28},
                    {'cid': 4, 'cname': 'Chritina', 'ctitle': 'Metro Design', 'zannum': 11, 'downloadnum': 26}
                ],
                mark: 0,
                imgArray: [
                    '/assets/img/1.png',
                    '/img/2.png',
                    '/img/4.png',
                    '/img/9.png'
                ]
            }
        },
        methods: {
            autoPlay() {
                this.mark++;
                if (this.mark === 4) { //当遍历到最后一张图片置零
                    this.mark = 0
                }
            },
            play() {
                setInterval(this.autoPlay, 3000)
            },
            change(i) {
                this.mark = i
            }
        },
        created() {
            this.play()
        }
    }
</script>
<style scoped>

    .image-enter-active {
        transform: translateX(0);
        transition: all 1.5s ease;
    }

    .image-leave-active {
        transform: translateX(-100%);
        transition: all 1.5s ease;
    }

    .image-enter {
        transform: translateX(100%);
    }

    .image-leave {
        transform: translateX(0);
    }

    .slideshow {
        width: 100%;
        height: 2rem;
        overflow: hidden;
    }

    li {
        width: 100%;
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        margin: 0 auto;
        overflow: hidden;
    }
    li a{
        display: block;
        overflow: hidden;
    }
    .bigbox .bai1 {
        margin-top: 0;
    }

    .shou .znum1 {
        display: block;
        width: 1rem;
        height: 0.4rem;
        font-family: "PingFang SC";
        font-size: 0.24rem;
        color: rgba(0, 0, 0, 0.3);
        margin-left: 0.1rem;
    }

    .shou .bei {
        width: 0.3rem;
        height: 0.3rem;
        border-radius: 50%;
        background: rgb(255, 217, 28);
        margin-top:0.02rem;
        overflow: hidden;

    }

    .shou .bei img {
        display: block;
        width: 0.16rem;
        
        margin-left:0.07rem;
        margin-top:0.07rem;

    }

    .shou {
        width: 1.6rem;
        height: 0.4rem;
        position: absolute;
        top: 1.3rem;
        left: 3.4rem;
        display: flex;
        justify-content: space-between;
    }

    .cc {
        margin-left: 0.15rem;
        font-family: "PingFang SC";
        font-size: 0.24rem;
    }

    .bb {
        display: block;
        line-height: 1rem;
        margin-left: 0.2rem;
    }

    .son .son1 .right {
        width: 4.75rem;
        height: 2rem;
        background: #fff;
        font-family: "PingFang SC";
        font-size: 0.24rem;
        text-align: left;
        position: relative;
    }

    .son .son1 .left .tu img {
        width: 1.5rem;
        height: 1.5rem;
    }

    .son .son1 .left {
        width: 2rem;
        height: 2rem;
        background: #fff;
        overflow: hidden;
        box-shadow: 0rem 0rem 0rem rgba(0, 0, 0, 0.1), 0rem 0rem 0rem rgba(0, 0, 0, 0.1), 0.1rem 0rem 0.9rem rgba(0, 0, 0, 0.1), 0rem 0rem 0rem rgba(0, 0, 0, 0.1);
    }

    .son .son1 .left .tu {
        width: 1.5rem;
        height: 1.5rem;
        margin: 0.25rem auto;
        overflow: hidden;
        box-shadow: 0rem -0.1rem 0.1rem rgba(0, 0, 0, 0.1), -0.1rem 0rem 0.1rem rgba(0, 0, 0, 0.1), 0.1rem 0rem 0.1rem rgba(0, 0, 0, 0.1), 0rem 0.1rem 0.1rem rgba(0, 0, 0, 0.1);
    }

    .son .son1 {
        width: 100%;
        height: 2rem;
        background: #fff;
        display: flex;
        justify-content: space-between;
    }

    .son {
        width: 90%;
        height: 4.5rem;
        margin: 0.4rem auto 0;
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-end;
    }

    .geng {
        width: 1.3rem;
        height: 0.5rem;
        border-radius: 0.4rem;
        background: rgb(132, 124, 255);
        position: absolute;
        left: 5.4rem;
        top: 0;
        line-height: 0.5rem;

    }

    .geng button {
        width: 1.2rem;
        height: 0.5rem;
        border-radius: 0.4rem;
        background: rgb(132, 124, 255);
        outline: none;
        border: none;
        letter-spacing: 0.02rem;
        color: #fff;
        font-weight: 800;
    }

    .info {
        display: block;
        width: 2rem;
        height: 0.4rem;
        font-family: "PingFang SC";
        font-size: 0.28rem;
        color: rgba(44, 47, 52, 0.4);
        text-align: left;
        margin-left: 0.4rem;
        font-weight: 800;
        letter-spacing: 0.02rem;
    }

    .sheji {
        width: 3rem;
        height: 0.5rem;
        margin: 0.4rem 0.4rem 0;
        display: flex;
        justify-content: left;
        position: relative;
    }

    .sheji .dian2 {
        width: 0.2rem;
        height: 0.5rem;
    }

    .sheji .dian2 .yuan {
        width: 0.08rem;
        height: 0.08rem;
        background: rgb(0, 155, 190);
        border-radius: 100%;
        margin-top: 0.08rem;
    }

    .sheji .zixun {
        width: 1.7rem;
        height: 0.8rem;
        font-family: "PingFang SC";
        font-size: 0.34rem;
        line-height: 0.6rem;
        display: flex;
        justify-content: space-around

    }

    .znum, .xnum {
        display: block;
        width: 0.4rem;
        height: 0.2rem;
        font-size: 0.2rem;
        position: absolute;
        top: -0.01rem;
        left: 0.53rem;
        font-weight: 800;
        color: rgb(195, 195, 195);
    }

    .zan {
        width: 2rem;
        height: 0.3rem;
        margin: 0 0.9rem;
        display: flex;
        justify-content: space-between;

    }

    .zan .zan1 {
        width: 0.8rem;
        height: 0.3rem;
        position: relative;
        top: 0;
        left: 0;
    }

    .zan .zan1 .aa {
        width: 0.5rem;
        height: 0.5rem;
        position: absolute;
        top: -0.1rem;
        left: 0.2rem;
    }

    .user {
        width: 2.5rem;
        height: 0.8rem;
        display: flex;
        justify-content: left;
    }

    .user .tou {
        width: 0.7rem;
        height: 0.7rem;
        border-radius: 50%;
        margin-left: 0.1rem;
        overflow: hidden;
        background: black;
        position: relative;
    }

    .con .xiaobox .user .tou img {
        width: 0.7rem;
        height: 0.7rem;
        position: absolute;
        top: 0;
        left: 0;
    }

    .user span {
        margin-top: 0.2rem;
        margin-left: 0.2rem;
        font-size: 0.24rem;
        font-weight: 800;
        color: rgb(195, 195, 195);
    }

    .user img {
        width: 1rem;
        height: 1rem;
    }

    .con {
        width: 90%;
        height: 12rem;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        margin: 0 auto;
    }

    .con1 {
        width: 90%;
        height: 7rem;
    }

    .con .xiaobox {
        width: 3.2rem;
        height: 5.7rem;
        background: #fff;
    }

    .con .xiaobox .tu {
        width: 3.2rem;
        height: 4rem;
        overflow: hidden;
    }

    .con .xiaobox img {
        width: 3.2rem;
        height: auto;
    }

    .con .xiaobox .tname {
        display: block;
        font-family: "PingFang SC";
        font-size: 0.24rem;
        margin: 0.1rem 0.2rem;
        text-align: left;
        color: rgba(0, 0, 0, 0.7);
    }

    .zi {
        width: 2rem;
        height: 0.4rem;
        margin: 0.1rem auto;
        font-family: "PingFang SC";
        font-size: 0.34rem;
        line-height: 0.4rem;
        display: flex;
        justify-content: space-around;
    }

    .dian1 {
        width: 0.6rem;
        height: 0.4rem;
        display: flex;
        justify-content: space-around;

    }

    .dian1 .yuan {
        width: 0.1rem;
        height: 0.1rem;
        background: rgb(0, 155, 190);
        border-radius: 100%;
        margin-top: 0.15rem;
    }

    .bai {
        width: 3.5rem;
        height: 0.4rem;
        display: flex;
        justify-content: space-between;
        font-size: 0.3rem;
        font-weight: 800;
        margin: 3rem auto 0;
        color: rgb(0, 155, 190);
    }

    .lun {
        width: 100%;
        height: 4rem;
        position: absolute;
        top: 2.5rem;
        display: flex;
        justify-content: space-around;
        overflow: hidden;
    }

    .bigbox {
        width: 100%;
        height: auto;
        background: rgb(251, 251, 251);
        position: relative;
    }

    .tit {
        display: flex;
        justify-content: space-between;
        font-family: "SignPainter";
        line-height: 1.4rem;
        font-size: 0.8rem;

    }

    .sou {
        width: 6.5rem;
        height: 0.7rem;
        background: rgba(57, 60, 64, 0.1);
        border-radius: 0.5rem;
        margin: 0 auto;
        display: flex;
        justify-content: left;
    }

    .sou .dian {
        width: 0.1rem;
        height: 0.1rem;
        background: rgba(255, 197, 40, 1);
        border-radius: 0.6rem;
        margin: 0.3rem 0.2rem 0rem 0.3rem;
    }

    .sou input {
        width: 6rem;
        height: 0.7rem;
        outline: none;
        border: none;
        background: rgba(57, 60, 64, 0);
    }

    .sou img {
        margin-right: 0.2rem;
        margin-top: 0.06rem;
        opacity: 0.6;
    }

    .top {
        width: 100%;
        height: 4rem;
        background-image: linear-gradient(to right bottom, #4e87f4, #61ccf3);
    }
</style>