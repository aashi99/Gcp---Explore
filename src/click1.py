def click2():
    import cv2

    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0

    while True:
        ret, frame = cam.read()
	frame=cv2.rectangle(frame,(frame.shape[0]/2,frame.shape[0]/3),((3*frame.shape[1])/4,frame.shape[1]/2),(0,0,255),4)
	start_row,start_col=frame.shape[0]/2,frame.shape[0]/3
	end_row,end_col=3*frame.shape[1]/4,frame.shape[1]/2
	cropped=img[start_row:end_row,start_col:end_col]
        cv2.imshow("test", frame)
	cv2.imshow("cropped",cropped)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27 or img_counter == 1:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
	    cv2.imwrite(img_name,cropped)
            print("{} written!".format(img_name))
            img_counter += 1

            # print(frame)

    cam.release()
    cv2.destroyAllWindows()
    return (img_name)

img_name=click2()
print(img_name)
###################################


'''cv2.rectangle(img,(100,250),(1000,600),(0,0,255),5)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
