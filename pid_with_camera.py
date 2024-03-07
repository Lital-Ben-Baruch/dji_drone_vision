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

    # Convert to grayscale
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Load the pre-trained face detection model (Haar cascade)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)
    # Initialize variables to keep track of the largest face
    max_area = 0
    largest_face = None
    x_init = IMAGE_WIDTH // 2
    y_init = IMAGE_HEIGHT // 2


    for (x, y, w, h) in faces:
        current_area = w
        print(f'x={x}')
        # X range: [x_init-80, x_init+80] y range: [y_init - 80, y_init+80]
        if (x> x_init-80 and x< x_init+80) and (y> y_init -80 and y< y_init+80):
            located_face = (x, y, w, h)

    # init rect
    IMAGE_WIDTH = 360
    IMAGE_HEIGHT = 240
    cv2.rectangle(img, (x_init - 40, y_init - 40), (x_init + 40, y_init + 40), (0, 0, 255), 2)


    # Draw rectangle around  the biggest detection
    if located_face is not None:
        (x, y, w, h) = located_face
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        text_size = f'size: w={w}'
        text_loc = f'loc={x, y} '
        font = cv2.FONT_HERSHEY_SIMPLEX
        # fontScale
        fontScale = 0.5
        # Blue color in BGR
        color = (255, 0, 0)
        # Line thickness of 2 px
        thickness = 2
        cv2.putText(img, text_size, (x, y - 10), font, fontScale, color, thickness)
        cv2.putText(img, text_loc, (x, y + w + 15), font, fontScale, color, thickness)
    # Display the frame in a window named "Face Detection"
    cv2.imshow("Face Detection", img)

    # Check for the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
