import cv2
import numpy as np

video_path = input("Enter the path of the video file: ")
text = input("Enter the text to add to the video: ")

cap = cv2.VideoCapture(video_path)
font = cv2.FONT_HERSHEY_SIMPLEX
font_color = (255, 255, 255)  # BGR color format
font_size = 1
font_thickness = 2

# Create a black background image with the same resolution as the video
background = np.zeros((1080, 1920, 3), dtype=np.uint8)

cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.moveWindow('video', 0, 0)

while True:
    ret, frame = cap.read()
    cv2.putText(frame, text, (50, 50), font, font_size, font_color, font_thickness, cv2.LINE_4)

    # Overlay the video frame on top of the black background
    x_offset = int((1920 - frame.shape[1]) / 2)
    y_offset = int((1080 - frame.shape[0]) / 2)
    background[y_offset:y_offset+frame.shape[0], x_offset:x_offset+frame.shape[1]] = frame

    cv2.imshow('video', background)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
