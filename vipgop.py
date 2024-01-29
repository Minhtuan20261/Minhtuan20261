import datetime, os
list_3_day = ['Mtuan3day01', 'Mtuan3day02']
list_30_day = ['Mtuan30dayvip', 'Dlinh30dayvip']
tg = datetime.datetime.now()
def check(key, tg, tgsd):
    if key in list_3_day:
        check_tg = tg - tgsd
        if check_tg <= datetime.timedelta(days = 3):
            return 'key_3_day'
        else:
            return 'het_han'
    elif key in list_30_day:
        check_tg = tg - tgsd
        if check_tg <= datetime.timedelta(days = 30):
            return 'key_30_day'
        else:
            return 'het_han'
    else:
        return 'false'
while True:
    if not os.path.exists('keyvip.txt'):
        print("Mua Key Mtuan dz zalo:0961561407")
        key = input("Input Key Đã Mua: ")
        data = {
        'key': key,
        'time_use': tg
        }
        with open('keyvip.txt', 'w') as f:
            f.write(str(data))
        if key in list_3_day:
            print('Key 3 Day')
            break
        elif key in list_30_day:
            print('Key 30 Day')
            break
        else:
            print('Invalid Key!')
            os.remove('keyvip.txt')
            continue
        
    with open('keyvip.txt', 'r') as f:
        read_file = eval(f.read())
        key = read_file['key']
        tgsd = read_file['time_use']
     
    if check(key, tg, tgsd) == 'key_3_day':
        print('Key 3 Day')
        print('Thời Gian Còn Lại: {}'.format(datetime.timedelta(days = 3) - (tg - tgsd)))
        break
    elif check(key, tg, tgsd) == 'key_30_day':
        print('Key 30 Day')
        print('Thời Gian Còn Lại: {}'.format(datetime.timedelta(days = 30) - (tg - tgsd)))
        break
    elif check(key, tg, tgsd) == 'het_han':
        print('Key Đã Hết Hạn Rồi Cưng')
        os.remove('keyvip.txt')
        continue
    else:
        print('Invalid Key!')
        os.remove('keyvip.txt')
        continue

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
\033[1;32m║➢ Author   : NgMinhTuấn乂Dlinh                               \033[1;32m║➢ Cảm Ơn Ae Đã Mua Key
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