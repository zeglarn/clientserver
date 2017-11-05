import socket
import sys

class Client:
    def __init__(self):
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def connect(self, address = None):
        # Connect the socket to the port where the server is listening
        if address == None:
            server_address = ('localhost', 10000)
        else:
            server_address = (address, 10000)

        print('connecting to {} port {}'.format(*server_address))
        try:
            self.sock.connect(server_address)
        except Exception as e:
            print(e)


    def sendMessage(self, message):
        try:
            self.sock.sendall(message)
            print("Message sent.")
        except Exception as e:
            print(e)

    def recv(self):
        totalData = None

        # While there is data to receive.
        while True:
            data = self.sock.recv(16)
            
            if not data:
                break
            
            totalData += data
        
        return totalData

    def disconnect(self):
        print("Closing socket.")
        self.sock.close()


class Server:
    def __init__(self):
        # Create a TCP/IP socket.
        self.sock = socket.socket()

        # Bind the socket to the port 10000.
        server_address = ('',10000)
        print("Starting up on {} port {}".format(*server_address))
        self.sock.bind(server_address)

        print("Listening for connections")
        self.sock.listen(1)

        self.conn, self.client_address = self.sock.accept()
        #print(self.connection, self.client_address)

    def sendMessage(self,message):
        if message:
            self.conn.sendall(message)
            print("Data sent!")

    
    def recv(self):
        totalData = b'' 

        # While there is data to receive.
        while True:
            data = self.conn.recv(2048)
            if not data:
                break
            totalData += data

        return totalData

    def disconnect(self):
        self.conn.close()

