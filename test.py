import socket
import time


def iniciar_ami(username, secret):
    s.send("Action: Login\n".encode())
    comando = "Username: " + username + "\n"
    s.send(comando.encode())
    comando = "Secret: " + secret + "\n"
    s.send(comando.encode())
    s.send("\n".encode())

def llamar(interno):
    s.send("Action: Originate\n".encode())
    comando = "Channel: SIP/" + str(interno) + "\n"
    s.send(comando.encode())
    s.send("Context: from-internos\n".encode())
    s.send("Exten: 500\n".encode())
    s.send("Priority: 1\n".encode())
    s.send("\n".encode())

def finalizar_ami():
    s.send("Action: Logout\n".encode())
    s.send("\n".encode())

def listar():
    s.send("Action: PeerlistComplete\n".encode())
    s.send("\n".encode())


s = socket.socket()
s.connect(("192.168.1.30",5038))

iniciar_ami("emanuel","1234")

listar()
#llamar(503)

#time.sleep(1)

finalizar_ami()
