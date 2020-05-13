import socket 

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((socket.gethostname(),6000))

s.listen(5)
print("Connecting to clients............")
while True:
    conn,address = s.accept()
    print(f"connection to the {address} is established")

    conn.send(("Welcome to socket programming").encode('utf-8'))
    i = ""
    while i!="quit":
        talk="@server: "
        i = input("@server: ")
        talk += i
        conn.send(bytes(talk,'utf-8'))
        msg = conn.recv(1024)
        print(msg.decode())
s.close()
