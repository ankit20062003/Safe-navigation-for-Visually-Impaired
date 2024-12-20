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

1) Captures video frames<br>
2) Processes frames for edge detection<br>
3) Detects path boundaries<br>
4) Classifies the scene<br>
5) Measures path width<br>
6) Provides audio feedback when significant changes occur<br>

<h3>System Requirements and Setup :</h3>
To run this system, the following requirements must be met:<br>

* Python 3.7 or higher<br>
* Required packages:<br>
* OpenCV (cv2)<br>
* TensorFlow 2.x<br>
* numpy<br>
* asyncio<br>
* gTTS<br>
* pydub<br>
* tensorflow-hub<br>



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

*Visual Output:<br>

Green lines indicating detected path boundaries<br>
Text showing current scene classification<br>
Numerical display of path width in feet<br>


*Audio Output:<br>

Notifications when path width changes significantly (≥3 feet)<br>
Alerts when crosswalks are detected<br>


*Performance Considerations:<br>

Frame processing occurs in real-time<br>
Width measurements are updated every 10 frames<br>
Audio notifications are provided only for significant changes to prevent overflow




<h2>Contribution of the resources (code and dataset) in the research</h2>
The MSCOCO dataset serves as the foundational training data for your system because of its comprehensive collection of urban scene images that are crucial for mobility assistance. Its value comes from containing diverse annotated examples of crosswalks, pathways, and common urban objects, which helps your model recognize these elements in real-world scenarios.
The YOLO model, initially trained on MSCOCO and then fine-tuned with your custom Kaggle dataset, forms the core computer vision component of your system. This model's specific role is enhancing the accuracy of path detection and scene understanding. The fine-tuning process adapts the model's general object detection capabilities to your specific use case of mobility assistance and path width measurement.<br>

In my implementation, these resources contribute by: <br>

1) Enabling real-time path detection and width measurement <br>
2) Providing reliable scene classification for identifying crosswalks and pathways <br>
3) Supporting the audio feedback system with accurate environmental information <br>

The combination of MSCOCO-trained YOLO model and your custom fine-tuning creates a specialized system that bridges the gap between general computer vision capabilities and practical mobility assistance applications. This makes a novel contribution by demonstrating how transfer learning can be effectively applied to create real-world accessibility solutions.
