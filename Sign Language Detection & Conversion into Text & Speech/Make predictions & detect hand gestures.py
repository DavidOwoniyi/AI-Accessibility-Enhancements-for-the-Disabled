# Import necessary dependencies
import pickle  # For loading the pre-trained model
import cv2  # OpenCV for video capture and image processing
import mediapipe as mp  # MediaPipe for hand detection and landmarks
import numpy as np  # For numerical operations

# Load the pre-trained model from a file
model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']  # Extract the model from the loaded dictionary

# Initialize the webcam for video capture
cap = cv2.VideoCapture(0)

# Initialize MediaPipe Hands for hand detection and landmarks
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# Define a dictionary mapping numeric labels to characters
labels_dict = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G',
    7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M',
    13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S',
    19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z',
    26: '1', 27: '2', 28: '3', 29: '4', 30: '5', 31: '6',
    32: '7', 33: '8', 34: '9', 35: '0', 36: '-', 37: '!'
}

# Start a loop to continuously capture frames from the webcam
while True:
    ret, frame = cap.read()  # Capture a frame
    if not ret:  # If the frame is not captured correctly, exit the loop
        break

    # Initialize lists to store auxiliary data and coordinates
    data_aux = []
    x_, y_ = [], []

    # Convert the frame to RGB format for MediaPipe processing
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)  # Process the frame for hand landmarks

    if results.multi_hand_landmarks:  # If hand landmarks are detected
        for hand_landmarks in results.multi_hand_landmarks:
            # Extract and normalize landmark coordinates
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                x_.append(x)
                y_.append(y)

            # Prepare the feature vector by subtracting minimum coordinates
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x - min(x_))
                data_aux.append(y - min(y_))

            # Make sure the length of features matches what the model expects
            if len(data_aux) == 42:  # Adjust this according to your model's expected input length
                prediction = model.predict([np.asarray(data_aux)])
                predicted_character = prediction[0]  # Directly use the predicted string

                # Draw bounding box and predicted character on the frame
                x1, y1 = int(min(x_) * frame.shape[1]), int(min(y_) * frame.shape[0])
                x2, y2 = int(max(x_) * frame.shape[1]), int(max(y_) * frame.shape[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (25, 32, 48), 4)
                cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_COMPLEX, 1.3, (25, 32, 48), 3, cv2.LINE_AA)

            # Draw hand landmarks on the frame
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style()
            )

    # Display the frame with the drawn landmarks and predictions
    cv2.imshow('Sign Language Detector', frame)
    key = cv2.waitKey(1)  # Wait for 1 ms for a key press

    if key == ord('x'):  # Exit the loop if 'x' is pressed
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
