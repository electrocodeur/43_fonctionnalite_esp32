from machine import TouchPad, Pin, lightsleep
import time

touch = TouchPad(Pin(4))
led = Pin(2, Pin.OUT)
threshold = 400

while True:
    val = touch.read()
    if val < threshold:
        led.on()
        time.sleep(1)
        led.off()
    lightsleep(500)
