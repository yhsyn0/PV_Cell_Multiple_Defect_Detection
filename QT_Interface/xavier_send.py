import socket
def sendCmd(ip, port, cmd):
    sock = socket.socket()
    sock.connect((ip, int(port)))
    sock.sendall(bytes(cmd, "utf-8"))
    sock.close()

sendCmd('192.168.43.243', 8080, "irServerRun")


# irServerRun
# irServerKill
# shutdown
# irTakePhoto
#sock.connect(('192.168.43.243', 8080))
#sock.connect(('10.42.0.210', 8080))
#sock.connect(('', 8080))
#sock.connect(('192.168.3.3', 8080))