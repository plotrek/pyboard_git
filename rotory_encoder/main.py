import machine
from ssd1306 import SSD1306
from rotary_irq_pyb import RotaryIRQ
import math
import time

height = 64
wight = 128
line_lenght = 20
middlex = wight / 2
middley = height / 2

r = RotaryIRQ(pin_num_clk='X1',
              pin_num_dt='X2',
              min_val=-9,
              max_val=9,
              reverse=False,
              range_mode=RotaryIRQ.RANGE_WRAP)

display = SSD1306(pinout={'sda': 'X10'},
                  height=64,
                  external_vcc=False)
s = pyb.Servo(3)

display.poweron()
display.init_display()

while True:
    display.clear()
    angle = r.value()
    a = line_lenght * math.cos(math.pi * angle / 18) + middlex
    b = line_lenght * math.sin(math.pi * angle / 18) + middley
    display.draw_line(middlex, middley, a, b)
    display.display()
    s.angle(angle*10)
    print(angle*10)
    time.sleep(.1)
