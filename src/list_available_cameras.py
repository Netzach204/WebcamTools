import cv2

def list_available_cameras():
    # List available camera indexes and return the total number of available cameras.
    available_cameras = []
    index = 0
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        cap.release()
        available_cameras.append(index)
        index += 1
    return available_cameras, index

if __name__ == '__main__':
    available_cameras, num_cameras = list_available_cameras()
    
    if num_cameras == 0:
        print("No cameras found.")
    else:
        print(f"Number of available cameras: {num_cameras}")
        print(f"Available camera indexes: {available_cameras}")
