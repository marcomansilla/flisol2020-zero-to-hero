<template lang="pug">
    form
        .modal-card
            head.modal-card-head
                p.modal-card-title {{contacto._id ? 'Actualizar contacto' : 'Crear nuevo contacto'}}
            section.modal-card-body
                b-field(label="Nombre" horizontal)
                    b-input(v-model="contacto.nombre")
                b-field(label="Apellido" horizontal)
                    b-input(v-model="contacto.apellido")
                b-field(label="Direccion" horizontal)
                    b-input(v-model="contacto.direccion")
                b-field(label="Telefono" horizontal)
                    b-input(v-model="contacto.telefono")
                b-field(label="E-mail" horizontal)
                    b-input(v-model="contacto.email")
                b-field(label="Cumple" horizontal)
                    b-input(v-model="contacto.cumple")
        footer.modal-card-foot
            slot(name="savebtn")

</template>


<script>
 export default {
     props:['value'],
     computed:{
         contacto:{
             get(){ return this.value},
             set(record){ this.$emit('input', record)}
         }
     },
     beforeDestroy(){
        Object.assign(this.contacto, {
             nombre:'',
             apellido:'',
             direccion:'',
             telefono:'',
             cumple:'',
             email:''
         })
     }
 }

</script>
