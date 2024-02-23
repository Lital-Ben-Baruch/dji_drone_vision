# # connect the drone to the computer buy connect it to the wifi before executing this code

from djitellopy import Tello
import cv2


tello = Tello()

tello.connect()

tello.streamon()

while True:
    # Read the video stream frame by frame
    frame = tello.get_frame_read().frame
    frame = cv2.resize(frame, (360, 240))
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the frame
    cv2.imshow('Tello Video Stream', frame_rgb)
    cv2.waitKey(1)

    # Check for the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

