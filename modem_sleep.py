import network
from machine import TouchPad, Pin
import time

touch = TouchPad(Pin(4))  
led = Pin(2, Pin.OUT)
threshold = 400

# Désactive le WiFi → mode Modem Sleep
sta_if = network.WLAN(network.STA_IF)
sta_if.active(False)

print("WiFi désactivé. En attente d’un réveil capacitif...")

# Attente d'un signal capacitif (main approchée)
while True:
    val = touch.read()
    if val < threshold:
        print("Détection capacitive : réveil")
        led.on()
        time.sleep(1)
        led.off()
        break  # Sortie de veille simulée
    time.sleep(0.2)

sta_if.active(True)
