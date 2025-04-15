from machine import Pin
from gpio_lcd import GpioLcd
import time

def result():
    if j>k and j>p:
        lcd.putstr("BJP WON")

    if k>j and k>p:
        lcd.putstr("AAP WON")

    if p>j and p>k:
        lcd.putstr("CON WON")
                 
        


   
lcd = GpioLcd(
    rs_pin = Pin(10),
    enable_pin = Pin(11),
    d4_pin = Pin(6),
    d5_pin = Pin(7),
    d6_pin = Pin(8),
    d7_pin = Pin(9),
    num_lines = 2,
    num_columns = 16,
)
j=0
k=0
p=0
button_red=Pin(0,Pin.IN,Pin.PULL_DOWN)
button_green=Pin(1,Pin.IN,Pin.PULL_DOWN)
button_blue=Pin(2,Pin.IN,Pin.PULL_DOWN)
button_white=Pin(3,Pin.IN,Pin.PULL_DOWN)

lcd.putstr("BJP AAP CON")


while True:

    x=button_red.value()
    y=button_green.value()
    z=button_blue.value()
    r=button_white.value()



    if x == 1:
       lcd.move_to(0,1)
       j += 1
       lcd.putstr(str(j))
       print("voting is in progress!!!")
       print (j)
       time.sleep(1)

    if y == 1:
       lcd.move_to(6,1)
       k += 1
       lcd.putstr(str(k))
       print("voting is in progress!!!")
       print (k)
       time.sleep(1)

       
    if z == 1:
       lcd.move_to(11,1)
       p += 1
       lcd.putstr(str(p))
       print("voting is in progress!!!")
       print (p)
       time.sleep(1)

    if r==1:
        lcd.clear()
        lcd.move_to(0,0)
        result()  
    