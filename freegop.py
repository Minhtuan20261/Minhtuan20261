import requests,os,sys, time
from datetime import datetime
os.system('clear')
#màu
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
red='\u001b[31;1m'
yellow='\u001b[33;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
tim='\033[1;35m'
xanhlam='\033[1;36m'
xam='\033[1;30m'
black='\033[1;19m'
#key tool
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
#MÀU
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
from time import strftime
import os
import sys
import requests
import json
from time import sleep
from datetime import datetime, timedelta
import base64
import requests
import os
import time
try:
  from faker import Faker
  import requests
  from colorama import Fore, Style
  import re
  import pystyle
except:
  os.system("pip install faker")
  os.system("pip install requests")
  os.system("pip install colorama")
  os.system('pip install requests && pip install bs4 && pip install pystyle')
  print('__Vui Lòng Chạy Lại Tool__')
# màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
tim = '\033[1;39m'
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb = "\033[1;37m"
red = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'
import requests,os,time,re,json,uuid,random,sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pystyle import *
import requests, random
import base64, json,os
from time import sleep,strftime
import re,requests,os,sys
from time import sleep 
import requests, random
import uuid, re
from pystyle import Write,Colors
import socket
from datetime import datetime
hong = "\033[1;95m"
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
red = "\033[1;31m"
xnhac = "\033[1;36m"

#today nand clear
os.system('cls')
data_machine = []
today = date.today()
os.system('clear')
#daystime
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
vLong = trang + " " + trang + do + trang + trang + "=> "
banner = """\033[1;31m

\033
 "\033[1;31m"   ░█▄█░▀█▀░█░█░█▀█░█▀█
"\033[1;32m"░█░█░░█░░█░█░█▀█░█░█
"\033[1;95m"░▀░▀░░▀░░▀▀▀░▀░▀░▀░▀
"""
for h in banner:
       sys.stdout.write(h)
       sys.stdout.flush()
       sleep(0.000)

a=now.strftime("%d")
h=int(now.strftime("%d"))
ngay_trc=h-2
b=now.strftime("%m")
day=now.strftime("%d-%m-%Y")
today=now.strftime("%d-%m-%Y")
d=now.strftime("%d-%m")
ngay=int(strftime('%d'))
key1=str(ngay*11000922+2007)
key='Mtuan'+key1
def check_internet_connection():
    try:
        response = requests.get("https://www.google.com/", timeout=5)
        return True
    except requests.ConnectionError:
        return False
if not check_internet_connection():
    print("\n\033[1;31mVui Lòng Bật WIFI Để Sử Dụng Tool")
    sys.exit(1)
long_url=(f"https://mtuandz.000webhostapp.com/?key={key}")
api_token='91ee304a-0181-4d62-9589-8788140ec79b'
url=requests.get(f'https://web1s.com/api?token={api_token}&url={long_url}').json()
status=url['status']
link=url['shortenedUrl']
#lấy key
file_key=f'key_ngay{ngay_hom_nay}.txt'
file_key_cu=f'key_ngay{ngay_trc}.txt'
check_file_key=os.path.exists(file_key)
if check_file_key == False:
   print(f"{vLong}{luc}Đây Là Tool Free Nên Key Sẽ Thay Đổi Mỗi Ngày !!")
   print(f'{vLong}{luc}Link Lấy Key {trang}: {link} ')
   print(f'{vLong}{luc}Dán Link Ở Trên Vào Chrome Vượt Nhé')
   print(f'{trang}----------------------------------------------------------------')
   print(f'\033[1;95m┌───────────────────────────┐ ')
   print(f'\033[1;95m║\033[1;33m Nhập Key Ngày  \033[1;95m{today} \033[1;95m║')
   print (f"\033[1;95m└───────────────────────────┘")
   while(True):
      ma=input(f"{xnhac}Nhập Key : \033[1;33m")
      if ma == key:
         print(f'{vLong}{luc}Key Đúng Rồi')
         luu=open(file_key, 'a+')
         luu.write(ma)
         luu.close()
         break
      elif ma != key:
         print(f'{vLong}{do}Key Sai Rồi Kìa')
