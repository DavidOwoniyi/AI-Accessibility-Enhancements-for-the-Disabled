# Import necessary dependencies
import os  # For handling directory and file operations
import cv2  # OpenCV for image processing
import mediapipe as mp  # For hand landmark detection
import pickle  # For saving data and labels to a file

# Initialize MediaPipe hands module
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Set up the Hands object for static image mode with a minimum detection confidence
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# Define the directory where the image data is stored
DATA_DIR = './data'

# Initialize lists to store data and labels
data = []
labels = []

# Loop through each sub-directory in the data directory
for sub_dir in os.listdir(DATA_DIR):
    sub_dir_path = os.path.join(DATA_DIR, sub_dir)
    if not os.path.isdir(sub_dir_path):
        continue  # Skip if it's not a directory
    
    # Loop through each image in the sub-directory
    for img_path in os.listdir(sub_dir_path):
        img_path_full = os.path.join(sub_dir_path, img_path)
        # print(f"Loading image from: {img_path_full}")

        # Read the image using OpenCV
        img = cv2.imread(img_path_full)
        if img is None:
            # print(f"Failed to load image at: {img_path_full}")
            continue  # Skip if the image cannot be loaded

        # Convert the image to RGB format for processing with MediaPipe
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)  # Process the image to detect hand landmarks

        # Check if any hand landmarks are detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                x_ = []
                y_ = []
                data_aux = []

                # Collect x and y coordinates of the hand landmarks
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    x_.append(x)
                    y_.append(y)

                # Normalize the coordinates by subtracting the minimum values
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

                # Append the normalized data to the data list
                data.append(data_aux)
                # Append the corresponding label (sub-directory name) to the labels list
                labels.append(sub_dir)

# Save the data and labels to a pickle file
f = open('data.pickle', 'wb')
pickle.dump({'data': data, 'labels': labels}, f)
f.close()
