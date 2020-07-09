"""This example prints to the serial console when the Circuit Playground is shaken."""
from adafruit_circuitplayground import cp

print("starting...")
counter = 0
while True:
    if cp.shake(shake_threshold=10):
        counter = counter + 1
        cp.red_led = True
        print("Shake detected!", counter)
    else:
        cp.red_led = False
