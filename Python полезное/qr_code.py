import qrcode


img = qrcode.make('https://morphologistview.ru/blog/')
img.save("MV_QR.png")



