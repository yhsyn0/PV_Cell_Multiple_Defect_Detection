from picamera import PiCamera
import time
from fractions import Fraction
import datetime

cur_time = datetime.datetime.now()
stub = cur_time.strftime("%Y%m%d%H%M_low")
print(1)
camera = PiCamera(resolution=(3280, 2464), framerate=Fraction(1,6))
print(2)
# You can change these as needed. Six seconds (6000000)
# is the max for shutter speed and 800 is the max for ISO.
camera.shutter_speed = 10000000
camera.iso = 800
print(3)
time.sleep(11)
camera.exposure_mode = 'off'
print(4)
outfile = "%s.jpg" % (stub)
camera.capture(outfile)
print(5)
camera.close()
print(6)
