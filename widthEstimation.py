from numbers import Number
import cv2  # OpenCV for image processing
import numpy as np  # Numerical computing
import asyncio  # For asynchronous operations
from gtts import gTTS  # Google Text-to-Speech
import io
from pydub import AudioSegment  # Audio processing
from pydub.playback import play
import tensorflow as tf  # Deep learning framework
import tensorflow_hub as hub  # TensorFlow model hub

# Initialize video capture from default camera ,index 0
cap = cv2.VideoCapture(0)
cnt = 0  # Counter for width measurement updates
prevWidth = 0  # Store previous width for change detection

# Define region of interest (ROI) for path detection
# Format: (x_start, y_start, x_end, y_end)
roi = (300, 200, 900, 680)

# Load pre-trained MobileNetV2 model for scene classification
model = MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=True,
    weights="imagenet"
)

# Define classification labels
labels = {
    0: "Background",
    1: "crosswalk",
    2: "road",
    3: "pathway"
}

def preprocess_frame_edges(frame):
    """
    Preprocess frame for edge detection.
    
    Args:
        frame: Input frame from video capture
        
    Returns:
        edges: Processed frame with detected edges
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    blur = cv2.GaussianBlur(gray, (5, 5), 0)  # Apply Gaussian blur
    edges = cv2.Canny(blur, 50, 150)  # Apply Canny edge detection
    return edges

def preprocess_frame_classification(frame):
    """
    Preprocess frame for neural network classification.
    
    Args:
        frame: Input frame from video capture
        
    Returns:
        preprocessed_frame: Normalized and resized frame
    """
    resized_frame = cv2.resize(frame, (224, 224))  
    normalized_frame = np.array(resized_frame) / 255.0  # Normalize pixel values
    return np.expand_dims(normalized_frame, axis=0)  # Add batch dimension

def detect_path(edges, roi):
    """
    Detect path lines within region of interest.
    
    Args:
        edges: Edge-detected frame
        roi: Region of interest coordinates
        
    Returns:
        lines: Detected line segments
    """
    # Create mask for ROI
    mask = np.zeros_like(edges)  
    mask[roi[1]:roi[3], roi[0]:roi[2]] = edges[roi[1]:roi[3], roi[0]:roi[2]]
    lines = cv2.HoughLinesP(
        mask,
        1,
        np.pi/180,
        threshold=50,
        minLineLength=100,
        maxLineGap=50
    )
    return lines

def classify_frame(frame):
    """
    Classify the current frame using the pre-trained model.
    
    Args:
        frame: Input frame
        
    Returns:
        label: Predicted scene class
    """
    preprocessed_frame = preprocess_frame_classification(frame)
    predictions = model(preprocessed_frame).numpy()
    predicted_class = np.argmax(predictions[0])
    return labels.get(predicted_class, "Background")

def calculate_width(lines):
    """
    Calculate path width from detected lines.
    
    Args:
        lines: Detected line segments
        
    Returns:
        width_in_pixels: Calculated width between leftmost and rightmost lines
    """
    if lines is None:
        return None
    
    left_line = min(lines, key=lambda line: line[0][0])
    right_line = max(lines, key=lambda line: line[0][0])
    width_in_pixels = right_line[0][0] - left_line[0][0]
    return width_in_pixels

# Audio feedback functions
async def generate_tts(message):
    """Generate Text-to-Speech audio"""
    tts = gTTS(text=message, lang='en')
    audio_file = io.BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)
    return audio_file

async def play_audio(audio_file):
    """Play generated audio feedback"""
    audio = AudioSegment.from_file(audio_file, format="mp3")
    play(audio)

async def notify_user(message):
    """Combine TTS generation and playback"""
    audio_file = await generate_tts(message)
    await play_audio(audio_file)
