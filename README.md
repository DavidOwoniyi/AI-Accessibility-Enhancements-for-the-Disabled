# **AI Accessibility Enhancements for the Disabled**

This innovative project leverages AI models and machine learning techniques to recognize and convert sign language into text and speech, empowering individuals with disabilities to communicate seamlessly with anyone. This solution includes two key features: a gesture-to-speech program that transforms sign language into text and speech, and a voice command execution system that allows users to perform various tasks through simple voice commands. Together, these tools enable users to communicate and interact effortlessly with both people and the world around them.

1. **Hand Gesture Conversion into Text & Speech**: Converts sign language gestures into text and then into speech, using a trained machine learning model. It's designed for stationary single-hand gestures only(for now).
2. **Voice Command Recognition & Execution**: Recognizes voice commands and executes various tasks, making interaction with technology more accessible.

## **Why This Project?**

This project stands out from other existing solutions due to its simplicity and targeted functionality. It focuses on single-hand, stationary gestures and is designed for environments where standard input methods are challenging or impossible. The combination of hand gestures and voice commands offers a versatile tool for individuals with different types of disabilities.

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
   - Run the data collection script to capture images of the hand gestures. Ensure that you move your hands back and forth and within the frame of the camera during the capture. This is to ensure that each hand gesture can be detect from almost anywhere.
   - Follow the prompts to capture different gestures for each character.

2. **Model Training**:
   - Use the provided script to train the machine learning model on the collected data.
   - The trained model will be saved for later use.

3. **Gesture Recognition & Text-to-Speech Conversion**:
   - Run the recognition script, which captures live video from your webcam.
   - The program detects gestures, converts them to text, and then to speech using Google Text-to-Speech (gTTS).

### **Voice Command Recognition & Execution**

1. **Run the voice command script**.
2. **Speak the command** clearly when prompted.
3. The program will recognize the command and execute the corresponding task.

### **Limitations**

- **Gesture Conversion**:
  - Only supports stationary, single-hand gestures.
  - Cannot recognize two-hand or moving gestures.
  - Limited to the gestures included in the training data.
  
- **Voice Command Recognition**:
  - Requires a clear and noise-free environment for optimal performance.

### **Dependencies**

- **Python 3.8+**
- **OpenCV**: For video capture and image processing.
- **MediaPipe**: For hand gesture detection.
- **scikit-learn**: For machine learning model creation and training.
- **gTTS**: For text-to-speech conversion.
- **playsound**: For audio playback.
- **speech_recognition**: For voice command recognition.

## **Limitations**

- **Hand Gesture Program**:
  - Limited to single-hand, stationary gestures.
  - Cannot handle gestures that involve movement or multiple hands.

- **Voice Command Program**:
  - Requires clear speech and a noise-free environment for optimal performance.
  - Limited to pre-defined command sets.

## **Reporting Bugs and Contributing**

- **Reporting Bugs**:
  - If you encounter any issues, please report them via the [Issues](https://github.com/your-username/Accessibility-Enhancement-Programs/issues) page on GitHub.
  - Provide a detailed description of the issue and steps to reproduce it.

- **Contributing**:
  - Contributions are welcome! Fork the repository, make your changes, and submit a pull request.
  - Ensure your code adheres to the project's coding standards and includes appropriate documentation.

## **Contact**

For any questions or further assistance, please contact the project maintainer at [your-email@example.com](mailto:your-email@example.com).

---

This README file should serve as a comprehensive guide for anyone looking to understand, install, and use your programs. Feel free to adjust the content to fit your specific needs or include additional sections if necessary.
