# Echo server program
import socket


def server():
    host = '127.1.1.1'       # symbolic name meaning all available interfaces
    port = 8080    # arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s = socket(AF_INET, SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    # print socket.getdefaulttimeout()
    # socket.setdefaulttimeout(60)
    conn, addr = s.accept()
    print 'Connected by', addr
    while 1:
        data = conn.recv(1024)
        if not data: break
        conn.sendall(data)
    conn.close()
    # conn, (rmip, rmpt) = s.accept()
    # while 1:
    #     print ("connected by ", str(rmip) + ": " + str(rmpt))
    #     data = conn.recv(1024)
    #     print ("What was delivered: ", data.decode())
    #
    #     if not data:
    #         break
    # conn.close()

if __name__ == "__main__":
    server()
