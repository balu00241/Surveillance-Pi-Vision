# motion_detection/recording.py
import cv2

def save_video(frame, output_path='saved_videos/output.avi'):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (640, 480))
    out.write(frame)
    out.release()
