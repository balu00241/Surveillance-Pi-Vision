# main.py
import cv2
from camera_feed.capture import initialize_camera
from motion_detection.motion_detection import detect_motion
from motion_detection.recording import save_video
from utils.email_alerts import send_alert
from utils.helpers import log_event

def main():
    cap = initialize_camera()
    if cap is None:
        log_event("Failed to initialize camera.")
        return

    first_frame = None

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            motion_detected, first_frame = detect_motion(frame, first_frame)

            if motion_detected:
                log_event("Motion detected!")
                send_alert("Motion detected at your property!")
                save_video(frame)
                # Optionally, upload to cloud storage
                # upload_to_cloud('saved_videos/output.avi')

            cv2.imshow('Smart Surveillance System', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
