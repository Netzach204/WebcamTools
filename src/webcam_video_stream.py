from threading import Thread, Lock
import numpy as np
import cv2, time


class WebcamVideoStream:
    def __init__(self, src=0, fps=30, resolution=(640, 480), name="WebcamVideoStream"):
        print("--> Init Webcam Connection")
        self.stream = cv2.VideoCapture(src)

        # Set desired properties for the video stream
        self.stream.set(cv2.CAP_PROP_FPS, fps)
        self.stream.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
        self.stream.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])

        self.crop_img = None
        self.frame_lock = Lock()  # Lock for accessing frame data
        (self.grabbed, self.frame) = self.stream.read()

        self.name = name
        self.stopped = False

    def start(self):
        # Start a thread to continually update frames from the video stream
        t = Thread(target=self.update, name=self.name, args=())
        t.daemon = True
        t.start()
        return self

    def update(self):
        while True:
            if self.stopped:
                return

            # Read the next frame from the video stream
            grabbed, frame = self.stream.read()
            if grabbed:
                with self.frame_lock:
                    self.frame = frame.copy()
            # Add a small delay to avoid excessive frame reading
            time.sleep(0.01)

    def read(self):
        with self.frame_lock:
            self.crop_img = self.frame.copy()
            # Convert the frame to a NumPy array
            frame_np = np.array(self.crop_img)
        return self.grabbed, frame_np

    def stop(self):
        self.stopped = True

if __name__ == '__main__':
    try:
        # Read configuration from file or command line
        webcam_config = {
            "src": 0,
            "resolution": (640, 480),
            "fps": 30,
            "name": "WebcamVideoStream"
        }

        # Initialize the webcam video stream with configured parameters
        vs = WebcamVideoStream(**webcam_config)
        vs.start()

        while True:
            # Read a frame from the video stream
            grabbed, frame = vs.read()
            if grabbed:
                # Display the frame
                cv2.imshow("Webcam Stream", frame)
                # Exit the loop and close the window if 'q' is pressed
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
    finally:
        # Stop the video stream and close all OpenCV windows
        vs.stop()
        cv2.destroyAllWindows()
