from picamera import PiCamera
from PIL import Image
from io import BytesIO
import time

stream = BytesIO()
camera = PiCamera()
camera.start_preview()
time.sleep(2)
camera.capture(stream, format="jpeg")
stream.seek(0)
with open("test.jpeg", "wb") as f:
    f.write(stream.read())
