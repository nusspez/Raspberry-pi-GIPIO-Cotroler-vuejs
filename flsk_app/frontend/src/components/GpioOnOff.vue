<template lang="html">
  <div class="">
    <h3>Raspberry pi controler</h3>
    <v-container fluid >
      <v-row >
        <v-col cols="7" sm="2" md="2" lg="2" xl="2">

          <div v-on:click="postMesage(2, switch2)">
            <v-switch flat :label="`GPIO 2`" v-model="switch2"></v-switch>
          </div>
          <div v-on:click="postMesage(3, switch3)">
            <v-switch flat :label="`GPIO 3`" v-model="switch3"></v-switch>
          </div>
          <div v-on:click="postMesage(4, switch4)">
            <v-switch flat :label="`GPIO 4`" v-model="switch4"></v-switch>
          </div>
          <div v-on:click="postMesage(5, switch5)">
            <v-switch flat :label="`GPIO 5`" v-model="switch5"></v-switch>
          </div>
          <div v-on:click="postMesage(6, switch6)">
            <v-switch flat :label="`GPIO 6`" v-model="switch6"></v-switch>
          </div>
          <div v-on:click="postMesage(7, switch7)">
            <v-switch flat :label="`GPIO 7`" v-model="switch7"></v-switch>
          </div>

        </v-col>

        <v-col cols="7" sm="2" md="2" lg="2" xl="2">

          <div v-on:click="postMesage(8, switch8)">
            <v-switch flat :label="`GPIO 8`" v-model="switch8"></v-switch>
          </div>
          <div v-on:click="postMesage(9, switch9)">
            <v-switch flat :label="`GPIO 9`" v-model="switch9"></v-switch>
          </div>
          <div v-on:click="postMesage(10,switch10)">
            <v-switch flat :label="`GPIO 10`" v-model="switch10"></v-switch>
          </div>
          <div v-on:click="postMesage(11, switch11)">
            <v-switch flat :label="`GPIO 11`" v-model="switch11"></v-switch>
          </div>
          <div v-on:click="postMesage(12, switch12)">
            <v-switch flat :label="`GPIO 12`" v-model="switch12"></v-switch>
          </div>
          <div v-on:click="postMesage(13, switch13)">
            <v-switch flat :label="`GPIO 13`" v-model="switch13"></v-switch>
          </div>

        </v-col>

        <v-col cols="7" sm="2" md="2" lg="2" xl="2">

          <div v-on:click="postMesage(14, switch14)">
            <v-switch flat :label="`GPIO 14`" v-model="switch14"></v-switch>
          </div>
          <div v-on:click="postMesage(15, switch15)">
            <v-switch flat :label="`GPIO 15`" v-model="switch15"></v-switch>
          </div>
          <div v-on:click="postMesage(16, switch16)">
            <v-switch flat :label="`GPIO 16`" v-model="switch16"></v-switch>
          </div>
          <div v-on:click="postMesage(17, switch17)">
            <v-switch flat :label="`GPIO 17`" v-model="switch17"></v-switch>
          </div>
          <div v-on:click="postMesage(18, switch18)">
            <v-switch flat :label="`GPIO 18`" v-model="switch18"></v-switch>
          </div>
          <div v-on:click="postMesage(19, switch19)">
            <v-switch flat :label="`GPIO 19`" v-model="switch19"></v-switch>
          </div>

        </v-col>

        <v-col cols="7" sm="2" md="2" lg="2" xl="2">
          <div v-on:click="postMesage(20, switch20)">
            <v-switch flat :label="`GPIO 20`" v-model="switch20"></v-switch>
          </div>
          <div v-on:click="postMesage(21, switch21)">
            <v-switch flat :label="`GPIO 21`" v-model="switch21"></v-switch>
          </div>
          <div v-on:click="postMesage(22, switch22)">
            <v-switch flat :label="`GPIO 22`" v-model="switch22"></v-switch>
          </div>
          <div v-on:click="postMesage(23, switch23)">
            <v-switch flat :label="`GPIO 23`" v-model="switch23"></v-switch>
          </div>
          <div v-on:click="postMesage(24, switch24)">
            <v-switch flat :label="`GPIO 24`" v-model="switch24"></v-switch>
          </div>
          <div v-on:click="postMesage(25, switch25)">
            <v-switch flat :label="`GPIO 25`" v-model="switch25"></v-switch>
          </div>

        </v-col>

        <v-col cols="7" sm="2" md="2" lg="2" xl="2">

          <div v-on:click="postMesage(26, switch26)">
            <v-switch flat :label="`GPIO 26`" v-model="switch26"></v-switch>
          </div>
          <div v-on:click="postMesage(27, switch27)">
            <v-switch flat :label="`GPIO 27`" v-model="switch27"></v-switch>
          </div>

        </v-col>
      </v-row>
    </v-container>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Gpio',
  data(){
    return{
      switch1: false,
      switch2: false,
      switch3: false,
      switch4: false,
      switch5: false,
      switch6: false,
      switch7: false,
      switch8: false,
      switch9: false,
      switch10: false,
      switch11: false,
      switch12: false,
      switch13: false,
      switch14: false,
      switch15: false,
      switch16: false,
      switch17: false,
      switch18: false,
      switch19: false,
      switch20: false,
      switch21: false,
      switch22: false,
      switch23: false,
      switch24: false,
      switch25: false,
      switch26: false,
      switch27: false,
      post1: {
        state:"1"
      },
      post0: {
        state:"0"
      }
    }
  },
  methods:{

    postMesage: function (number, switch_number) {
      if (switch_number == false){
        console.log("false");
        axios.put("http://192.168.1.71:3000/api/v1.0/action/" + number,this.post0);

      }
      else {
        console.log("true")
        axios.put("http://192.168.1.71:3000/api/v1.0/action/" + number,this.post1);

      }
    }
  }
};
</script>

<style lang="css" scoped>
</style>
