<template>
    <div id="index">
        <div class="view">
            <router-view></router-view>
        </div>
        <div class="bottom">
            <div class="four">
                <router-link to="/index">
                    <img src="../assets/img/shouye.png" alt="">
                </router-link>
                <router-link to="/reg">
                    <img src="../assets/img/faxian.png" alt="">
                </router-link>
                <router-link to="/reg">
                    <img src="../assets/img/luntan.png" alt="">
                </router-link>
                <router-link to="/pre">
                    <img src="../assets/img/ge.png" alt="">
                </router-link>
            </div>
        </div>
    </div>
</template>
<script>

</script>
<style scoped>
    *{
        padding:0;
        margin:0;
    }
    .view {
        width: 100%;
        height: 13.34rem;
    }

    .bottom {
        width: 100%;
        height: 1rem;
        position: fixed;
        left: 0;
        bottom: 0;
        background-color: blue;
    }
    .bottom .four{
        width: 100%;
        height: 1rem;
        display: flex;
        justify-content: space-around;
    }
    a{
        width:0.7rem;
        height:0.6rem;
        padding:0.2rem 0.4rem;
        display: block;
    }
    a img{
        display: block;
        width: 0.8rem;
    }

</style>

