<h2>Real-Time Path Detection and Width Estimation for Enhanced Navigation of Visually Impaired Individuals</h2>

<h3> Implementation Details :</h3>
The implemented system provides real-time path assistance using computer vision techniques and deep learning for path detection and classification.<br>
Below is a detailed explanation of the system components and their implementation.

<h3>System Architecture :</h3>
The system comprises several key components:<br>

Video capture and processing<br>
Path detection using edge detection<br>
Scene classification using MobileNetV2<br>
Audio feedback system<br>
Real-time width measurement<br>


<h3>Main Processing Loop :</h3>
The main processing loop continuously performs the following operations:<br>

Captures video frames<br>
Processes frames for edge detection<br>
Detects path boundaries<br>
Classifies the scene<br>
Measures path width<br>
Provides audio feedback when significant changes occur<br>

<h3>System Requirements and Setup :</h3>
To run this system, the following requirements must be met:<br>

Python 3.7 or higher<br>
Required packages:<br>
OpenCV (cv2)<br>
TensorFlow 2.x<br>
numpy<br>
asyncio<br>
gTTS<br>
pydub<br>
tensorflow-hub<br>



<h3>Usage Instructions :</h3>

Ensure all required packages are installed
Connect a webcam to the system
Run the script
The system will display:

Live video feed with detected paths highlighted in green
Current scene classification
Path width measurements when available
Audio notifications for significant changes in path width or crosswalk detection



<h3>Output Interpretation :</h3>
The system provides multiple forms of output:<br>

Visual Output:<br>

Green lines indicating detected path boundaries<br>
Text showing current scene classification<br>
Numerical display of path width in feet<br>


Audio Output:<br>

Notifications when path width changes significantly (≥3 feet)<br>
Alerts when crosswalks are detected<br>


Performance Considerations:<br>

Frame processing occurs in real-time<br>
Width measurements are updated every 10 frames<br>
Audio notifications are provided only for significant changes to prevent overflow
