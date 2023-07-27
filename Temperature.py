# Stock.py

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.tmd.go.th/weather/province/bangkok' # เว็ปที่เราสนใจ

webopen = urlopen(url) # เปิดเว็ปโดยไม่ต้องเปิด chrome
html_page = webopen.read() # อ่านข้อมูลในเว็ป
webopen.close() # ปิดเว็ป

data = BeautifulSoup(html_page,'html.parser') # แปลงโค้ดให้ bs4 ช่วยแปล(เป็นคำสั่งเฉพาะอ้างอิง Doc)

print(data)