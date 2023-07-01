import socket

IP_ADDRESS = "192.168.1.110"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP_ADDRESS, 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()

    handshake = (clientsocket.recv(1024)).decode()

    if handshake != 'handshake':
        clientsocket.send("handshake refused".encode())
        clientsocket.close()
    else:
        print(f"Connected to {address}")

        clientsocket.send("1".encode())
        clientData = clientsocket.recv(1024)
        if clientData.decode() == '1':
            clientsocket.send("data pack 1".encode())
        elif clientData.decode() == '2':
            clientsocket.send("data pack 2".encode())
        else:
            clientsocket.send("No data".encode())

        clientsocket.close()
