from machine import UART, Pin
import utime

led_verde = Pin(15, Pin.OUT)
led_rojo  = Pin(16, Pin.OUT)

uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))  # UART1

def check_parity(byte):
    bits = bin(byte).count("1")
    return bits % 2  # 0 = par, 1 = impar

while True:
    if uart.any():
        data = uart.read(1)
        if data:
            val = data[0]
            if check_parity(val) == 0:  # paridad correcta
                led_verde.value(1)
                led_rojo.value(0)
            else:
                led_verde.value(0)
                led_rojo.value(1)
        utime.sleep(0.5)
