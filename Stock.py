# Stock.py

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.set.or.th/th/home' # เว็ปที่เราสนใจ

webopen = urlopen(url) # เปิดเว็ปโดยไม่ต้องเปิด chrome
html_page = webopen.read() # อ่านข้อมูลในเว็ป
webopen.close() # ปิดเว็ป

data = BeautifulSoup(html_page,'html.parser') # แปลงโค้ดให้ bs4 ช่วยแปล(เป็นคำสั่งเฉพาะอ้างอิง Doc)



s_title = data.find_all('div',{'class':'d-flex link'})
s_value = data.find_all('span',{'class':'ms-auto'}) #ให้คนหา tag "label" (เราต้องไปตรวจสอบ source code จากหน้าเว็ปก่อนว่าใช้ tag ประเภทไหน)และใน Dict คือ filter ผลลัพท์ออกมาเป็น list


s_Name = s_title[0].text.strip() # ตัวชื่อ Set100 อยู่ลับดับที่ 3 | .text คือตัดคำที่เป็นภาษาเทคนิคออกเหลือแต่คำหน้าเว็ป
s_Values = s_value[0].text.strip() # ตัวค่า Set100 อยู่ลับดับที่ 3 | .text คือตัดคำที่เป็นภาษาเทคนิคออกเหลือแต่คำหน้าเว็ป

#print('{} Index = {}'.format(Set100_Name,Set100_Values))

Index_Dict = {'Set':0,'Set50':1,'Set100':2}

def Set(v=0):
    if v==0:
        print('{} = {}'.format(s_title[0].text.strip(),s_value[0].text.strip()))
    elif v==50:
        print('{} = {}'.format(s_title[1].text.strip(),s_value[1].text.strip()))
    elif v==100:
        print('{} = {}'.format(s_title[2].text.strip(),s_value[2].text.strip()))
    else:
        print('กรุณากรอกใหม่ครับ')


    
Set(50)






