from machine import Pin,SoftI2C
import ssd1306
import dht
import time

i2c=SoftI2C(sda=Pin(22),scl=Pin(23))

oled = ssd1306.SSD1306_I2C(128,32,i2c)

def Calculate_data():
    sensor_pin=dht.DHT11(Pin(15))
    sensor_pin.measure()
    global temp
    temp=sensor_pin.temperature()
    global hum
    hum=sensor_pin.humidity()
    print("Temperature : ",temp,"Humidity : ",hum)


while True:
    Calculate_data()
    oled.text("Temperature :",0,0)
    oled.text(str(temp),110,0)
    oled.text("Humidity : ",0,10)
    oled.text(str(hum),80,10)
    oled.show()
    time.sleep(1)
