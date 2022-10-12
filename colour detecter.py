import cv2,numpy
def empty(a):
    pass

cv2.namedWindow("bar")
cv2.resizeWindow("bar",640,300)
cv2.createTrackbar("hue_min","bar",0,179,empty)
cv2.createTrackbar("hue_max","bar",179,179,empty)
cv2.createTrackbar("sat_min","bar",0,255,empty)
cv2.createTrackbar("sat_max","bar",255,255,empty)
cv2.createTrackbar("val_min","bar",0,255,empty)
cv2.createTrackbar("val_max","bar",255,255,empty)

img=cv2.VideoCapture(0)
while True:
    set,frame=img.read()
    img1=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    h_min=cv2.getTrackbarPos("hue_min","bar")
    h_max=cv2.getTrackbarPos("hue_max","bar")
    s_min=cv2.getTrackbarPos("sat_min","bar")
    s_max=cv2.getTrackbarPos("sat_max","bar")
    v_min=cv2.getTrackbarPos("val_min","bar")
    v_max=cv2.getTrackbarPos("val_max","bar")

    lower=numpy.array([h_min,s_min,v_min])
    upper=numpy.array([h_max,s_max,v_max])
    print(lower,upper)
    mask=cv2.inRange(img1,lower,upper)
    imgr=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("mask", mask)
    cv2.imshow("imgr",imgr)
    cv2.imshow("hsv",img1)
    cv2.imshow("img",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
