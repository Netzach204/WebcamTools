import cv2
import time
from webcam_video_stream import WebcamVideoStream

class WebcamTools:
    def __init__(self, vs, fps=30, resolution=(640, 480)):
        self.vs = vs
        self.fps = fps
        self.resolution = resolution
        self.is_recording = False
        self.video_out = None

    def capture_images(self):
        # Capture a single image from the webcam and save it
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        image_filename = f"image_{timestamp}.jpg"
        cv2.imwrite(image_filename, frame)
        print(f"Captured image: {image_filename}")

    def start_recording(self):
        # Start recording video from the webcam
        if not self.is_recording:
            self.is_recording = True
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            output_filename = f"output_video_{timestamp}.avi"
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            self.video_out = cv2.VideoWriter(output_filename, fourcc, self.fps, self.resolution)
            print(f"Recording started: {output_filename}")

    def stop_recording(self):
        # Stop recording video from the webcam
        if self.is_recording:
            self.is_recording = False
            if self.video_out is not None:
                self.video_out.release()
                print("Recording stopped")
                self.video_out = None

    def process_key(self, key):
        # Process user input keys
        if key == ord('c'):
            self.capture_images()
        elif key == ord('r'):
            if not self.is_recording:
                self.start_recording()
            else:
                self.stop_recording()
        elif key == ord('q'):
            self.stop_recording()
            self.vs.stop()
            cv2.destroyAllWindows()

if __name__ == '__main__':
    # Start the webcam stream
    vs = WebcamVideoStream().start()
    webcam_tools = WebcamTools(vs)

    while True:
        # Read a frame from the webcam stream
        grabbed, frame = vs.read()
        if not grabbed:
            break
        
        # Display the webcam stream
        cv2.imshow("Webcam Stream", frame)
        key = cv2.waitKey(1) & 0xFF

        # If recording, write the frame to the output video
        if webcam_tools.is_recording:
            webcam_tools.video_out.write(frame)

        # Process user input keys
        webcam_tools.process_key(key)

        if key == ord('q'):
            break
