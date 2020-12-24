<template>
    <div class="counter">
        <h2>{{description}}</h2>
        <div class="counter-wrapper">
            <number
                    class="bold transition"
                    v-bind:class="mode"
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
        },


    };

</script>

<style scoped>
    .counter {
        font-family: "Avenir", Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: inherit;
        margin-top: 60px;
    }

    .dark {
        --r: 255;
        --g: 255;
        --b: 255;
    }

    .white {
        --r: 0;
        --g: 0;
        --b: 0;
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

    .counter-wrapper {
        --r: 0;
        --g: 0;
        --b: 0;

        width: 150px;
        display: inline-block;
        padding: 20px 0;
        border-radius: 15px;
        box-shadow: 0 3px 8px 0 rgba(var(--r), var(--g), var(--b), 0.50);

    }

    input {
        display: inline-block;
        margin: 10px;
        padding: 10px;
    }
</style>
