import cv2
import numpy as np

# Prompt the user to enter the path of the video file and the text to add to the video
video_path = input("Enter the path of the video file: ")
text = input("Enter the text to add to the video: ")

# Load the video file
cap = cv2.VideoCapture(video_path)

# Define the font properties
font = cv2.FONT_HERSHEY_SIMPLEX
font_color = (0, 255, 255)  # BGR color format
font_size = 1
font_thickness = 2

# Create a black background image with a resolution of 1920x1080
background = np.zeros((1080, 1920, 3), dtype=np.uint8)

# Create a window to display the output video
cv2.namedWindow('output', cv2.WINDOW_NORMAL)
cv2.moveWindow('output', 0, 0)

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Detect corners in the video frame using the Harris Corner Detection algorithm
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners = cv2.cornerHarris(gray, 2, 3, 0.04)
    corners = cv2.dilate(corners, None)
    corners = cv2.threshold(corners, 0.01 * corners.max(), 255, cv2.THRESH_BINARY)[1]
    corners = np.uint8(corners)
    contours, _ = cv2.findContours(corners, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    corners = np.float32([c[0] for c in contours])

    # Draw the corners on the video frame
    for i, corner in enumerate(corners):
        cv2.circle(frame, tuple(corner), 5, (0, 0, 255), -1)
        cv2.putText(frame, f'Corner {i+1}', tuple(corner), font, font_size, font_color, font_thickness, cv2.LINE_4)

    # Prompt the user to choose a corner to add the text
    corner_num = int(input(f"Enter the number of the corner to add the text (1-{len(corners)}): "))

    # Add the text to the chosen corner
    cv2.putText(frame, text, tuple(corners[corner_num-1]), font, font_size, font_color, font_thickness, cv2.LINE_4)

    # Overlay the video frame on top of the background
    x_offset = int((1920 - frame.shape[1]) / 2)
    y_offset = int((1080 - frame.shape[0]) / 2)
    background[y_offset:y_offset+frame.shape[0], x_offset:x_offset+frame.shape[1]] = frame

    # Display the output video
    cv2.imshow('output', background)

    # Exit the program if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the resources and close all windows
cap.release()
cv2.destroyAllWindows()
