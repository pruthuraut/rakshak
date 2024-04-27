import cv2
import tensorflowjs as tfjs
from tensorflow.keras.models import load_model
import json
import numpy as np

# Set the link to your model provided by Teachable Machine export panel
URL = "https://teachablemachine.withgoogle.com/models/jLeJTw1rQ"

# Load the model and metadata
model = load_model(URL + "model.h5")
metadata_path = URL + "metadata.json"
with open(metadata_path, 'r') as f:
    metadata = json.load(f)
max_predictions = metadata['numberOfClasses']

# Create a VideoCapture object to capture video from the webcam
cap = cv2.VideoCapture(0)

# Set the window size
size = 200
cap.set(3, size)
cap.set(4, size)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Preprocess the frame if needed

    # Perform predictions
    # Replace the following lines with your own image preprocessing and prediction code
    # This is just a placeholder
    input_data = np.expand_dims(frame, axis=0)
    predictions = model.predict(input_data)

    # Draw predictions on the frame
    for i in range(max_predictions):
        class_prediction = f"{metadata['labels'][i]}: {predictions[0][i]:.2f}"
        cv2.putText(frame, class_prediction, (10, 30 + i * 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1,
                    cv2.LINE_AA)

    # Display the frame
    cv2.imshow("Webcam", frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()