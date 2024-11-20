# camera_feed/capture.py
import cv2

def initialize_camera():
    cap = cv2.VideoCapture(0)  # '0' for the default webcam
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return None
    return cap
