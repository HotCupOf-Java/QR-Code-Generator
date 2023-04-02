import qrcode

def  qrcode_gen(text):
     qr = qrcode.QRCode(
          version = 1,
          error_correction = qrcode.ERROR_CORRECT_L,
          box_size=10,
          border=4,
     )

     
     qr.add_data(text)
     qr.make(fit=True)
     img = qr.make_image(fill_color="black", back_color="white")
     img.save("qrimg.png")

print("QR Code Generator. File is created in this project file. \n")
user_input = str(input("Enter the text to be converted into a QR Code: "))

qrcode_gen(user_input)