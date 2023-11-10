import cv2

cap = cv2.VideoCapture('C:\\Users\\Bekir\\Desktop\\projects\\keygenerator\\Icardi.mp4')
font = cv2.FONT_HERSHEY_SIMPLEX
font_color = (0, 255, 255)  # BGR color format
font_size = 1
font_thickness = 2

while True:
    ret, frame = cap.read()
    cv2.putText(frame, 'TEXT ON VIDEO', (50, 50), font, font_size, font_color, font_thickness, cv2.LINE_4)
    cv2.imshow('video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()