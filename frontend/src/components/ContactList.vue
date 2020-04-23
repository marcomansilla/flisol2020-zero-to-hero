<template lang="pug">
    div#contactList
        table.table
            thead
                tr
                    th Apellido
                    th Nombre
                    th Direccion
                    th Telefono
                    th Cumple
                    th Editar
                    th Eliminar
            tbody
                tr(v-for="contact in data")
                    td {{contact.apellido}}
                    td {{contact.nombre}}
                    td {{contact.direccion}}
                    td {{contact.telefono}}
                    td {{contact.cumple}}
                    td.has-text-centered
                       b-button(type="is-info" icon-right="user-edit" icon-pack="fas")
                    td.has-text-centered
                       b-button(type="is-danger"
                                icon-right="user-slash"
                                icon-pack="fas"
                                @click="deleteContact(contact)")

</template>

<script>
 import axios from 'axios';

 export default {
     data(){
         return {
             data:null
         }
     },
     mounted(){
         this.getContacts()
     },
     methods:{
         getContacts(){
             axios.get('http://localhost:5000/api/contacts').then(response =>{
                 this.data = response.data
             }).catch(error => console.log(error))
         },
         deleteContact(contact){
             this.$buefy.dialog.confirm({
                 title: 'Eliminar contacto',
                 message: 'Seguro que quiere eliminar el contacto?, esta operacion no puede ser revertida',
                 confirmText: 'Si',
                 cancelText: 'No',
                 type: 'is-danger',
                 hasIcon: true,
                 onConfirm: () => {
                     axios.delete('http://localhost:5000/api/contact', {data : {id: contact._id.$oid}}).then(response => {
                         this.getContacts();
                         this.$buefy.toast.open({
                             message: 'El usuario ha sido eliminado',
                             type:'is-success',
                             position:'is-bottom'
                         })
                     }).catch(error => console.log(error))
                 }
             })
         }
     }
 }

</script>

<style lang="scss">
 #contactList {
     table {
         width:90vw;
         margin:auto;
         &.table thead tr th {
             text-align:center
         }

     }
 }

</style>
