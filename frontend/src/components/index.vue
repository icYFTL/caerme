<template>
    <div>
        <div v-bind:class="bg"></div>
        <top_bar :toggle-dark-mode="toggleDarkMode"></top_bar>
        <div v-bind:class="index_class">
            <span><a :href="caerme_ctftime_link">Cáerme</a></span>
            <h2>free from kks servitute</h2>
            <div class="counters">
                <Counter class="counters_child" ref="RuRating" :description=description1 :number-from=numberFrom1
                         :number-to=numberTo1 :duration=3
                         :scale-class=false></Counter>
                <Counter class="counters_child" ref="WorldRating" :description=description2 :number-from=numberFrom2
                         :number-to=numberTo2
                         :duration=3 :scale-class=false></Counter>
                <Counter class="counters_child" ref="PTS" :description=description3 :number-from=numberFrom3 :number-to=numberTo3
                         :duration=3 :scale-class=false></Counter>
            </div>
        </div>
    </div>
</template>

<script>
    import Counter from "./counter";
    import top_bar from "./top_bar";
    import Vue from 'vue';
    import axios from 'axios'
    //import Players from "@/components/players";


    export default {
        name: 'index',
        components: {/*Players*/ top_bar, Counter},
        props: {
            caerme_ctftime_link: String
        }
        , data() {
            return {
                description1: "RU Place:",
                description2: "World Place:",
                description3: "PTS:",
                numberFrom1: 0,
                numberFrom2: 0,
                numberFrom3: 0,
                numberTo1: 0,
                numberTo2: 0,
                numberTo3: 0,
                index_class: "index white",
                bg: "backgroundMountain white"
            }
        },
        async mounted() {
            if (Vue.$cookies.get('theme') && Vue.$cookies.get('theme') === 'dark'){
                Vue.$cookies.set('theme', 'white');
                this.toggleDarkMode();
            }
            else
                Vue.$cookies.set('theme', 'white');


            await axios.get("https://caerme.icyftl.ru/ctftime/teams/get/team/121175/id").then((response) => {
                this.numberTo1 = parseInt(response.data["ru_rating"]);
                this.numberTo2 = parseInt(response.data["rating"][0][new Date().getFullYear().toString()]["rating_place"]);
                this.numberTo3 = parseInt(response.data["rating"][0][new Date().getFullYear().toString()]["rating_points"]);
            })


            this.$refs.PTS.playAnimation();
            this.$refs.RuRating.playAnimation();
            this.$refs.WorldRating.playAnimation();


        },
        methods: {
            toggleDarkMode: function () {
                Vue.$cookies.set('theme', Vue.$cookies.get('theme') === 'white' ? 'dark' : 'white');
                this.index_class === "index black" ? this.index_class = "index white" : this.index_class = "index black";
                this.bg === "backgroundMountain black" ? this.bg = "backgroundMountain white" : this.bg = "backgroundMountain black";
            }
        }
    }
</script>

<style scoped>
    @font-face {
        font-family: 'Chocolate';
        src: url('../assets/fonts/painting-with-chocolate.regular-webfont.woff2') format('woff2');
        font-weight: 100;
        font-style: normal;
    }

    .white {
        --default_color: black;
        --bg-brightness-lighter: 280%;
        --bg-brightness: 280%;
        --bg-color: none;
        transition-duration: 1s;
    }
    .black{
        --default_color: white;
        --bg-brightness-lighter: 60%;
        --bg-brightness: 60%;
        --bg-color: black;
        transition-duration: 1s;
    }

    .backgroundMountain {
        z-index: -1;
        position: absolute;
        top: 0;
        left: 0;
        -webkit-filter: brightness(var(--bg-brightness-lighter));
        filter: brightness(var(--bg-brightness));
        background-size: cover;
        background-position: center;
        background-color: var(--bg-color);
        width: 100%;
        height: 100%;
        background-image: url("../assets/pics/bg.png");
        background-repeat: space;
    }

    .index {
        display: flex;
        align-items: center;
        flex-direction: column;
        margin-top: 10px;
        color: var(--default_color)
    }

    .index a {
        text-decoration: none;
        color: inherit;
    }

    .index span {
        font-family: Chocolate, sans-serif;
        font-size: 8.5rem;
        margin-top: 50px;
        transition: text-shadow 0.5s ease-in-out;
    }

    .index span:hover {
        text-shadow: 1px 1px 1px var(--default_color);
    }

    .index span a {
        cursor: default;
    }

    .index h2 {
        margin-top: -20px;
        font-weight: normal;
        font-family: Optima, sans-serif;
        transition: text-shadow 0.5s ease-in-out;
    }


    .index h2:hover {
        text-shadow: 1px 1px 1px var(--default_color);
        cursor: default;
    }

    .counters {
        display: flex;
        flex-flow: row nowrap;
    }

    .counters_child {
        margin: 100px;
    }


</style>
