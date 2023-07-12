# Taken from https://www.linkedin.com/pulse/creating-live-video-streaming-app-using-python-ranjit-panda

import cv2, pickle, socket, struct, signal, sys, os
#print(os.getpid())
HOST = '192.168.137.235'
PORT = 8088
if len(sys.argv) > 1:
    PORT = int(sys.argv[1])
#print(PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(10)

def handler(signum, frame):
    try: 
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).shutdown(socket.SHUT_RDWR)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).close()
    except OSError:
        exit()
    
def passVideo(s):
    clientSocket, addr = s.accept()
    
    if clientSocket:
        cap=cv2.VideoCapture(0)

    while(cap.isOpened()):
        ret, frame = cap.read()
        #frame = cv2.imread("/home/azarakuss/Downloads/6.jpg")
        data = pickle.dumps(frame)
        message_size = struct.pack("Q", len(data))

        try:
            clientSocket.sendall(message_size + data)
        except Exception as e:
            cap.release()
            #print("S")
            break
            
try:
    while True:
        #signal.signal(signal.SIGTSTP, handler)
        passVideo(s)
except KeyboardInterrupt:
    #print("c")
    exit()