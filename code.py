# Circuit Playground NeoPixel
import time
import board
import neopixel
import microcontroller
import touchio

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.01, auto_write=False)

touch1 = touchio.TouchIn(board.A1)
touch2 = touchio.TouchIn(board.A2)
touch3 = touchio.TouchIn(board.A3)
touch4 = touchio.TouchIn(board.A4)
touch5 = touchio.TouchIn(board.A5)
touch6 = touchio.TouchIn(board.A6)
touch7 = touchio.TouchIn(board.A7)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

def wait_any_touch():
    touched = False
    while not touched:
        if touch1.value or touch2.value or touch3.value or touch4.value or touch5.value or touch6.value or touch7.value:
            print("touch detected")
            # light up one pixel to indicate touch detected
            pixels[4] = CYAN
            pixels.show()
            touched = True
        time.sleep(0.1)
        pixels[4] = OFF
        pixels.show()
    return True

def one_green():
    pixels[0] = GREEN
    pixels[1] = OFF
    pixels[2] = OFF
    pixels.show()

def one_yellow():
    pixels[0] = OFF
    pixels[1] = YELLOW
    pixels[2] = OFF
    pixels.show()

def one_redyellow():
    pixels[0] = OFF
    pixels[1] = YELLOW
    pixels[2] = RED
    pixels.show()

def one_red():
    pixels[0] = OFF
    pixels[1] = OFF
    pixels[2] = RED
    pixels.show()

def two_green():
    pixels[9] = GREEN
    pixels[8] = OFF
    pixels[7] = OFF
    pixels.show()

def two_yellow():
    pixels[9] = OFF
    pixels[8] = YELLOW
    pixels[7] = OFF
    pixels.show()

def two_red():
    pixels[9] = OFF
    pixels[8] = OFF
    pixels[7] = RED
    pixels.show()

# initial: light up all traffic lights as demo for 1 second.
pixels[0] = GREEN
pixels[1] = YELLOW
pixels[2] = RED

pixels[9] = GREEN
pixels[8] = YELLOW
pixels[7] = RED

pixels.show()
time.sleep(1)
one_green()
two_red()
pixels.show()

while True:
    wait_any_touch()
    time.sleep(1)
    one_yellow()
    time.sleep(1)
    one_red()
    time.sleep(0.5)
    two_green()
    time.sleep(2)
    two_yellow()
    time.sleep(2)
    two_red()
    time.sleep(1)
    one_redyellow()
    time.sleep(1)
    one_green()