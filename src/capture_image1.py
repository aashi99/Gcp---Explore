
import cv2
import numpy as np

def capturing_image():
	windowname = "Vedio Feed"
	cv2.namedWindow(windowname)
	cap = cv2.VideoCapture(0)

	if cap.isOpened():
	    ret, frame = cap.read()
	else:
	    ret = False

	while ret:
	    ret, frame = cap.read()
        print("frame is ..........")
	    print(frame)
	    #output = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	    '''#low = np.array([100,50,50])
	    #high = np.array([140,255,255])
	    low = np.array([100,0,0])
	    high = np.array([255,0,0])

	    image_mask = cv2.inRange(output, low, high)
	    output = cv2.bitwise_and(frame, frame, mask=image_mask)

	    inv = cv2.bitwise_not(frame)'''
	    cv2.imshow("Original",frame)
	    '''cv2.imshow("Masked",image_mask)
	    cv2.imshow("Color Tracking",output)'''
	    if cv2.waitKey(1)==27:
		cv2.imwrite("image_to_be_processed.jpg", frame)
		# return frame
		break;
	cv2.destroyAllWindows()
	cap.release()
capture_image1.py
Displaying capture_image1.py.
