import os, sys
import socket
import re, select
import time, threading



SOCKS_VERSION = 5



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
					if port == 39698:
						MainC = client
						MainS = remote
					if "0301" in dataC.hex()[0:4] and len(dataC.hex()) >= 800:
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
								if True == True:
									Istarted = True
									Listt.append(dataS)
									t = threading.Thread(target=break_the_matchmaking, args=(ServerSocket,)).start()
								else:
									client.send(dataS)
					# [ End LevelUp ]
					
					if "1200" in dataS.hex()[0:4] and b"/mtuan(" in dataS:
						Increase = True
						threading.Thread(target=send_msg, args=(client, dataS.hex(), "[c][00FF00]Fb:Tũn Nhớ Em", 0.2)).start()
						threading.Thread(target=send_msg, args=(client, dataS.hex(), "[c][FFFF00]Tele:@Mtuan0802205", 0.3)).start()
						threading.Thread(target=send_msg, args=(client, dataS.hex(), "[c][FFFFFF]NgMinhTuấn", 0.4)).start()
					if client.send(dataS) <= 0:
						break


def mtuanbot():
	Proxy().runs('127.0.0.1', 57469)
		
mtuanbot()