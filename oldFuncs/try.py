import cv2
# vid = cv2.VideoCapture(0) # For webcam
vid = cv2.VideoCapture("http://192.168.43.243:9000/stream.mjpg") # For streaming links
while True:
	rdy,frame = vid.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	try:
		cv2.imshow('Video Live IP cam',gray)
		key = cv2.waitKey(1) & 0xFF
		if key ==ord('q'):
			break
	except:
		pass

vid.release()
cv2.destroyAllWindows()
