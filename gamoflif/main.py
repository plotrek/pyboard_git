import pyb
from ssd1306 import SSD1306
import time
import gol

height = 64
width = 128
display = SSD1306(pinout={'sda': 'X10'},
                  height=height,
                  external_vcc=False)

sw = pyb.Switch()
display.poweron()
display.init_display()
led_red = pyb.LED(1)
led_red.on()
grid = gol.randomGrid(height, width)

while not sw():
    display.clear()
    for row in range(height):
        for index in range(width):
            if grid[row, index] == 255:
                display.set_pixel(row, index, 1)
    display.display()
    grid = gol.update(grid, height, width)
    time.sleep(1)

display.draw_text(1, 1, 'Hello World!', size=1, space=1)
display.display()
led_red.off()
