import cv2, socket, pickle, struct

class StreamThread():
    HOST = None
    PORT = None
    s = None

    def __init__(self, HOST, PORT):
        super().__init__()
        self._run_flag_ = True

        self.HOST = HOST
        self.PORT = PORT

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.HOST, self.PORT))
        self.s.listen(10)

    def run(self):
        while(True):
            if self._run_flag_ == False:
                cap.release()
                break
            try:
                clientSocket, addr = self.s.accept()
            except OSError:
                cap.release()
                break

            if clientSocket:
                cap=cv2.VideoCapture(-1)
            while(cap.isOpened()):
                ret, frame = cap.read()
                data = pickle.dumps(frame)
                message_size = struct.pack("Q", len(data))

                try:
                    clientSocket.sendall(message_size + data)
                except Exception as e:
                    cap.release()
                    break

    def stop(self):
        self._run_flag_ = False
        self.s.shutdown(socket.SHUT_RDWR)
        self.s.close()
        print("Ending")
        return