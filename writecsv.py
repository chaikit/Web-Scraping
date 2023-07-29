# write_csv.py

import csv # import csv
from datetime import datetime # import datetime ที่อยู่ใน datetime package



def writetocsv(data):

    date = datetime.now().strftime('%Y-%m-%d')
    
    with open('data_Stock-{}.csv'.format(date),'a',newline='',encoding='utf-8') as file: #เปิด data-Stock.csv และเติมข้อมูลแบบ append 
        filewriter = csv.writer(file) # เขียน file csv เข้าไป
        filewriter.writerow(data) # เขียนข้อมูลแบบครั้งละ 1 บรรทัด

writetocsv(['SET','1,543.27'])     

