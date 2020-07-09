<template lang="html">
  <div class="">
    <h3>Raspberry pi controler</h3>
    <v-container fluid>
      <v-row>
        <!-- <v-col cols="2">
          <v-switch flat :label="`GPIO 2`"></v-switch>
          <v-switch flat :label="`GPIO 3`"></v-switch>
          <v-switch flat :label="`GPIO 4`"></v-switch>
          <v-switch flat :label="`GPIO 5`"></v-switch>
          <v-switch flat :label="`GPIO 6`"></v-switch>
          <v-switch flat :label="`GPIO 7`"></v-switch>
        </v-col>

        <v-col cols="2">
          <v-switch flat :label="`GPIO 8`"></v-switch>
          <v-switch flat :label="`GPIO 9`"></v-switch>
          <v-switch flat :label="`GPIO 10`"></v-switch>
          <v-switch flat :label="`GPIO 11`"></v-switch>
          <v-switch flat :label="`GPIO 12`"></v-switch>
          <v-switch flat :label="`GPIO 13`"></v-switch>
        </v-col>

        <v-col cols="2">
          <v-switch flat :label="`GPIO 14`"></v-switch>
          <v-switch flat :label="`GPIO 15`"></v-switch>
          <v-switch flat :label="`GPIO 16`"></v-switch>
          <v-switch flat :label="`GPIO 17`"></v-switch>
          <v-switch flat :label="`GPIO 18`"></v-switch>
          <v-switch flat :label="`GPIO 19`"></v-switch>
        </v-col>

        <v-col cols="2">
          <v-switch flat :label="`GPIO 20`"></v-switch>
          <v-switch flat :label="`GPIO 21`"></v-switch>
          <v-switch flat :label="`GPIO 22`"></v-switch>
          <v-switch flat :label="`GPIO 23`"></v-switch>
          <v-switch flat :label="`GPIO 24`"></v-switch>
          <v-switch flat :label="`GPIO 25`"></v-switch>
        </v-col>

        <v-col cols="2">
          <v-switch flat :label="`GPIO 26`"></v-switch>
          <v-switch flat :label="`GPIO 27`"></v-switch>
        </v-col> -->
      </v-row>

      {{mensaje}}




    </v-container>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Gpio',
  data(){
    return{
      mensaje: ' '
    }
  },
  mounted () {
    axios
      .get('https://api.coindesk.com/v1/bpi/currentprice.json')
      .then(response => (this.mensaje = response))
  }
}
</script>

<style lang="css" scoped>
</style>
