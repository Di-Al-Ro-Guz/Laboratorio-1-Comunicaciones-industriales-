from machine import Pin, I2C
import utime

i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=40000)

leds = [Pin(16, Pin.OUT), Pin(17, Pin.OUT), Pin(18, Pin.OUT)]

while True:
    data = i2c.readfrom(8, 1)  # Leer 1 byte del esclavo
    if data:
        val = data[0]
        bits = [(val >> i) & 1 for i in range(7, 4, -1)]
        for i, led in enumerate(leds):
            led.value(bits[i])
    utime.sleep(0.2)
