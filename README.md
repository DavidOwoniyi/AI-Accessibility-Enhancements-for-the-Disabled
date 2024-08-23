# **AI Accessibility Enhancements for the Disabled**

This innovative project leverages AI models and machine learning techniques to recognize and convert sign language into text and speech, empowering individuals with disabilities to communicate seamlessly with anyone. 

This solution includes two key features: a gesture-to-speech program that transforms sign language into text and speech, and a voice command execution system that allows users to perform various tasks using simple voice commands. Together, these tools enable users to communicate and interact effortlessly with both people and the world around them.

## **Why This Project?**  
This project was developed to enhance the quality of life for individuals with disabilities by bridging the communication gap between them and non-sign language speakers. By recognizing hand sign language and integrating voice command execution, it facilitates easier and more effective interactions, making life simpler and more inclusive for both parties.

## **Installation**

To use these programs, follow these steps:

1. **Clone this repository to your local machine**:
   ```bash
   https://github.com/DavidOwoniyi/Accessibility-Enhancements-for-the-Disabled.git
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## **How to Use**

### **Hand Gesture Conversion into Text & Speech**

1. **Data Collection**:
   - Run the data collection script to capture images of the hand gestures. Move your hands back and forth, closer/farther from the camera and within the camera frame, to vary the distances. This is to ensure that each hand gesture can be detected from almost any distance from the camera.
   - Follow the prompts to capture different gestures for each character.

2. **Model Training**:
   - Use the provided script to train the machine learning model on the collected data.
   - The trained model will be saved for later use.

3. **Gesture Recognition & Text-to-Speech Conversion**:
   - Run the recognition script, which captures live video from your webcam.
   - The program detects gestures, converts them to text, and then to speech using Google Text-to-Speech (gTTS).

### **Voice Command Recognition & Execution**

1.	Running the Program:
	- Execute the program by running the **Speech Recognition & Task Execution.py script**.

2.	Voice Commands:
	   - Greeting: Say "Hello" to receive a greeting from the program.
	   - Ask for Name: Ask "What is your name?" to learn the program's name ("Jarvis").
	   - Ask About Well-being: Ask "How are you?" or similar phrases to receive a response about the program's state.
	   - Take a Screenshot: Say "Take a screenshot" or similar phrases to capture a screenshot and save it as screenshot.png.
	   - Open YouTube: Say "Open YouTube" to open the YouTube website in the default web browser.
	   - Read the News: Say "Read the news" or similar phrases to open a news website in the default web browser.
	   - Goodbye: Say "Goodbye" or similar phrases to end the program.

## **Dependencies**
- **Python 3.11+**
- **OpenCV**: For video capture and image processing.
- **MediaPipe**: For hand gesture detection.
- **scikit-learn**: For machine learning model creation and training.
- **gTTS**: For text-to-speech conversion.
- **playsound 1.2.2**: For audio playback.
- **speech_recognition**: For voice command recognition.

## **Limitations**

- **Hand Gesture Program**:
  - Limited to single-hand, stationary gestures.
  - Cannot handle gestures that involve movement or two hands(for now).

- **Voice Command Program**:
  - Requires clear speech and a noise-free environment for optimal performance.
  - Limited to pre-defined command sets(for now).

## **Reporting Bugs and Contributing**

- **Reporting Bugs**:
  - If you encounter any issues, please report them via the [Issues](https://github.com/DavidOwoniyi/Accessibility-Enhancements-for-the-Disabled/issues) page on GitHub.
  - Provide a detailed description of the issue and steps to reproduce it.

- **Contributing**:
  - Contributions are highly welcome! Fork the repository, make your changes, and submit a pull request.
  - Ensure your code adheres to the good coding standards and includes appropriate documentation.

## **Contact**

For any questions or further assistance, please contact me at  [owoniyidavid@yahoo.com](mailto:owoniyidavid@yahoo.com).
