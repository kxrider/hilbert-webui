import socket
import struct

class TcpSocket:
    MAX_BUFF_SIZE = 1024
    FORMAT = 'utf-8'

    def __init__(self, port = 0):
        ip = socket.gethostbyname(socket.gethostname())
        self.thisPC = (ip, port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.clientSock = 0
        #self.clientAddr = 0
        if port != 0:
            self.socket.bind(self.thisPC)
        
    
    def listenForClients(self):
        self.socket.listen()

    def acceptClient(self):
        clientsock, addr = self.socket.accept() # close this socket to disconnect
        return clientsock, addr
    
    def connectToServer(self, addr):
        self.socket.connect(addr)
    
    # reliable sending
    # buffer[1, size] must be actual data
    def sendRaw(self, sock, byteString):
        size = len(byteString)
        amountSent = 0
        while amountSent < size:
            sent = sock.send(byteString[amountSent:])
            
            if sent == 0:
                raise RuntimeError("socket connection broken")
            
            amountSent += sent
    
    def recvRaw(self, sock, size):
        chunks = []
        bytes_recd = 0
        while bytes_recd < size:
            chunk = sock.recv(min(size - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)

    def sendData(self, sock, byteString):
        size = len(byteString)
        byteSize = struct.pack('<I', size)
        self.sendRaw(sock, byteSize)
        self.sendRaw(sock, byteString)

    def recvData(self, sock):
        byteSize = self.recvRaw(sock, 4)
        size = struct.unpack('<I', byteSize)[0]
        msg = self.recvRaw(sock, size)
        
        # DC message stuff

        return msg
    
    def sendMsg(self, sock, msg):
        byteString = msg.encode(TcpSocket.FORMAT)
        self.sendData(sock, byteString)
    
    def recvMsg(self, sock):
        byteString = self.recvData(sock)
        msg = byteString.decode(TcpSocket.FORMAT)
        return msg
