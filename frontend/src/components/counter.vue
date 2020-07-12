<template>
    <div id="app">
        <h2>{{description}}</h2>
        <div id="wrapper">
            <number
                    class="bold transition"
                    :class="{scaleBig: scaleClass}"
                    ref="number2"
                    :from=numberFrom
                    animationPaused
                    :to=numberTo
                    :duration=duration
                    easing="Power4.easeOut"
                    @complete="completed"
            />
        </div>
    </div>
</template>

<script>
    export default {
        name: "counter",
        props: {
            description: String,
            numberFrom: Number,
            numberTo: Number,
            duration: Number,
            scaleClass: Boolean
        },

        methods: {

            completed() {
                //this.scaleClass = true;
            },
            playAnimation() {
                this.scaleClass = false;
                this.$refs.number2.play();
            }
        }

    };

</script>

<style scoped>
    #app {
        font-family: "Avenir", Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: inherit;
        margin-top: 60px;
    }

    .bold {
        font-weight: bold;
        font-size: 25px;
    }


    label {
        width: 100px;
        display: inline-block;
    }

    .scaleBig {
        font-size: 35px;
    }

    #wrapper {
        width: 150px;
        display: inline-block;
        padding: 20px 0;
        border-radius: 15px;
        box-shadow: 0 3px 8px 0 rgba(0, 0, 0, 0.18);
    }

    input {
        display: inline-block;
        margin: 10px;
        padding: 10px;
    }
</style>
