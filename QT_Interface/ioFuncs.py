import socket, struct, pickle, cv2, time
from datetime import datetime

HOST = "192.168.43.243"
PORT = 8081

def takeImg(host, port, path):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #print("bekliyor")
    clientSocket.connect((host, port))
    #print("Connected")
    data = b''
    payload_size = struct.calcsize("Q")
    #print(payload_size)
    #time1 = time.time()
    while len(data) < payload_size:
        #print(len(data))
        packet = clientSocket.recv(256 * 1024)

        if not packet:
            break
        data += packet
    #print("out")
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q", packed_msg_size)[0]
    #print(msg_size)

    while len(data) < msg_size:
        data += clientSocket.recv(4096 * 1024)
        #print(len(data))

    frame_data = data[:msg_size]
    data = data[msg_size:]    

    frame = pickle.loads(frame_data)
    #print(time.time()-time1)
    cv2.imwrite(path, frame)
    #print(time.time()-time1)



def sendCmd(host, port, cmd):
    sock = socket.socket()
    sock.connect((host, port))
    sock.sendall(bytes(cmd, "utf-8"))
    sock.close()


#nowStr = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
#takeImg(HOST, 8081, "/home/azarakuss/development/sources/captures/" + nowStr + ".jpg")
