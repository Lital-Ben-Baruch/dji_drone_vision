import cv2
IMAGE_WIDTH = 360
IMAGE_HEIGHT = 240
# Create a VideoCapture object with camera index 0 (default camera)
cap = cv2.VideoCapture(0)
# for my phone
# capture = cv2.VideoCapture("https://....../video")

# Set the width of the frame (ID 3)
cap.set(3, IMAGE_WIDTH)

# Set the height of the frame (ID 4)
cap.set(4, IMAGE_HEIGHT)

# Set the brightness (ID 10)
cap.set(10, 100)

while True:
    # Read a frame from the video capture
    success, img = cap.read()

    # start
    # Convert to grayscale
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Load the pre-trained face detection model (Haar cascade)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        text = f'size: w={w}, h={h} '

        font = cv2.FONT_HERSHEY_SIMPLEX
        # fontScale
        fontScale = 0.5
        # Blue color in BGR
        color = (255, 0, 0)
        # Line thickness of 2 px
        thickness = 2
        cv2.putText(img, text, (x + w//2, y), font, fontScale, color, thickness)
    # # Display the image
    # cv2.imshow('Face Detection', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # end

    # Display the frame in a window named "Live Feed"
    cv2.imshow("Face Detection", img)

    # Check for the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

# # Load the image
# image = cv2.imread('Picture1.jpg')
#
# # Convert to grayscale
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Load the pre-trained face detection model (Haar cascade)
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#
# # Detect faces
# faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)
#
# # Draw rectangles around each face
# for (x, y, w, h) in faces:
#     cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
#
# # Display the image
# cv2.imshow('Face Detection', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
