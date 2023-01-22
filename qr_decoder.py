from pyzbar.pyzbar import decode
from PIL import Image

image = Image.open('DemoDirectory/myqrcode.png')
result = decode(image)
print(result)
