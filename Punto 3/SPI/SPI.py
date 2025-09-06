from machine import Pin, SPI
import utime

spi = SPI(0, baudrate=1000000, polarity=0, phase=0, sck=Pin(2), mosi=Pin(3), miso=Pin(4))
cs = Pin(5, Pin.OUT)

while True:
    cs.value(0)
    spi.write(b'1')   # Enviar 1 = encender LED
    cs.value(1)
    utime.sleep(2)

    cs.value(0)
    spi.write(b'0')   # Enviar 0 = apagar LED
    cs.value(1)
    utime.sleep(2)
