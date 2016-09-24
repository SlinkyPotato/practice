# Echo client program
import socket
HOST = '127.1.1.1'   # the remote host
PORT = 8080          # the same port used by the server


def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    sendme = raw_input('What do you want to send?\n')
    s.sendall(sendme)
    data = s.recv(1024)
    s.close()
    print 'Received', repr(data)

if __name__ == "__main__":
    client()