import cv2 as cv
import numpy as np

capture = cv.VideoCapture("video.mp4")
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
count = capture.get(cv.CAP_PROP_FRAME_COUNT)
fps = capture.get(cv.CAP_PROP_FPS)

print("Yukseklik:", height)
print("Genislik:", width)
print("Kare sayisi:", count)
print("FPS:", fps)

fourcc = cv.VideoWriter_fourcc(*"XVID")
out = cv.VideoWriter("video_kayit.avi", fourcc, fps, (int(width), int(height)))

while True:
    ret, frame = capture.read()
    if ret is True:
        cv.imshow("Video Giris", frame)
        out.write(frame)
        c = cv.waitKey(20)
        if c == 27:
            break
    else:
        break

capture.release()
out.release()
cv.destroyAllWindows()