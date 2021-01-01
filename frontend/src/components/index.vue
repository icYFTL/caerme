<template>
    <div class="all">
        <top_bar :toggle-dark-mode="toggleDarkMode" class="top-bar"></top_bar>
        <div v-bind:class="index_class">
            <span><a href="https://ctftime.org/team/121175">Cáerme</a></span>
            <h2>free from kks servitute</h2>
            <div class="counters">
                <Counter class="counters_child" ref="RuRating" v-bind="counters.first" :duration=3
                         :scale-class=false></Counter>
                <Counter class="counters_child" ref="WorldRating" v-bind="counters.second"
                         :duration=3 :scale-class=false></Counter>
                <Counter class="counters_child" ref="PTS" v-bind="counters.third"
                         :duration=3 :scale-class=false></Counter>
            </div>
        </div>
    </div>
</template>

<script>
    import Counter from "./counter";
    import top_bar from "./top_bar";
    import axios from 'axios'

    export default {
        name: 'index',
        components: {top_bar, Counter},
        data() {
            return {
                counters_: {
                    'first': {
                        "from": 0,
                        "to": 0
                    },
                    'second': {
                        "from": 0,
                        "to": 0
                    },
                    'third': {
                        "from": 0,
                        "to": 0
                    }
                },
                index_class: "index white",
                sections: [{value: 25}, {value: 25}, {value: 25}, {value: 25}],

            }
        },
        async mounted() {
            if (this.$cookies.get('theme') && this.$cookies.get('theme') === 'dark') {
                this.$cookies.set('theme', 'white');
                this.toggleDarkMode();
            } else
                this.$cookies.set('theme', 'white');


            await axios.get("https://caerme.icyftl.ru/info").then((response) => {
                this.counters_.first.to = parseInt(response.data["ru_rating"]);
                this.counters_.second.to = parseInt(response.data["world_rating"]);
                this.counters_.third.to = parseInt(response.data["pts"]);
            })


            this.$refs.PTS.playAnimation();
            this.$refs.RuRating.playAnimation();
            this.$refs.WorldRating.playAnimation();


        },
        methods: {
            toggleDarkMode: function () {
                this.$cookies.set('theme', this.$cookies.get('theme') === 'white' ? 'dark' : 'white');
                this.index_class === "index black" ? this.index_class = "index white" : this.index_class = "index black";

                document.getElementsByTagName("body")[0].classList.add(this.$cookies.get('theme') === 'white' ? 'white' : 'black');
                document.getElementsByTagName("body")[0].classList.remove(this.$cookies.get('theme') === 'white' ? 'black' : 'white');
            }
        },
        computed: {
            counters: function () {
                return {
                    'first': {description: "RU Place:", numberFrom: this.counters_.first.from, numberTo: this.counters_.first.to},
                    'second': {description: "World Place:", numberFrom: this.counters_.second.from, numberTo: this.counters_.second.to},
                    'third': {description: "PTS:", numberFrom: this.counters_.third.from, numberTo: this.counters_.third.to}
                }
            }
        }

    }
</script>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Red+Rose&display=swap');

    @font-face {
        font-family: 'Chocolate';
        src: url('../assets/fonts/painting-with-chocolate.regular-webfont.woff2') format('woff2');
        font-weight: 100;
        font-style: normal;
    }


    .white {
      transition: all ease-in-out 1s;
      --default_color: black;
      background-blend-mode: hard-light;
      --bg-color: white;
    }
    .black {
      transition: all ease-in-out 1s;
      --default_color: white;
      --bg-color: black;
      background-blend-mode: difference;
    }

    body {
        background-size: 100%;
        background-repeat: no-repeat;
        background-color: var(--bg-color);
        background-image: url("../assets/pics/bg.png");
        /*filter: brightness(var(--bg-brightness)); Doesnt work yet */


    }

    .index {
        display: flex;
        align-items: center;
        flex-direction: column;
        width: 100%;
        top: 0;
        left: 0;
        color: var(--default_color);
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
        font-family: 'Red Rose', sans-serif;
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

    .top-bar {
        align-self: flex-end;
    }

    @media (max-width: 768px) {
        .counters {
            display: flex;
            flex-flow: column nowrap;
        }
    }

    @media (max-width: 470px) {
        .index {
            zoom: 0.7;
        }
    }

    @media (max-width: 435px) {
        .index span {
            font-size: 7rem;
        }
    }
</style>
