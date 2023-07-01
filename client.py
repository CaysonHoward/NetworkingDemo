import socket
def main():
    con = ''
    while con != '1':
        con = input("Would you like to connect (y/n)")
        if con == 'y':
            connect()

def connect():
    IP_ADDRESS = "192.168.1.110"
    HANDSHAKE = 'handshake'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP_ADDRESS, 1234))

    s.send(HANDSHAKE.encode())
    dataFromServer = s.recv(1024)

    if len(dataFromServer) > 2:
        print(dataFromServer.decode())
    else:
        print('Enter a number or press 4 to close connection')
        data = input("Enter a number: ")

        if data == '4':
            s.close()
            return

        s.send(data.encode())

        # Receive data from server
        dataFromServer = s.recv(1024)

        # Print to the console
        print(dataFromServer.decode())
        s.close()

main()