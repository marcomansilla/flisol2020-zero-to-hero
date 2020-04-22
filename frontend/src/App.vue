<template lang="pug">
    div
        b-navbar(type="is-info")
            template(slot="brand")
                navbar-item(href="/")
                    .title.is-2.has-text-white Flisol 2020
        contacts-component
</template>

<script>
 import ContactsComponent from '@/components/ContactsComponent'

 export default {
     components: {
        ContactsComponent
     },
     data(){
         return {
         }
     }
 }
</script>
<style lang="scss">
 #app {
     font-family: Avenir, Helvetica, Arial, sans-serif;
     -webkit-font-smoothing: antialiased;
     -moz-osx-font-smoothing: grayscale;
     text-align: center;
     color: #2c3e50;
 }

 #nav {
     padding: 30px;
 }

 #nav a {
     font-weight: bold;
     color: #2c3e50;
 }

 #nav a.router-link-exact-active {
     color: #42b983;
 }
</style>
