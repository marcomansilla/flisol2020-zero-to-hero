<template lang="pug">
    div#contactList
        b-button#newContact(
                            type="is-info"
                            icon-left="user-plus"
                            icon-pack="fas" size="is-medium"
                            @click="createContact")
        br
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
                       b-button(type="is-info"
                                icon-right="user-edit"
                                icon-pack="fas"
                                @click="updateContact(contact)")
                    td.has-text-centered
                       b-button(type="is-danger"
                                icon-right="user-slash"
                                icon-pack="fas"
                                @click="deleteContact(contact)")
        b-modal(
                :active.sync="openModal"
                has-modal-card
                trap-focus
                aria-role="dialog"
                aria-modal
                )
                modal-form-component(v-model="contacto")
                    template(slot="savebtn")
                        b-button.is-info(icon-right="save" icon-pack="fas" @click="saveContact(contacto)") Guardar

</template>

<script>
 import axios from 'axios';
 import ModalFormComponent from '@/components/ModalFormComponent'

 export default {
     components:{
         ModalFormComponent
     },
     data(){
         return {
             data:null,
             openModal: false,
             action:null,
             contacto:{
                 nombre:'',
                 apellido:'',
                 direccion:'',
                 telefono:'',
                 cumple:'',
                 email:''
             }
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
         },
         createContact(){
             this.openModal=true;
             this.action='save';
         },
         updateContact(contact){
             this.openModal=true;
             this.action='update';
             Object.assign(this.contacto, contact);
         },
         saveContact(contacto){
             if (this.action == 'update') {
                 axios.put('http://localhost:5000/api/contact', {data:{ ...contacto}}).then(response => {
                     this.getContacts();
                     this.$buefy.toast.open({
                         message: 'El usuario ha sido actualizado!',
                         type:'is-success',
                         position:'is-bottom'
                     })
                     this.openModal=false;
                     this.action=null;
                 }).catch(error => console.log(error))
             } else {
                 axios.post('http://localhost:5000/api/contact', { ...contacto}).then(response => {
                     this.getContacts();
                     this.$buefy.toast.open({
                         message: 'El usuario ha sido creado!',
                         type:'is-success',
                         position:'is-bottom'
                     })
                     this.openModal=false;
                     this.action=null;
                 }).catch(error => console.log(error))
             }
         }
     }
 }

</script>

<style lang="scss">
 #contactList {
     #newContact {
         position:relative;
         float:right;
         right:2rem;
     }
     table {
         width:90vw;
         margin:3rem auto;
         &.table thead tr th {
             text-align:center
         }
     }
 }
</style>
