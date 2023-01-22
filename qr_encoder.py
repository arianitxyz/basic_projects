import qrcode
import image

data = 'the quick brown fox jumped over the lazy dog'

qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)
image = qr.make_image(fill_color='red', back_color='white')
image.save('DemoDirectory/myqrcode.png')
