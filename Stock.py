# Stock.py

from urllib.request import urlopen
from bs4 import BeautifulSoup

Set = {}

def CheckStock(ID=0): # สร้าง function Set ค่าเริ่มต้นคือ 0
    url = 'https://www.set.or.th/th/home' # เว็ปที่เราสนใจ

    webopen = urlopen(url) # เปิดเว็ปโดยไม่ต้องเปิด chrome
    html_page = webopen.read() # อ่านข้อมูลในเว็ป
    webopen.close() # ปิดเว็ป
    data = BeautifulSoup(html_page,'html.parser') # แปลงโค้ดให้ bs4 ช่วยแปล(เป็นคำสั่งเฉพาะอ้างอิง Doc)


    s_title = data.find_all('div',{'class':'d-flex link'}) # หาชื่อดัชนีหุ้น โดยหา tag "div" filter class | final_all ผลลัพธ์จะได้เป็น List
    s_value = data.find_all('span',{'class':'ms-auto'}) # หาค่าดัชนีหุ้น โดยหา tag "span" filter class | final_all ผลลัพธ์จะได้เป็น List


    s_Name = s_title[ID].text.strip() # dcode ออกมาเป็นชื่อ | .text คือตัดคำที่เป็นภาษาเทคนิคออกเหลือแต่คำหน้าเว็ป
    s_Values = s_value[ID].text.strip() # dcode ออกมาเป็นค่าดัชนี | .text คือตัดคำที่เป็นภาษาเทคนิคออกเหลือแต่คำหน้าเว็ป

    try:
        Set[s_Name] = s_Values  # ใส่ ชื่อและค่าของหุ้นลงลงใน Dictionary
    except:
        pass




for i in range(10):
    try:
        CheckStock(i) # ใส่ค่าลงใน Dictionary เป็นชุด
    except:
        pass
    

print(Set['SET'])












