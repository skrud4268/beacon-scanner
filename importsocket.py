import socket
 
HOST = '14.63.172.130'
PORT = 9009
 
def getFileFromServer(filename):
    data_transferred = 0
 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST,PORT))
        sock.sendall(filename.encode())
 
        data = sock.recv(1024)
        if not data:
            print('file[%s]: do not exist' %filename)
            return
 
        with open('/var/www/html/' + filename, 'wb') as f:
            try:
                while  data:
                    f.write(data)
                    data_transferred += len(data)
                    data = sock.recv(1024)
            except Exception as e:
                print(e)
 
    print('sended [%s]. data transferred [%d]' %(filename, data_transferred))
 
filename = input('filename:')
getFileFromServer(filename)
