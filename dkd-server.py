import socket
import json
import base64

def auth_check(idx, method):
    print "User id: %s" % idx
    print "Auth method: %s" % method
    return True

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
    if a["msgType"] == "passwdAuth":
        print base64.b64decode(a["authData"])
    elif a["msgType"] == "audioAuth":
        with open("sample.3gp","wb") as f:
            f.write(base64.b64decode(a["authData"]))
    elif a["msgType"] == "photoAuth":
        with open("photo.png","wb") as f:
            f.write(base64.b64decode(a["authData"]))
    if auth_check(a["userId"], a["msgType"]):
        conn.send("ok")
    else:
        conn.send("unauthorized")
