import qrcode
from PIL import Image
import qrcode.constants
qr=qrcode.QRCode(version=2, 
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=30,border=10)
qr.add_data("https://drive.google.com/drive/folders/1SYYxKi5Pnk24OjLjRMDk9SToLSE_-T8U?usp=drive_link")
qr.make(fit=True)
img=qr.make_image(fill_color="white", back_color="blue")
img.save("VDS ALL DETELSE.png")
