<template lang="pug">
   div
    br
    h1.has-text-centered.title.is-1 Lista de Contactos
    contact-list
</template>

<script>
 import ContactList from '@/components/ContactList'

 export default {
     components: {
        ContactList
     }
 }

</script>

<style>

</style>
