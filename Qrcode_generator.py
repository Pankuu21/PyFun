from turtle import fillcolor
import qrcode 
#img=qr.make("Top 20 Python Projects for #Beginners to Advanced - Full Walk Through")
#img.save("youtube.png")
from PIL import Image
qr=qrcode.QRCode(version=1,error_correction=qrcode.ERROR_CORRECT_H,box_size=20,border=4)
qr.add_data("hello i am pankaj badgujar and i have made this qr code ")
qr.make(fit=True)
img=qr.make_image(fill_color="yellow",back_color="blue")
img.save("open and see.png")