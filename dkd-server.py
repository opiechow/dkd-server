import socket
import json
import base64

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
while 1:
    s.listen(1)
    conn, addr = s.accept()
    print 'Connected by', addr
    fragments = []
    while 1:
        data = conn.recv(4096)
        fragments.append(data)
        if "DATA_END" in data: break
    jsonstring = "".join(fragments)[:-8]
    a = json.loads(jsonstring)
    print a
    if "photo" in a["authMethod"]:
        with open("zdj.png","wb") as f:
            f.write(base64.b64decode(a["data"]))
        print "photo saved"
    conn.send("ok")

