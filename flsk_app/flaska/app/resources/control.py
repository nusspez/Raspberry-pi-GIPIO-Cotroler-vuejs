from gpiozero import LED

PIN_2 = LED(2)
PIN_3 = LED(3)
PIN_4 = LED(4)
PIN_5 = LED(5)
PIN_6 = LED(6)
PIN_7 = LED(7)
PIN_8 = LED(8)
PIN_9 = LED(9)
PIN_10 = LED(10)
PIN_11 = LED(11)
PIN_12 = LED(12)
PIN_13 = LED(13)
PIN_14 = LED(14)
PIN_15 = LED(15)
PIN_16 = LED(16)
PIN_17 = LED(17)
PIN_18 = LED(18)
PIN_19 = LED(19)
PIN_20 = LED(20)
PIN_21 = LED(21)
PIN_22 = LED(22)
PIN_23 = LED(23)
PIN_24 = LED(24)
PIN_25 = LED(25)
PIN_26 = LED(26)
PIN_27 = LED(27)

class Pin:
    def __init__(self,state,gpio_number):
        self.gpio_number = gpio_number
        self.state = state

    def change_satate(self):

        if self.state == '1':
            if self.gpio_number == '2':
                PIN_2.on()
            elif self.gpio_number == '3':
                PIN_3.on()
            elif self.gpio_number == '4':
                PIN_4.on()
            elif self.gpio_number == '5':
                PIN_5.on()
            elif self.gpio_number == '6':
                PIN_6.on()
            elif self.gpio_number == '7':
                PIN_7.on()
            elif self.gpio_number == '8':
                PIN_8.on()
            elif self.gpio_number == '9':
                PIN_9.on()
            elif self.gpio_number == '10':
                PIN_10.on()
            elif self.gpio_number == '11':
                PIN_11.on()
            elif self.gpio_number == '12':
                PIN_12.on()
            elif self.gpio_number == '13':
                PIN_13.on()
            elif self.gpio_number == '14':
                PIN_14.on()
            elif self.gpio_number == '15':
                PIN_15.on()
            elif self.gpio_number == '16':
                PIN_16.on()
            elif self.gpio_number == '17':
                PIN_17.on()
            elif self.gpio_number == '18':
                PIN_18.on()
            elif self.gpio_number == '19':
                PIN_19.on()
            elif self.gpio_number == '20':
                PIN_20.on()
            elif self.gpio_number == '21':
                PIN_21.on()
            elif self.gpio_number == '22':
                PIN_22.on()
            elif self.gpio_number == '23':
                PIN_23.on()
            elif self.gpio_number == '24':
                PIN_24.on()
            elif self.gpio_number == '25':
                PIN_25.on()
            elif self.gpio_number == '26':
                PIN_26.on()
            elif self.gpio_number == '27':
                PIN_27.on()

        elif self.state == '0':

            if self.gpio_number == '2':
                PIN_2.off()
            elif self.gpio_number == '3':
                PIN_3.off()
            elif self.gpio_number == '4':
                PIN_4.off()
            elif self.gpio_number == '5':
                PIN_5.off()
            elif self.gpio_number == '6':
                PIN_6.off()
            elif self.gpio_number == '7':
                PIN_7.off()
            elif self.gpio_number == '8':
                PIN_8.off()
            elif self.gpio_number == '9':
                PIN_9.off()
            elif self.gpio_number == '10':
                PIN_10.off()
            elif self.gpio_number == '11':
                PIN_11.off()
            elif self.gpio_number == '12':
                PIN_12.off()
            elif self.gpio_number == '13':
                PIN_13.off()
            elif self.gpio_number == '14':
                PIN_14.off()
            elif self.gpio_number == '15':
                PIN_15.off()
            elif self.gpio_number == '16':
                PIN_16.off()
            elif self.gpio_number == '17':
                PIN_17.off()
            elif self.gpio_number == '18':
                PIN_18.off()
            elif self.gpio_number == '19':
                PIN_19.off()
            elif self.gpio_number == '20':
                PIN_20.off()
            elif self.gpio_number == '21':
                PIN_21.off()
            elif self.gpio_number == '22':
                PIN_22.off()
            elif self.gpio_number == '23':
                PIN_23.off()
            elif self.gpio_number == '24':
                PIN_24.off()
            elif self.gpio_number == '25':
                PIN_25.off()
            elif self.gpio_number == '26':
                PIN_26.off()
            elif self.gpio_number == '27':
                PIN_27.off()
