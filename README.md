# WebcamTools

WebcamTools provides basic functionalities for working with webcams. It includes tools to list available cameras, perform basic operations on webcam video streams, capture images, and record videos.

## Getting Started

### Prerequisites

- Python 3.x
- OpenCV library (cv2)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/Netzach204/WebcamTools.git
cd WebcamTools
```

2. Install the required packages:
```bash
pip install opencv-python
```

## Usage

### List Available Cameras

The `list_available_cameras.py` script allows you to list all available cameras on your system. Run the script using the following command:

```bash
python src/list_available_cameras.py
```

### Webcam Video Basics

The `webcam_tools.py` module provides basic webcam video operations, including capturing images and recording videos. You can import this module and use its functions in your scripts.

### Opening Webcams with Threading

The `webcam_video_stream.py` module introduces a threaded approach to opening webcam streams. This enables you to efficiently handle multiple cameras concurrently. This module is used internally by the `run_multi_camera.py` example script.

## Configuration

The `webcam_settings.json` file in the `config/` directory holds camera settings. You can customize the camera sources, resolutions, and FPS values according to your requirements.

## Example

To see how to run multiple cameras, check out the `run_multi_camera.py` script. It demonstrates how to load camera settings, initialize streams, and display feeds from multiple cameras simultaneously.

```bash
python run_multi_camera.py
```
