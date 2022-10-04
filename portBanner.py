import socket
import pyfiglet

def banner(ip, port):
   s = socket.socket()
   s.connect((ip, int(port)))
   s.settimeout(5)
   print(s.recv(1024))

xx = pyfiglet.figlet_format("MAERIH" , font="big")
print(xx)
ip = input("Please input IP to scan:")
port = str(input("Please enter Target's port:"))
banner(ip,port)
