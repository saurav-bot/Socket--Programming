import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),6000))

while True:
    msg = s.recv(1024)
    print(msg.decode("utf-8"))
    while True:
        msg="@client: "
        msg += input("@client: ")
        s.sendall(bytes(msg,'utf-8'))
        talk = s.recv(1024)
        print(talk.decode())

s.close()