# **AI Accessibility Enhancements for the Disabled**

This innovative project leverages AI models and machine learning techniques to recognize and convert sign language into text and speech, empowering individuals with disabilities to communicate seamlessly with anyone. 

This solution includes two key features: a gesture-to-speech program that transforms sign language into text and speech, and a voice command execution system that allows users to perform various tasks using simple voice commands. Together, these tools enable users to communicate and interact effortlessly with both people and the world around them.

<br />

## **Why This Project?**  
This project was developed to enhance the quality of life for individuals with disabilities by bridging the communication gap between them and non-sign language speakers. By recognizing hand sign language and integrating voice command execution, it facilitates easier and more effective interactions, making life simpler and more inclusive for both parties.

<br />

## **Installation**

To use these programs, follow these steps:

1. **Clone this repository to your local machine**:
   ```bash
   https://github.com/DavidOwoniyi/AI-Accessibility-Enhancements-for-the-Disabled.git
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

<br />

## **How to Use**

### **Hand Gesture Conversion into Text & Speech**

 1. **Dataset Collection Script (`Collect Images.py`)**:
	- Purpose: Captures images of various hand gestures or characters using a webcam and stores them in a structured dataset.
	- Usage:
	  - The script prompts you to start capturing images for each gesture by pressing 'r'.
	  - Captures 300 images per gesture, which are stored in a directory corresponding to the gesture label.
	  - Don't forget to capture a gesture for starting the gesture capturing process and another gesture for adding space inbetween words.
	  - Move your hands back and forth, closer/farther from the camera and within the camera frame to vary the distances. This is to ensure that gestures will be detected from varying distances.
	  - Press 'x' to exit the program at any time.

 2. **Data Preprocessing Script (`Create the dataset.py`)**:
	- Purpose: Processes the captured images, detects hand landmarks, normalizes the data, and prepares it for training.
	- Usage:
	  - The script reads images from the dataset directory.
	  - Uses MediaPipe to detect hand landmarks and normalizes the coordinates.
	  - Saves the processed data and corresponding labels to a pickle file (`data.pickle`).

3. **Model Training Script (`Train the model.py`)**:
	- Purpose: Trains a machine learning model (Random Forest Classifier) using the preprocessed data to recognize gestures.
	- Usage:
	  - The script loads the data from `data.pickle`.
	  - Pads the data to ensure uniformity in input length.
	  - Splits the data into training and testing sets.
	  - Trains a Random Forest Classifier model and evaluates its accuracy.
	  - Saves the trained model to a pickle file (`model.p`).

4. **Gesture Recognition Script (`Make predictions & detect hand gestures.py`)**:
	- Purpose: Recognizes hand gestures in real-time using a webcam, based on the trained model.
	- Usage:
	  - The script captures video frames from the webcam.
	  - Detects hand landmarks and uses the trained model to predict the gesture.
	  - Displays the recognized gesture on the video feed along with a bounding box around the hand.
	  - Press 'x' to exit the program.

5. **Gesture to Text and Speech Script (`Convert hand gestures to text and speech.py`)**:
	- Purpose: Converts recognized gestures into text and then into speech using Google Text-to-Speech (gTTS).
	- Usage:
	  - The script continuously captures frames and recognizes gestures.
	  - Starts/stops capturing gestures when the '!' gesture is held for 2 seconds.
	  - Converts the recognized gestures into text and then into speech.
	  - The captured text is played as speech using the `playsound` module.

<br />

### **Voice Command Recognition & Execution**

1.	**Running the Program**:
	- Execute the program by running the **`Speech Recognition & Task Execution.py`** script.

2.	**Voice Commands**:
	   - Greeting: Say "Hello" to receive a greeting from the program.
	   - Ask for Name: Ask "What is your name?" to learn the program's name ("Jarvis").
	   - Ask About Well-being: Ask "How are you?" or similar phrases to receive a response about the program's state.
	   - Take a Screenshot: Say "Take a screenshot" or similar phrases to capture a screenshot and save it as `screenshot.png`.
	   - Open YouTube: Say "Open YouTube" to open the YouTube website in the default web browser.
	   - Read the News: Say "Read the news" or similar phrases to open a news website in the default web browser.
	   - Goodbye: Say "Goodbye" or similar phrases to end the program.

<br />

## **Dependencies**
- **Python 3.11+**
- **OpenCV**: For video capture and image processing.
- **MediaPipe**: For hand gesture detection.
- **scikit-learn**: For machine learning model creation and training.
- **gTTS**: For text-to-speech conversion.
- **playsound 1.2.2**: For audio playback.
- **speech_recognition**: For voice command recognition.

<br />

## **License**
This project is licensed under the [MIT License](https://github.com/DavidOwoniyi/AI-Accessibility-Enhancements-for-the-Disabled?tab=MIT-1-ov-file)

<br />

## **Reporting Bugs and Contributing**

- **Reporting Bugs**:
  - If you encounter any issues, please report them via the [Issues](https://github.com/DavidOwoniyi/AI-Accessibility-Enhancements-for-the-Disabled/issues) page on GitHub.
  - Provide a detailed description of the issue and steps to reproduce it.

- **Contributing**:
  - Contributions are highly welcome! Fork this repository, make your changes, and submit a pull request.
  - Ensure your code adheres to good coding standards and includes appropriate documentation.

<br />

## **Contact**

For any questions or further assistance, please contact me at  or on [LinkedIn](https://www.linkedin.com/in/david-owoniyi/).
