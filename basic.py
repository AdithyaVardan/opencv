import cv2 as cv
img=cv.imread('photos/cat1.jpg')
cv.imshow('cat',img)

#grey
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#blur
blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#edge cascade
canny=cv.Canny(blur,125,175)
cv.imshow("Casked",canny)

#dialationg the images
dialate=cv.dilate(canny,(3,3),iterations=1)
cv.imshow("dialate",dialate)

#eroded
eroded=cv.erode(dialate,(3,3),iterations=1)
cv.imshow("eroded",eroded)

#resize
resized=cv.resize(img,(185*2,275*2),interpolation=cv.INTER_CUBIC)
cv.imshow("resized",resized)

#dcrop
cropped=img[50:125,75:200]
cv.imshow("crop",cropped)
cv.waitKey()
