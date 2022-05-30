from website import create_app
from flask_socketio import SocketIO, emit
from threading import Thread
import TcpSocket

app = create_app()
iosock = SocketIO(app)
tcpsock = TcpSocket.TcpSocket(8080)
mcInstances = []
clientsock = None

print(f'tcp server listening on {tcpsock.thisPC[0]}:{tcpsock.thisPC[1]}')

def acceptConnection(sock):
    sock.listenForClients()
    clientsock, clientaddr = sock.acceptClient()
    sock.sendMsg(clientsock, 'connected')
    return clientsock
    
def updateTerm(tcpsocket, clientsock, io):
    msg = tcpsocket.recvMsg(clientsock)
    io.emit('updateTerm', {'data': msg})

def runApp():
    # if 'main' is imported elsewhere, equality not satisfied
    if __name__ == '__main__':
        #app.run(debug=True)
        iosock.run(app, debug=True)

#t1 = Thread(target=acceptConnection, args=(tcpsock))
#t2 = Thread(target=updateTerm)
#t3 = Thread(target=runApp)


updateTerm(tcpsock, acceptConnection(tcpsock), iosock)
runApp()
