import pyqrcode
import png

data=pyqrcode.create(input("Enter the data you want to add : \n"))
data.png('code.png',scale=6)
print("QR code generated!")
