import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
while 1:
    s.listen(1)
    conn, addr = s.accept()
    print 'Connected by', addr
    data = conn.recv(1024)
    print data
    conn.send("ok")

