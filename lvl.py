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
api_token='f63dd9b7-5b75-498d-b534-ca1b8b1eb02b'
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
   print(f'\033[1;95m║\033[1;33m Nhập Key Ngày Mà Bú Đi!  \033[1;95m{today} \033[1;95m║')
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
    Author:NgMinhTuấn乂TrVũMaiLinh乂DuyN乂ThànhMinh
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
\033[1;32m║➢ Author :NgMinhTuấn乂TrVũMaiLinh乂DuyN乂ThànhMinh          \033[1;32m║➢ Status    : Online
\033[1;34m╚═════════════════════════════════════════════════════════════════╝
"""
import os, sys
import socket
import re, select
import time, threading
import os
try:
    import requests,colorama,prettytable
except:
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system("pip install prettytable")
import threading, requests, ctypes, random, json, time, base64, sys, re
from prettytable import PrettyTable
import random
from time import strftime
from colorama import init, Fore
from urllib.parse import urlparse, unquote, quote
from string import ascii_letters, digits
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
#đánh dấu bản quyền
edit = vang+"]"+trang+"["+do+"[⟨⟩]"+trang+"]"+vang+"["+trang+" ➩ "+luc
edit1 = trang+"["+do+"[⟨⟩]"+trang+"]"+trang+" ➩ "+luc
os.system("cls" if os.name == "nt" else "clear")
banner="""
\033[1;34m╔═════════════════════════════════════════════════════════════════╗
"\033[1;95m"░▀█▀░█▀▄░█▀█░█▀█░░░█░█░█░█░░░█▄█░█▀█░▀█▀░░░█░░░▀█▀░█▀█░█░█
"\033[1;31m"░░█░░█▀▄░█▀█░█░█░░░▀▄▀░█░█░░░█░█░█▀█░░█░░░░█░░░░█░░█░█░█▀█
"\033[1;32m"░░▀░░▀░▀░▀░▀░▀░▀░░░░▀░░▀▀▀░░░▀░▀░▀░▀░▀▀▀░░░▀▀▀░▀▀▀░▀░▀░▀░▀
Author:NgMinhTuấn乂TrVũMaiLinh乂DuyN乂ThànhMinh
Status:Online
Tools Lvl Free Fire
\033[1;34m╠═════════════════════════════════════════════════════════════════╣

"""
for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 


SOCKS_VERSION = 5


# 76, 84 | Lvl = True | LT
# 76, 70 | Lvl = False | LF
# 77, 84 | SpamMsg = True | MT
# 77, 70 | SpamMsg = False | MF
# 73, 84 | SpamInv = True | IT
# 73, 70 | SpamInv = False | IF
# 71, 84 | GhostMode = True | GT
# 71, 70 | GhostMode =  False | GF
# 84, 84 | BackLastTeam = True | TT
# 84, 70 | BackLastTeam = False | TF
# 83, 84 | SpamBack =  True | ST
# 83, 70 | SpamBack =  False | SF
# 70, 84 | FakeFriend = True |  FT
# 70, 70 | FakeFriend = False |  FF



# [ LVL UP VAR ]
Listt = []
Increase = False
IsStarted = False
StartData = None
ServerSocket = None
StopData = b'\x03\x15\x00\x00\x00\x10\t\x1e\xb7N\xef9\xb7WN5\x96\x02\xb0g\x0c\xa8'


# [ LVL UP DEF ]
def timesleep():
	time.sleep(30)
	if IsStarted == True:
		ServerSocket.send(StartData)
		
def enter_game_and_RM():
	global Listt
	for data in Listt:
		MainC.send(data)
		Listt.remove(data)
	time.sleep(4)
	IStarted = False
	ServerSocket.send(StartData)
	t = threading.Thread(target=timesleep, args=()).start()

def break_the_matchmaking(server):
	server.send(StopData)
	server.send(StopData)
	server.send(StopData)
	t = threading.Thread(target=enter_game_and_RM, args=()).start()








def gen_msg(packet, content):
	content = content.encode("utf-8")
	content = content.hex()
	
	header = packet[0:8]
	packetLength = packet[8:10]
	packetBody = packet[10:32]
	pyloadbodyLength = packet[32:34]
	pyloadbody2 = packet[34:62]
	pyloadlength = packet[62:64]
	
	pyloadtext= re.findall(r"{}(.*?)28".format(pyloadlength) , packet[50:])[0]
	pyloadTile = packet[int(int(len(pyloadtext))+64):]
	
	NewTextLength = (hex((int(f"0x{pyloadlength}", 16) - int(len(pyloadtext)//2) ) + int(len(content)//2))[2:])
	if len(NewTextLength) == 1:
		NewTextLength = "0"+str(NewTextLength)
	
	NewpaketLength = hex(((int(f"0x{packetLength}", 16) - int((len(pyloadtext))//2) ) ) + int(len(content)//2) )[2:]
	NewPyloadLength = hex(((int(f"0x{pyloadbodyLength}", 16) - int(len(pyloadtext)//2)))+ int(len(content)//2) )[2:]
	NewMsgPacket = header + NewpaketLength + packetBody + NewPyloadLength + pyloadbody2 + NewTextLength + content + pyloadTile
	return str(NewMsgPacket)
	
def gen_msgv2(packet , replay):

	replay = replay.encode('utf-8')
	replay = replay.hex()
	
	
	hedar = packet[0:8]
	packetLength = packet[8:10] #
	paketBody = packet[10:32]
	pyloadbodyLength = packet[32:34]
	pyloadbody2= packet[34:54]
	
	pyloadlength = packet[54:62]
	pyloadtext= re.findall(r'{}(.*?)28'.format(pyloadlength) , packet[50:])[0]
	pyloadTile = packet[int(int(len(pyloadtext))+62):]
	
	
	NewTextLength = (hex((int(f'0x{pyloadlength}', 16) - int(len(pyloadtext)//2) ) + int(len(replay)//2))[2:])
	if len(NewTextLength) == 1:
		NewTextLength = "0"+str(NewTextLength)
	
	NewpaketLength = hex(((int(f'0x{packetLength}', 16) - int((len(pyloadtext))//2) ) ) + int(len(replay)//2) )[2:]
	NewPyloadLength = hex(((int(f'0x{pyloadbodyLength}', 16) - int(len(pyloadtext)//2)))+ int(len(replay)//2) )[2:]
	
	finallyPacket = hedar + NewpaketLength +paketBody + NewPyloadLength +pyloadbody2+NewTextLength+ replay + pyloadTile
	
	return str(finallyPacket)
	
def send_msg(sock, packet, content, delay:int):
	time.sleep(delay)
	try:
		sock.send(bytes.fromhex(gen_msg(packet, content)))
		sock.send(bytes.fromhex(gen_msgv2(packet, content)))
	except Exception as e:
		print(e)
		pass




class Proxy:
	
	def __init__(self):
		self.username = "Mtuandz"
		self.password = "Mtuandz"
		self.packet = b''
		self.sendmode = 'client-0-'
		
	def handle_client(self, connection):
		global Increase, SpamMsg
		version, nmethods = connection.recv(2)
		#print(version)
		#print(nmethods)
		if version == 76 and nmethods == 84:
			Increase = True
		if version == 76 and nmethods == 70:
			Increase = False
		if version == 77 and nmethods == 84:
			SpamMsg = True
			print("Spam Msg: On")
		if version == 77 and nmethods == 70:
			SpamMsg = False
			print("Spam Msg: Off")
		else:
			methods = self.get_available_methods(nmethods, connection)
			if 2 in set(methods):
				connection.sendall(bytes([SOCKS_VERSION, 2]))
			else:
				connection.sendall(bytes([SOCKS_VERSION, 0]))
				
			if not self.verify_credentials(connection,methods):
				return
			try:
				version, cmd, _, address_type = connection.recv(4)
				
				if address_type == 1:
					address = socket.inet_ntoa(connection.recv(4))
				elif address_type == 3:
					domain_length = connection.recv(1)[0]
					address = connection.recv(domain_length)
					address = socket.gethostbyname(address)
					name= socket.gethostname()
					
					
				port = int.from_bytes(connection.recv(2), 'big', signed=False)
				port2 = port
				
				try:
					
					remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					remote.connect((address, port))
					
					print("* Connected to {} {}".format(address, port))
					bind_address = remote.getsockname()
					
					addr = int.from_bytes(socket.inet_aton(bind_address[0]), 'big', signed=False)
					port = bind_address[1]
					reply = b''.join([
						SOCKS_VERSION.to_bytes(1, 'big'),
						int(0).to_bytes(1, 'big'),
						int(0).to_bytes(1, 'big'),
						int(1).to_bytes(1, 'big'),
						addr.to_bytes(4, 'big'),
						port.to_bytes(2, 'big')
					])
				except Exception as e:
					reply = self.generate_failed_reply(address_type, 5)
					
				connection.sendall(reply)
				
				self.botdev(connection, remote,port2)
			except:
				pass
		
	def generate_failed_reply(self, address_type, error_number):
		return b''.join([
			SOCKS_VERSION.to_bytes(1, 'big'),
			error_number.to_bytes(1, 'big'),
			int(0).to_bytes(1, 'big'),
			address_type.to_bytes(1, 'big'),
			int(0).to_bytes(4, 'big'),
			int(0).to_bytes(4, 'big')
		])
		
	def verify_credentials(self, connection,methods):
		
		if 2 in methods:
			version = ord(connection.recv(1))
			
			username_len = ord(connection.recv(1))
			username = connection.recv(username_len).decode('utf-8')
			
			password_len = ord(connection.recv(1))
			password = connection.recv(password_len).decode('utf-8')
			# print(username,password)
			if username == self.username and password == self.password:
				
				response = bytes([version, 0])
				connection.sendall(response)
				return True
				
			response = bytes([version, 0])
			connection.sendall(response)
			return True
			
		else:
			version = 1
			response = bytes([version, 0])
			try:
				connection.sendall(response)
			except BrokenPipeError:
				pass
			return True
			
	def get_available_methods(self, nmethods, connection):
		methods = []
		for i in range(nmethods):
			try:
				methods.append(ord(connection.recv(1)))
			except:
				pass
		return methods
		
	def runs(self, host, port):
		try:
			var = 0
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.bind((host, port))
			s.listen()
			while True:
				var = var+1
				conn, addr = s.accept()
				t = threading.Thread(target=self.handle_client, args=(conn,))
				t.start()
				
					
		except Exception as e:
			print(e)
			
	#connect
	def botdev(self, client, remote, port):
		while True:
			r, w, e = select.select([client, remote], [], [])
			if client in r or remote in r:
				if client in r:
					global MainC, MainS
					global StartData, ServerSocket, Increase, IsStarted, Listt
					dataC = client.recv(999999)
					if port == 39699:
						MainC = client
						MainS = remote
					if "0314" in dataC.hex()[0:4] and len(dataC.hex()) >= 800:
						StartData = dataC
						ServerSocket = remote
						t = threading.Thread(target=timesleep, args=()).start()
						
					if remote.send(dataC) <= 0:
						break

				if remote in r:
					dataS = remote.recv(999999)
					# [ Start LevelUp ]
					if "0300" in dataS.hex()[0:4]:
						if b"Ranked Mode" in dataS:
							pass
						else:
							if len(dataS.hex()) <= 100:
								pass
							else:
								if Increase == True:
									Istarted = True
									Listt.append(dataS)
									t = threading.Thread(target=break_the_matchmaking, args=(ServerSocket,)).start()
								else:
									client.send(dataS)
					# [ End LevelUp ]
					
					if "1200" in dataS.hex()[0:4] and b"/mlinh(" in dataS:
						Increase = True
						# GHI GIỐNG BIO TRONG FF....
						threading.Thread(target=send_msg, args=(client, dataS.hex(), "[c][FF0000]NgMinhTuấn " ,0.1)).start()
						threading.Thread(target=send_msg, args=(client, dataS.hex(), "[c][00FF00]DuyN " ,0.2)).start()
						threading.Thread(target=send_msg, args=(client, dataS.hex(), "[c][FFFF00]TrVũMaiLinh " ,0.3)).start()
						threading.Thread(target=send_msg, args=(client, dataS.hex(), "[c][FFFFFF]ThànhMinh " ,0.4)).start()
						threading.Thread(target=send_msg, args=(client, dataS.hex(), "[c][00FF00]Hoàn Tất Quá Trình Bật Tools Bạn Có Thể Sài Tools " ,0.5)).start()
					if client.send(dataS) <= 0:
						break

def vrxxbot():
	Proxy().runs('127.0.0.1', 7777)
		
vrxxbot()