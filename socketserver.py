import SocketServer
from os.path import exists
 
HOST = ''
PORT = 9009
 
class MyTcpHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data_transferred = 0
        print('[%s] connected' %self.client_address[0])
        filename = self.request.recv(1024) 
        filename = filename.decode() 
 
        if not exists(filename): 
            return 
 
        print('file[%s] sending...' %filename)
        with open(filename, 'rb') as f:
            try:
                data = f.read(1024) 
                while data: 
                    data_transferred += self.request.send(data)
                    data = f.read(1024)
            except Exception as e:
                print(e)
 
        print('sended[%s], data transferred[%d]' %(filename,data_transferred))
 
 
def runServer():
    print('++++++start fileserver++++++')
    print("+++press Ctrl+C to terminate.")
 
    try:
        server = SocketServer.TCPServer((HOST,PORT),MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('++++++terminate fileserver.++++++')
 

runServer()

