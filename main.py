# # connect the drone to the computer buy connect it to the wifi before executing this code
from djitellopy import Tello
import cv2


tello = Tello()

tello.connect()

tello.streamon()

while True:
    # Read the video stream frame by frame
    frame = tello.get_frame_read().frame
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # start
    # Convert to grayscale
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Load the pre-trained face detection model (Haar cascade)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame_rgb, (x, y), (x + w, y + h), (255, 0, 0), 2)
        text = f'size: w={w} '

        font = cv2.FONT_HERSHEY_SIMPLEX
        # fontScale
        fontScale = 1
        # Blue color in BGR
        color = (255, 0, 0)
        # Line thickness of 2 px
        thickness = 2
        cv2.putText(frame_rgb, text, (x + w // 2, y), font, fontScale, color, thickness)

    # end

    # Display the frame
    cv2.imshow('Tello Video Stream', frame_rgb)
    cv2.waitKey(1)

    # Check for the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

