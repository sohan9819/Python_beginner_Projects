import qrcode

# data = qrcode.make("http://bit.ly/IoTws_regform")
# data.save("registration.png")


qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=20,
                   border=2)

qr.add_data("https://registration_link")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")


# for making .svg file of qrcode
# import qrcode.image.svg

# factory = qrcode.image.svg.SvgPathImage
# svg_img = qrcode.make("Hello World!", image_factory=factory)
# svg_img.save("image.svg")
