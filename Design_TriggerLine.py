import numpy as np
import cv2

cnt_up = 0
cnt_down = 0
count_up = 0
count_down = 0
state = 0


cap = cv2.VideoCapture("TestVideo.avi")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output1.mkv', fourcc, 20.0, (640, 480))


w = cap.get(3)
h = cap.get(4)
frameArea = h * w
areaTH = frameArea / 300
print('Area Threshold', areaTH)


# Lines coordinate for counting

line_up = int(1 * (h / 5))
line_down = int(4 * (h / 5))

up_limit = int(.5 * (h / 5))
down_limit = int(4.5 * (h / 5))

print("Red line y:", str(line_down))
print("Blue line y:", str(line_up))
line_down_color = (255, 0, 0)
line_up_color = (0, 0, 255)
pt1 = [0, line_down]
pt2 = [w, line_down]
pts_L1 = np.array([pt1, pt2], np.int32)
pts_L1 = pts_L1.reshape((-1, 1, 2))
pt3 = [0, line_up]
pt4 = [w, line_up]
pts_L2 = np.array([pt3, pt4], np.int32)
pts_L2 = pts_L2.reshape((-1, 1, 2))

pt5 = [0, up_limit]
pt6 = [w, up_limit]
pts_L3 = np.array([pt5, pt6], np.int32)
pts_L3 = pts_L3.reshape((-1, 1, 2))
pt7 = [0, down_limit]
pt8 = [w, down_limit]
pts_L4 = np.array([pt7, pt8], np.int32)
pts_L4 = pts_L4.reshape((-1, 1, 2))

# Variables
font = cv2.FONT_HERSHEY_SIMPLEX

while cap.isOpened():
    ret, frame = cap.read()

    # Display on Frames
    frame = cv2.polylines(frame, [pts_L1], False, line_down_color, thickness=4)
    frame = cv2.polylines(frame, [pts_L2], False, line_up_color, thickness=4)

    frame = cv2.polylines(frame, [pts_L3], False, (255, 255, 255), thickness=2)
    frame = cv2.polylines(frame, [pts_L4], False, (255, 255, 255), thickness=2)
    cv2.putText(frame, "Draw Trigger Line----TASK DONE", (10, 40), font, 1, (255, 255, 255), 2)

    out.write(frame)
    cv2.imshow('Frame', frame)

    # Press ESC to exit
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Closing
cap.release()
cv2.destroyAllWindows()

