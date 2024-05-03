#qr generator

import qrcode as qr

link = input("Enter the link to generate QR code : ")
fileName = input("Enter the file name for the QR : ")

img = qr.make(link)
img.save(fileName +".png")