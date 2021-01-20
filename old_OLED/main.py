import time
from SSD1306 import SSD1306
import lcd_gfx
import bmp
import pyb
d = SSD1306()
sw = pyb.Switch()
acl = pyb.Accel()
d.poweron()
d.init_display()

while not sw():
  x,y,z=(acl.x(),acl.y(),acl.z())
  d.clear()
  d.p_string("x: "+str(x)+" y: "+str(y)+" z: "+str(z))
  d.display()
  time.sleep(1)

d.clear()
d.p_string('nie wkurwiaj mnie Wojtus bo ci zajebie')
d.display()
time.sleep(5)

d.clear()
lcd_gfx.drawTrie(42,2,21,23,63,23,d,1)
d.display()
time.sleep(1)

lcd_gfx.drawFillRect(10,12,20,20,d,1)
d.display()
time.sleep(1)

lcd_gfx.drawCircle(70,24,10,d,1)
d.display()
time.sleep(1)

d.clear()
bmp.bmp('new.bmp',d)
d.display()
time.sleep(5)

d.clear()
bmp.bmp('icon.bmp',d)
d.display()
time.sleep(5)
