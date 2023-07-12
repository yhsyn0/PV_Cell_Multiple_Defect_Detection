import picamera
import  pyshine as ps

class StreamThread():
	HOST = None
	PORT = None
	HTML = None
	server = None

	def __init__(self, HOST, PORT):
		super().__init__()

		
		self.HOST = HOST
		self.PORT = PORT
		self.HTML=	"""
					<html>
					<head>
					<title>PyShine Live Streaming</title>
					</head>

					<body>
					<center><h1> PyShine Live Streaming using PiCamera </h1></center>
					<center><img src="stream.mjpg" width='1640' height='1232' autoplay playsinline></center>
					</body>
					</html>
					"""

	def run(self):
		StreamProps = ps.StreamProps
		StreamProps.set_Page(StreamProps, self.HTML)
		address = (self.HOST, int(self.PORT))
		StreamProps.set_Mode(StreamProps,'picamera')    
		with picamera.PiCamera(resolution='1640x1232', framerate=30) as camera:
			output = ps.StreamOut()
			StreamProps.set_Output(StreamProps,output)
			camera.rotation = 180
			camera.start_recording(output, format='mjpeg')
			try:
				self.server = ps.Streamer(address, StreamProps)
				print('Server started at','http://'+address[0]+':'+str(address[1]))
				self.server.serve_forever()
			finally:
				camera.stop_recording()
				

	def stop(self):
		self.server.shutdown()
		print("Down")
		
