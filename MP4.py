# import cv2
# RES =1000,800
# main_capture=cv2.VideoCapture(0)
# subtractor = cv2.createBackgroundSubtractorKNN()
# while True:
#     frame = main_capture.read()[1]
#     frame = cv2.resize(frame, RES, interpolation=cv2.INTER_AREA)
#     mask = subtractor.apply(frame ,1)
#     bitwise = cv2.bitwise_and(frame,frame,mask=mask)
#     cv2.imshow('oma',frame)
#     if cv2.waitKey(1)==27:
#         break



# import cv2
# RES =1000,800
# main_capture=cv2.VideoCapture(0)
# while True:
#     frame = main_capture.read()[1]
#     frame = cv2.resize(frame, RES, interpolation=cv2.INTER_AREA)
#     cv2.imshow('',frame)
#     if cv2.waitKey(1)==27:
#         break
# cv2.destroyAllWindows()

import cv2
r =1400,900
m=cv2.VideoCapture(0)
while True:
    f=m.read()[1]
    f=cv2.resize(f , r ,interpolation=cv2.INTER_AREA)
    cv2.imshow('okno',f)
    if cv2.waitKey(1)==27:
        break