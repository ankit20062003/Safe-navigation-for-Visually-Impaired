Real-Time Path Detection and Width Estimation for Enhanced Navigation of Visually Impaired Individuals

Implementation Details:
The implemented system provides real-time path assistance using computer vision techniques and deep learning for path detection and classification.
Below is a detailed explanation of the system components and their implementation.

System Architecture:
The system comprises several key components:

Video capture and processing
Path detection using edge detection
Scene classification using MobileNetV2
Audio feedback system
Real-time width measurement


Main Processing Loop:
The main processing loop continuously performs the following operations:

Captures video frames
Processes frames for edge detection
Detects path boundaries
Classifies the scene
Measures path width
Provides audio feedback when significant changes occur

System Requirements and Setup:
To run this system, the following requirements must be met:

Python 3.7 or higher
Required packages:
OpenCV (cv2)
TensorFlow 2.x
numpy
asyncio
gTTS
pydub
tensorflow-hub



Usage Instructions:

Ensure all required packages are installed
Connect a webcam to the system
Run the script
The system will display:

Live video feed with detected paths highlighted in green
Current scene classification
Path width measurements when available
Audio notifications for significant changes in path width or crosswalk detection



Output Interpretation:
The system provides multiple forms of output:

Visual Output:

Green lines indicating detected path boundaries
Text showing current scene classification
Numerical display of path width in feet


Audio Output:

Notifications when path width changes significantly (≥3 feet)
Alerts when crosswalks are detected


Performance Considerations:
Frame processing occurs in real-time
Width measurements are updated every 10 frames
Audio notifications are provided only for significant changes to prevent overflow
