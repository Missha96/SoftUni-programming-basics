import pyqrcode
import png
from pyqrcode import QRCode

adrress = 'https://www.imot.bg/obiava-2m176941598038113-dava-pod-naem-magazin-grad-sofiya-tsentar'

url = pyqrcode.create(adrress)

url.png('test.png')


