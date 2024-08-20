# Import necessary dependencies
import os
import cv2

# Define the directory where the dataset will be stored
DATA_DIR = './data'

# Check if the data directory exists, if not, create it
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# List of class labels, representing the different gestures or characters to be captured
class_labels = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', 
    '6', '7', '8', '9', '-', '!'
]  # Example class labels

# Set the number of images to capture per class
dataset_size = 300

# Open a connection to the default camera (webcam)
cap = cv2.VideoCapture(0)

# Loop through each class label to capture images for each one
for class_index in range(len(class_labels)):
    class_name = class_labels[class_index]
    
    # Create a directory for each class if it doesn't already exist
    class_dir = os.path.join(DATA_DIR, class_name)
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    # Notify the user which class is being captured
    print('Collecting data for class {}'.format(class_name))

    # Wait for the user to press 'r' to start capturing images for the current class
    while True:
        ret, frame = cap.read()  # Capture a frame from the camera

        # Check if the frame was successfully captured
        if not ret:
            break  # Exit the loop if the frame was not captured

        # Display a message on the video feed to prompt the user to start capturing
        cv2.putText(
            frame, "Ready? Press 'r' to start capturing!", 
            (25, 60), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 255), 2, cv2.LINE_AA
        )
        cv2.imshow("Capturing datasets", frame)
        
        key = cv2.waitKey(25)

        # Start capturing images when 'r' is pressed
        if key == ord('r'):
            print('Starting image capture for class {}'.format(class_name))
            break  # Exit the loop and start capturing images
        elif key == ord('x'):
            # Release the camera and close all OpenCV windows if 'x' is pressed
            cap.release()
            cv2.destroyAllWindows()
            break  # Exit the entire program if 'x' is pressed

    # Image capture process: capture images until the desired dataset size is reached
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()  # Capture a frame from the camera

        # Check if the frame was successfully captured
        if not ret:
            print("Failed to grab frame during capture")
            break  # Exit the loop if the frame was not captured

        # Display the current frame
        cv2.imshow("Capturing datasets", frame)
        cv2.waitKey(25)

        # Save the captured frame to the class directory
        cv2.imwrite(os.path.join(class_dir, '{}.jpg'.format(counter)), frame)
        counter += 1

# Release the camera and close all OpenCV windows when done
cap.release()
cv2.destroyAllWindows()