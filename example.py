from picamera import PiCamera
import time

camera = PiCamera()

camera.start_preview()
camera.annotate_text = "JVS-ALPHA"
time.sleep(5)
camera.stop_preview()