elif check_file_key == True:
    print(f'{vLong}{luc}Đang Lấy Key...',end='\r')
    sleep(1)
    k=open(file_key, 'r')
    ma=k.read()
    k.close()
    if ma == key:
        print(f'{vLong}{luc}Lấy Key Thành Công       ',end='\r')
        sleep(0.5)
    elif ma != key:
        if os.path.exists(file_key_cu) == True:
            os.system(f'rm {file_key_cu}')
        os.system(f'rm {file_key}')
        print(f'{vLong}{do}Key Sai Rồi Kìa         ')
        while(True):
            ma=input(f"{vLong}{luc}Nhập Key Bạn Đã Vượt\033[1;32m Ngày \033[1;37m{today}: \033[1;33m")
            if ma == key:
                print(f'{vLong}{luc} Key Đúng Rồi')
                luu=open(file_key, 'a+')
                luu.write(ma)
                luu.close()
                break
            elif ma != key:
                print(f'{vLong}{do}Key Sai Rồi Kìa        ')
                exit()
from time import strftime
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import uuid, re
from pystyle import Write,Colors
from bs4 import BeautifulSoup
import socket
from datetime import datetime
from rich.table import Table as me
from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup as parser
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
from rich import print as kui
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
import calendar
from time import sleep as jeda
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
import os,sys
os.system('clear')
import os, sys
import requests
import os, sys
import time
from time import strftime
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
ip = requests.post('https://api.proxyscrape.com/ip.php').text

import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
import os, sys
import requests
import os, sys
import time
from time import strftime
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
ip = requests.post('https://api.proxyscrape.com/ip.php').text
#đánh dấu bản quyền
ndp_tool="\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
#Config
__ZALO__ = '0961561407'
__ADMIN__ = 'Nguyễn Minh Tuấn'
__FACEBOOK__ = 'Tũn Nhớ Em'
__VERSION__ = '1.0'
os.system("cls" if os.name == "nt" else "clear")
loag = (f'{do}➩ {trang}Nếu thấy vào chậm hãy sài vpn !....')
for x in loag:
  sys.stdout.write(x)
  sys.stdout.flush()
  sleep(0.090)
