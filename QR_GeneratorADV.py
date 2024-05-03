#using qrcode class and PIL class

import qrcode as qr
from PIL import Image

data = input("Enter the link : ")
data2 = input("Enter the name of file to be saved as : ")
QR = qr.QRCode(version = 1,
               error_correction = qr.constants.ERROR_CORRECT_H,
               box_size = 10,
               border = 10)
QR.add_data(data)
QR.make(fit = True)
img = QR.make_image(fill_color = "white" , back_color = "black")
img.save(data2 +".png")
img.show()