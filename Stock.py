# Stock.py

from urllib.request import urlopen
from bs4 import BeautifulSoup

import csv # import csv
from datetime import datetime # import datetime ที่อยู่ใน datetime package

Set = {}

def writetocsv(data):

    date = datetime.now().strftime('%Y-%m-%d')
    
    with open('data_Stock-{}.csv'.format(date),'a',newline='',encoding='utf-8') as file: #เปิด data-Stock.csv และเติมข้อมูลแบบ append 
        filewriter = csv.writer(file) # เขียน file csv เข้าไป
        filewriter.writerow(data) # เขียนข้อมูลแบบครั้งละ 1 บรรทัด



def CheckStock(ID=0): # สร้าง function Set ค่าเริ่มต้นคือ 0
    url = 'https://www.set.or.th/th/home' # เว็ปที่เราสนใจ

    webopen = urlopen(url) # เปิดเว็ปโดยไม่ต้องเปิด chrome
    html_page = webopen.read() # อ่านข้อมูลในเว็ป
    webopen.close() # ปิดเว็ป
    data = BeautifulSoup(html_page,'html.parser') # แปลงโค้ดให้ bs4 ช่วยแปลเพื่อเก็บโครงสร้างข้อมูล เป็นคำสั่งสำเร็จรูป


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
    

for k,v in Set.items(): # i คือลำดับที่ | เขียนข้อมูลลงใน csv
    data = [k,v]
    writetocsv(data)














