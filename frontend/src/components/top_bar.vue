<template>
    <div class="collection">
        <div v-on:click="toggleDarkMode">
            <svg width="30" height="30" viewBox="0 0 48 48">

                <path d="M22 41C32.4934 41 41 32.4934 41 22C41 11.5066 32.4934 3 22
                3C11.5066 3 3 11.5066 3 22C3 32.4934 11.5066 41 22 41ZM7 22C7
                13.7157 13.7157 7 22 7V37C13.7157 37 7 30.2843 7 22Z"></path>
            </svg>
        </div>
    </div>
</template>

<script>
    export default {
        name: "top_bar",
        props: {
            toggleDarkMode: Function
        }
    }
</script>

<style scoped>
    .collection{
        display: flex;
        flex-flow: row nowrap;
        justify-content: flex-end;
        overflow: hidden;
    }
</style>