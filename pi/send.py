import socket, cv2, pickle, struct, os

HOST = "192.168.43.243"
PORT = 8081

def sendImg(host, port, path):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(10)
    #print("dinliyor")
    clientSocket, addr = s.accept()
    #print("Connected")
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    data = pickle.dumps(img)
    message_size = struct.pack("Q", len(data))
    #print(len(data))
    clientSocket.sendall(message_size + data)

    s.shutdown(socket.SHUT_RDWR)
    s.close()


#sendImg(HOST, PORT, "/home/pi/development/captures/" + sorted(os.listdir("/home/pi/development/captures/"), reverse=True)[0])
