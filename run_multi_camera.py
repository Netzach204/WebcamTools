import cv2
import json
from src.webcam_video_stream import WebcamVideoStream

class MultiCameraViewer:
    def __init__(self, settings_path):
        self.settings_path = settings_path
        self.camera_streams = {}

    def load_settings(self):
        # Load camera settings from JSON file
        with open(self.settings_path, 'r', encoding='UTF-8-sig') as jsonfile:
            self.webcam_settings = json.load(jsonfile)

    def initialize_streams(self):
        # Initialize camera streams based on loaded settings
        for camera_id, settings in self.webcam_settings.items():
            src = settings['src']
            resolution = (settings['resolution_width'], settings['resolution_height'])
            fps = settings['fps']
            name = settings['name']
            
            # Create and start WebcamVideoStream for each camera
            self.camera_streams[camera_id] = WebcamVideoStream(src=src, fps=fps, resolution=resolution, name=name)
            self.camera_streams[camera_id].start()

    def display_feeds(self):
        # Create windows for displaying camera feeds
        for camera_id in self.camera_streams:
            cv2.namedWindow(f"Camera {camera_id}", cv2.WINDOW_NORMAL)
        
        try:
            while True:
                for camera_id, camera_stream in self.camera_streams.items():
                    grabbed, frame = camera_stream.read()
                    if not grabbed:
                        print(f"Camera {camera_id} not available.")
                        continue
                    
                    # Display the current frame of each camera
                    cv2.imshow(f"Camera {camera_id}", frame)
                
                # Break the loop when 'q' key is pressed
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        finally:
            # Clean up resources when exiting
            self.cleanup()

    def cleanup(self):
        # Stop camera streams and release resources
        for camera_stream in self.camera_streams.values():
            camera_stream.stop()
            camera_stream.stream.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    # Specify the path to the settings JSON file
    settings_path = "./config/webcam_settings.json"
    viewer = MultiCameraViewer(settings_path)
    
    # Load camera settings, initialize streams, and display feeds
    viewer.load_settings()
    viewer.initialize_streams()
    viewer.display_feeds()
