import cv2 as cv
import numpy as np
img = cv.imread('/home/khushi/Downloads/task (copy)/task.png')
grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
tem1 = cv.imread('/home/khushi/Downloads/task (copy)/red.png')
tem2 = cv.imread('/home/khushi/Downloads/task (copy)/green.png')
tem3 = cv.imread('/home/khushi/Downloads/task (copy)/yellow.png')

temo1 = cv.cvtColor(tem1, cv.COLOR_BGR2GRAY)
w1, h1 = temo1.shape[::-1]
temo2 = cv.cvtColor(tem2, cv.COLOR_BGR2GRAY)
w2, h2 = temo2.shape[::-1]
temo3 = cv.cvtColor(tem3, cv.COLOR_BGR2GRAY)
w3, h3 = temo3.shape[::-1]


res1 = cv.matchTemplate(grey_img, temo1, cv.TM_CCORR_NORMED)
res2 = cv.matchTemplate(grey_img, temo2, cv.TM_CCORR_NORMED)
res3 = cv.matchTemplate(grey_img, temo3, cv.TM_CCORR_NORMED)

print(tem1.shape)
print(tem2.shape)
print(tem3.shape)
min_1v, max_1v, min_1pt, max_1pt = cv.minMaxLoc(res1)
top_left1 = max_1pt
bottom_right1 = (top_left1[0]+w1 , top_left1[1]+h1)
print( "yellow" ,top_left1,bottom_right1)
cv.rectangle(img, top_left1, bottom_right1, (0, 0, 255), 3)
font = cv.FONT_HERSHEY_COMPLEX
img = cv.putText(img, 'yellow', (260,230), font, 1, (0,255,255), 1, cv.LINE_AA)
img = cv.circle(img,(512, 330), 1,(255,255,255),1)
cv.imshow("display window", img)
min_2v, max_2v, min_2pt, max_2pt = cv.minMaxLoc(res2)
top_left2 = max_2pt
bottom_right2 = (top_left2[0]+w2 , top_left2[1]+h2)
print("red" ,top_left2,bottom_right2)
cv.rectangle(img, top_left2, bottom_right2, (0, 255, 0), 3)
font = cv.FONT_HERSHEY_COMPLEX
img = cv.putText(img, 'red', (480,270), font, 1, (0,0,255), 1, cv.LINE_AA)
img = cv.circle(img,(787, 344), 1,(255,255,255),1)
cv.imshow("display window", img)
min_3v, max_3v, min_3pt, max_3pt = cv.minMaxLoc(res3)
top_left3 = max_3pt
bottom_right3 = (top_left3[0]+w3 , top_left3[1]+h3)
print("green" ,top_left3,bottom_right3)
cv.rectangle(img, top_left3, bottom_right3, (0, 255, 255), 3)
font = cv.FONT_HERSHEY_COMPLEX
img = cv.putText(img, 'green', (730,290), font, 1, (0,255,0), 1, cv.LINE_AA)
img = cv.circle(img,(316, 287), 1,(255,255,255),1)
cv.imshow("display window", img)

k = cv.waitKey(0)
if k == ord('q'): 
    
    exit()
    exit()
