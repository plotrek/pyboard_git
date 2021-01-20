import pyb
from ssd1306 import SSD1306
import time
import bmp

display = SSD1306(pinout={'sda':'X10'},
                  height=64,
                  external_vcc=False)

sw = pyb.Switch()
acl = pyb.Accel()
display.poweron()
display.init_display()
led_red = pyb.LED(1)
led_red.on()

while not sw():
  x,y,z=(acl.x(),acl.y(),acl.z())
  display.clear()
  display.draw_text("x: "+str(x)+" y: "+str(y)+" z: "+str(z))
  display.display()
  time.sleep(.1)

display.draw_text(1,1,'Hello World!',size=1,space=1)
display.draw_text(1,10,'this is TPYBoard ',size=1,space=1)
display.display()
led_red.off()
time.sleep(5)

display.clear()
bmp.bmp('icon.bmp', d)
display.display()
time.sleep(5)
 