os.system('espeak -a 300 "Have a nice day"')
logo = f"""

"\033[1;95m"░█▄█░▀█▀░█░█░█▀█░█▀█
"\033[1;31m"░█░█░░█░░█░█░█▀█░█░█
"\033[1;32m"░▀░▀░░▀░░▀▀▀░▀░▀░▀░▀
    Author:NgMinhTuấn乂Dlinh
    Status:Online

                        Ấn Enter Để Vào Tool
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            """
Anime.Fade(Center.Center(logo), Colors.red_to_yellow, Colorate.Vertical, enter=True)
sleep(0)
def banner():
 banner = f"""\033[0;31m
 
\033[1;34m╠═════════════════════════════════════════════════════════════════╣
"\033[1;95m"░█▄█░▀█▀░█░█░█▀█░█▀█
"\033[1;31m"░█░█░░█░░█░█░█▀█░█░█
"\033[1;32m"░▀░▀░░▀░░▀▀▀░▀░▀░▀░▀
\033[1;32m║➢ Author   : NgMinhTuấn乂Dlinh                               \033[1;32m║➢ Status    : Online
\033[1;34m╚═════════════════════════════════════════════════════════════════╝
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)
#tool
os.system("cls" if os.name == "nt" else "clear")
banner()
sleep(1)
print("\033[1;31m╔════════════════════════════════════════╗")
print("\033[1;31m║  \033[1;33mTool Gộp Khác \033[1;37m( Mtuan pro vip )\033[1;37m║")
print("\033[1;31m╚════════════════════════════════════════╝")
print("\033[1;31m[\033[1;37mMtuan\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m111\033[1;31m] \033[1;32mHDT-TOOL ")
print("\033[1;31m[\033[1;37mMtuan\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m222\033[1;31m] \033[1;32mHHOANG-TOOL ")
print("\033[1;31m[\033[1;37mMtuan\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m333\033[1;31m] \033[1;32mBNAM_HNAM-TOOL ")
print("\033[1;31m[\033[1;37mMtuan\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m444\033[1;31m] \033[1;32mPYPHONG-TOOL ")
print("\033[1;31m[\033[1;37mMtuan\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m555\033[1;31m] \033[1;32mNHD-TOOL ")
print("\033[1;31m[\033[1;37mMtuan\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m666\033[1;31m] \033[1;32mANORIN-TOOL ")
print("\033[1;31m[\033[1;37mMtuan\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m777\033[1;31m] \033[1;32mNULL_DEV-TOOL ")
print("\033[1;31m╔═════════════════════╗")
print("\033[1;31m║  \033[1;33mTool Trao Đổi Sub  \033[1;37m║")
print("\033[1;31m╚═════════════════════╝")
print("\033[1;31m[\033[1;37mMtuan\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m1\033[1;31m] \033[1;32mTool TDS Fb Full Job ")
print("\033[1;31m[\033[1;37mMtuan\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m2\033[1;31m] \033[1;32mTool TDS Tiktok ")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;31m╔═══════════════════════╗")
print("\033[1;31m║  \033[1;33mTool Tương Tác Chéo  \033[1;37m║")
print("\033[1;31m╚═══════════════════════╝")
print("\033[1;31m[\033[1;37mMtuan\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m3\033[1;31m] \033[1;32mTool TTC Pro5 Ver1 ")
print("\033[1;31m[\033[1;37mMtuan\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m4\033[1;31m] \033[1;32mTool TTC Pro5 Ver2 ")
print("\033[1;31m[\033[1;37mMtuan\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m5\033[1;31m] \033[1;32mTool TTC Instagram Vipig ")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;31m╔═════════════════════╗")
print("\033[1;31m║  \033[1;33mTool BUFF          \033[1;37m║")
print("\033[1;31m╚═════════════════════╝")
print("\033[1;31m[\033[1;37mMtuan\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m6\033[1;31m] \033[1;32mTool BUFF FOLLOW BẰNG PAGE PRO5 ")
print("\033[1;31m[\033[1;37mMtuan\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m7\033[1;31m] \033[1;32mTool BUFF VIEW TIKTOK  \033[1;34m(đang lỗi)")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;31m╔══════════════════════╗")
print("\033[1;31m║  \033[1;33mTool Share ảo + Spam\033[1;37m║")
print("\033[1;31m╚══════════════════════╝")
print("\033[1;31m[\033[1;37mMtuan\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m8\033[1;31m] \033[1;32mTool SHARE ẢO MAX SPEED ")
print("\033[1;31m[\033[1;37mMtuan\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m9\033[1;31m] \033[1;32mTool SPAM SMS VÀ CALL ")
print("\033[1;31m────────────────────────────────────────────────────────────")
chon = int(input('\033[1;31m[\033[1;37mMtuan\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;37m: \033[1;33m'))
if chon == 111 :
	exec(requests.get('https://run.mocky.io/v3/899008c5-17ff-488d-9318-9766886f9ac2').text)
if chon == 222 :
	exec(requests.get('https://run.mocky.io/v3/8400cea8-4705-4533-a006-f442c395cd7a').text)
if chon == 333 :
	exec(requests.get('https://run.mocky.io/v3/b211e1d0-0e61-4ca6-9bcf-96c61c2067dd').text)
if chon == 444 :
	exec(requests.get('https://run.mocky.io/v3/c304dfd9-bf08-419b-8e0f-c47b0d39a5a4').text)
if chon == 555 :
	exec(requests.get('https://run.mocky.io/v3/3cf81d8f-993d-4acc-b24a-89bf2f758fe9').text)
if chon == 666 :
	exec(requests.get('https://run.mocky.io/v3/34e13b9b-7c61-4feb-93f9-f93eb4ca9b61').text)
if chon == 777 :
	exec(requests.get('https://run.mocky.io/v3/b70f8c80-f955-4539-821f-9474ff4f4430').text)
if chon == 1 : #tooltds
	exec(requests.get('https://raw.githubusercontent.com/Minhtuan20261/Minhtuan20261/main/Tds.py').text)
if chon == 2 :
	exec(requests.get('https://raw.githubusercontent.com/Minhtuan20261/Minhtuan20261/main/Tdstik.py').text)
if chon == 3 : #toolttc
	exec(requests.get('https://raw.githubusercontent.com/Minhtuan20261/Minhtuan20261/main/ttcv1.py').text)
if chon == 4 :
	exec(requests.get('https://raw.githubusercontent.com/Minhtuan20261/Minhtuan20261/main/ttcv2.py').text)
if chon == 5 :
	exec(requests.get('https://raw.githubusercontent.com/Minhtuan20261/Minhtuan20261/main/ttcins.py').text)
if chon == 6 : #toolbuff
	exec(requests.get('https://raw.githubusercontent.com/Minhtuan20261/Minhtuan20261/main/buffflpage.py').text)
if chon == 7 :
 exec(requests.get('https://raw.githubusercontent.com/Minhtuan20261/Minhtuan20261/main/tiktik.py').text)
if chon == 8 : #tool share ảo + spamsms
 exec(requests.get('https://raw.githubusercontent.com/Minhtuan20261/Minhtuan20261/main/shareaomaxspeed.py').text)
if chon == 9 :
	exec(requests.get('https://raw.githubusercontent.com/Minhtuan20261/Minhtuan20261/main/sms2.py').text)
else :
	exit()