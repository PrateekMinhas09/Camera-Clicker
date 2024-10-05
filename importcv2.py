import cv2
import time

def take_picture():
    # Access the webcam
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()

    if ret:
        # Save the picture as 'image.jpg'
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        cv2.imwrite(f'f:/ibm/IBM_SPSS_Statistics_27.0.1_IF026/IF026 Update/JRE/winPoint/image_{timestamp}.jpg', frame)

    cam.release()
    cv2.destroyAllWindows()

take_picture()