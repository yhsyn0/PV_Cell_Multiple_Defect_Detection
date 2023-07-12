import os, socket, signal, time, threading
from picamera import PiCamera
from StreamThread import StreamThread
from send import sendImg
from datetime import datetime

print("ON NOW")

HOST = "192.168.43.243"
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(10)

t = None
th =  None

def runProcess(cmd):
    global t, th
    if cmd == "irServerRun" and t == None and th == None:
        t = StreamThread(HOST, 8088)
        th =  threading.Thread(target=t.run)
        th.start()
        print("Server Run")

    if cmd == "irServerKill" and t != None and th != None:
        print("Server Down")
        t.stop()
        t = None
        th =  None

    if cmd == "irTakePhoto":
        camera = PiCamera()
        camera.resolution = (3280, 2464)
        time.sleep(1)
        nowStr = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        camera.capture("/home/pi/development/captures/" + "image_" + nowStr + ".jpg")
        print("Captured")
        camera.close()
    
    if cmd == "irProcess":
        if t != None and th != None:
            #print("durdu")
            t.stop()
            t = None
            th =  None
            time.sleep(3)
            #print("Uyku bitti")

        # Burayı en son güncelle
        camera = PiCamera()
        camera.resolution = (3280, 2464)
        time.sleep(1)
        nowStr = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        camera.capture("/home/pi/development/captures/" + "image_" + nowStr + ".jpg")
        #print("Captured")
        camera.close()
        # ---
        sendImg(HOST, 8081, 
        	"/home/pi/development/captures/" + \
        	sorted(os.listdir("/home/pi/development/captures/"), reverse=True)[0])
        #print("gönderildi")
        if t == None and th == None:
            t = StreamThread(HOST, 8088)
            th =  threading.Thread(target=t.run)
            th.start()
            #print("başladı")

        #    print("dinliyor")print("DONE")

    if cmd == "shutdown":
        if t != None and th != None:
            t.stop()
            t = None
            th =  None
        exit()
    
    
def handler(signum, frame):
    try: 
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).shutdown(socket.SHUT_RDWR)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).close()
    except OSError:
        exit()

def reciveCmd(s):
    clientSocket, addr = s.accept()
    if clientSocket:
        try:
            runProcess(clientSocket.recv(2048).decode())
        except Exception as e:
            print(e)
            
try:
    while True:
        signal.signal(signal.SIGTSTP, handler)
        reciveCmd(s)
except KeyboardInterrupt:
    exit()
