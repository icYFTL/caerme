<template>
    <div>
        <div class="players">
            <div class="player">
                <img src="../assets/pics/undefined.jpeg">
            </div>
            <div class="player">
                <img src="../assets/pics/undefined.jpeg">
            </div>
            <div class="player">
                <img src="../assets/pics/undefined.jpeg">
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "players"
    }
</script>

<style scoped>
    .players {
        display: flex;
        flex-flow: row ;
        margin: 20px;
    }
    .player img{

        width: 150px;
        height: 150px;
        -webkit-border-radius: 50%;
        -moz-border-radius: 50%;
        border-radius: 50%;
        background: red;
    }
</style>