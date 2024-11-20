# camera_feed/test_camera.py
import cv2
from camera_feed.capture import initialize_camera

cap = initialize_camera()

if cap:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Camera Test', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
