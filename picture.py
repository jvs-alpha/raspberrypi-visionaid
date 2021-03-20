from picamera import PiCamera
import time

camera = PiCamera()

for i in range(5):
    camera.start_preview()
    time.sleep(5)
    camera.capture("./image%s.jpg" % i)
camera.stop_preview()
