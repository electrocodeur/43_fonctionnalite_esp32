from machine import TouchPad, Pin
import time

touch = TouchPad(Pin(4))
led = Pin(2, Pin.OUT)

threshold = 400

while True:
    val = touch.read()
    print("Capacité :", val)
    if val < threshold:
        led.on()
    else:
        led.off()
    time.sleep(0.1)
