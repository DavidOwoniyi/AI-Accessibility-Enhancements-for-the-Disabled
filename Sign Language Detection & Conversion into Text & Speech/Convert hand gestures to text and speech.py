# Importing the necessary dependencies
import speech_recognition as sr  # For voice command recognition
import time  # To handle timing for gesture detection
from gtts import gTTS  # Google Text-to-Speech for converting text to speech
from playsound import playsound  # To play the generated speech
import os  # For file operations like saving and deleting audio files
import pickle  # To load the trained model
import mediapipe as mp  # For hand gesture detection
import cv2  # OpenCV for capturing video and handling frames
import numpy as np  # To handle numerical operations like array creation

# Function to convert text to speech
def text_to_speech(text):
    if not text.strip():  # Check if the text is empty or only whitespace
        print("No text to convert to speech.")
        return
    # Convert the text to speech using gTTS with Nigerian accent (tld='com.ng')
    speech = gTTS(text, tld='us', lang='en', slow=False)
    speech_file = 'speech.mp3'  # Temporary filename for the speech audio
    speech.save(speech_file)  # Save the speech to the file
    playsound(speech_file)  # Play the speech audio
    os.remove(speech_file)  # Remove the audio file after playing

# Function to get the predicted gesture from the frame
def get_predicted_gesture(frame, hands, model, mp_drawing, mp_hands, mp_drawing_styles):
    data_aux = []  # To store the normalized coordinates of landmarks
    x_, y_ = [], []  # To store x and y coordinates separately

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert frame to RGB for processing
    results = hands.process(frame_rgb)  # Process the frame to detect hand landmarks

    if results.multi_hand_landmarks:  # If hand landmarks are detected
        for hand_landmarks in results.multi_hand_landmarks:
            # Collect x and y coordinates of each landmark
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                x_.append(x)
                y_.append(y)

            # Normalize the coordinates and append to data_aux
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x - min(x_))
                data_aux.append(y - min(y_))

        # Check if the number of features matches the model's expectation
        if len(data_aux) == model.n_features_in_:
            prediction = model.predict([np.asarray(data_aux)])  # Predict the gesture
            predicted_gesture = prediction[0]  # Get the predicted gesture

            for hand_landmarks in results.multi_hand_landmarks:
                # Draw the hand landmarks on the frame
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style()
                )
            return predicted_gesture  # Return the predicted gesture
        else:
            print("Skipped frame due to incorrect number of features.")
            return None

    return None  # Return None if no hand landmarks are detected

# Function to capture gestures, convert them to text, and then to speech
def gesture_to_text_and_speech():
    captured_text = ""  # String to store the captured text
    capturing = False  # Boolean to track if capturing is ongoing
    capture_start_time = None  # To store the start time of capturing

    model_dict = pickle.load(open('./model.p', 'rb'))  # Load the trained model
    model = model_dict['model']  # Extract the model from the dictionary

    cap = cv2.VideoCapture(0)  # Start video capture from the default camera

    # Initialize MediaPipe components for hand detection and drawing
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    hands = mp_hands.Hands(static_image_mode=False, min_detection_confidence=0.3)

    try:
        while True:
            ret, frame = cap.read()  # Capture a frame from the video feed
            if not ret:  # Break if frame capture fails
                break

            predicted_gesture = get_predicted_gesture(frame, hands, model, mp_drawing, mp_hands, mp_drawing_styles)

            if predicted_gesture:
                if predicted_gesture == '!':  # Start or stop capturing based on the '!' gesture
                    if not capturing:
                        if capture_start_time is None:
                            capture_start_time = time.time()
                        elif time.time() - capture_start_time >= 2:
                            capturing = True
                            print("Capturing started...")
                            capture_start_time = None
                    else:
                        if capture_start_time is None:
                            capture_start_time = time.time()
                        elif time.time() - capture_start_time >= 2:
                            capturing = False
                            print("Capturing stopped.")
                            print("Captured text:", captured_text)
                            text_to_speech(captured_text)  # Convert captured text to speech
                            captured_text = ""  # Reset captured text
                            capture_start_time = None

                elif capturing:
                    if predicted_gesture == '-':  # Add a space to the captured text with '-' gesture
                        if capture_start_time is None:
                            capture_start_time = time.time()
                        elif time.time() - capture_start_time >= 2:
                            captured_text += " "
                            print("Added space.")
                            capture_start_time = None
                    else:
                        if capture_start_time is None:
                            capture_start_time = time.time()
                        elif time.time() - capture_start_time >= 2:
                            captured_text += predicted_gesture  # Append the captured letter
                            print("Captured letter:", predicted_gesture)
                            capture_start_time = None

            # Display the captured text on the frame
            cv2.putText(frame, captured_text, (25, 60), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.imshow("Gesture-Based Text and Speech", frame)  # Show the frame with the captured text

            key = cv2.waitKey(1)  # Check for key press
            if key == ord('x'):  # Break the loop if 'x' is pressed
                break

    finally:
        cap.release()  # Release the video capture object
        cv2.destroyAllWindows()  # Close all OpenCV windows

# Run the gesture to text and speech conversion
gesture_to_text_and_speech()
