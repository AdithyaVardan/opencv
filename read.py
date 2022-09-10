import cv2 as cv
#img=cv.imread('Photos/cat2.jpg')
#cv.imshow('Cat',img)
def rescaleFrame(frame,scale=.25):
    #images and videos
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimentions=(width,height)
    return cv.resize(frame,dimentions,interpolation=cv.INTER_AREA)
capture=cv.VideoCapture('videos/earth.mp4',)
def changeRes(width,height):
    #live videos only
    capture.set(3.width)
    capture.set(4,height)

while True:
    isTrue,frame=capture.read()
    frame_r=rescaleFrame(frame)
    #cv.imshow('video',frame)
    cv.imshow('video resized',frame_r)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
