# Importing necessary dependencies
import speech_recognition as sr  # For speech recognition
import time  # For handling time-related functions
from gtts import gTTS  # For converting text to speech
from playsound import playsound  # For playing audio files
import os  # For file handling operations
import pyautogui  # For automating GUI interactions like taking screenshots
import webbrowser  # For opening web pages



# Initialize the recognizer for speech recognition
recognizer = sr.Recognizer()

def capture_voice_input():
    """
    Captures voice input from the microphone and returns the audio data.
    Handles ambient noise by adjusting the recognizer sensitivity.
    """
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise

        try:
            # Listen for the user's input, with a timeout for silence and maximum duration
            audio = recognizer.listen(source, timeout=20, phrase_time_limit=12)
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for you to speak")
            return None  # Return None if the timeout is reached
    return audio  # Return the captured audio



def text_to_speech(text):
    """
    Converts text to speech using Google Text-to-Speech (gTTS) and plays it.
    The speech is saved to a temporary file and deleted after playback.
    """
    speech = gTTS(text, tld='com.ng', lang='en', slow=False)  # Create speech object
    speech_file = 'speech.mp3'  # Define the filename for the audio file
    speech.save(speech_file)  # Save the speech to the file
    playsound('speech.mp3')  # Play the audio file
    os.remove(speech_file)  # Remove the file after playing



def convert_voice_to_text(audio):
    """
    Converts the captured audio to text using Google's speech recognition.
    Handles errors like unrecognized speech and request errors.
    """
    if audio is None:
        return ""  # Return an empty string if no audio is captured
    try:
        text = recognizer.recognize_google(audio)  # Convert audio to text
        print("You said: " + text)
    except sr.UnknownValueError:
        text = ""
        print("Sorry I didn't understand that.")
        text_to_speech(f"Sorry I didn't understand that")
    except sr.RequestError as e:
        text = ""
        print("Error: {0}".format(e))  # Print the error if the API request fails
    return text



def process_voice_command(text):
    """
    Processes the recognized text and performs specific actions based on voice commands.
    """
    if "hello" in text.lower():
        print("Hello! How can I help you?")
        text_to_speech(f"Hello! How can I help you")

    elif "what is your name" in text.lower():
        print("My name is Jarvis")
        text_to_speech(f"My name is Jarvis")

    elif ("how are you doing today" in text.lower() or
          "how are you" in text.lower() or
          "how are you doing" in text.lower()):
        print("I'm doing alright, thank you very much")
        text_to_speech(f"I'm doing alright, thank you very much")

    elif ("take a screenshot" in text.lower() or 
          "take screenshot" in text.lower() or
          "screenshot" in text.lower()):
        pyautogui.screenshot("screenshot.png")  # Take a screenshot and save it
        print("I took a screenshot for you")
        text_to_speech(f"I took a screenshot for you")

    elif "open youtube" in text.lower():
        print("Opening YouTube")
        webbrowser.open("https://www.youtube.com/")  # Open YouTube in the web browser
        text_to_speech(f"Opening YouTube")

    elif ("read the news" in text.lower() or 
          "the news" in text.lower() or
          "news" in text.lower() or
          "open news" in text.lower()):
        print("Opening the news")
        webbrowser.open("https://punchng.com/")  # Open a news website
        text_to_speech(f"Opening the news")

    elif ("alright, goodbye" in text.lower() or 
          "alright" in text.lower() or 
          "goodbye" in text.lower() or 
          "all right" in text.lower() or 
          "stop" in text.lower()):
        print("Goodbye! Have a nice day")
        text_to_speech(f"Goodbye! Have a nice day")
        return True  # End the program
    else: 
        print("I didn't understand that command. Please try again.") 
        text_to_speech(f"I didn't understand that command. Please try again.")
    return False  # Continue running the program



def main():
    """
    Main loop for capturing voice input, processing commands, and handling retries.
    The loop exits after a successful command or after a set number of failed attempts.
    """
    end_program = False  # Flag to indicate if the program should end
    attempts = 0  # Track the number of failed attempts
    max_attempts = 3  # Limit to the number of attempts

    while not end_program and attempts < max_attempts:
        audio = capture_voice_input()  # Capture voice input
        if audio is None:
            attempts += 1
            print(f"Retrying... ({attempts}/{max_attempts})")
            time.sleep(1)  # Delay to prevent rapid looping
        else:
            text = convert_voice_to_text(audio)  # Convert voice input to text
            if text == "":
                attempts += 1
                print(f"Retrying... ({attempts}/{max_attempts})")
            else:
                end_program = process_voice_command(text)  # Process the voice command
                attempts = 0  # Reset attempts if a valid command is processed
    if attempts >= max_attempts:
        print("Too many failed attempts due to timeout. Exiting program.")
        text_to_speech(f"Too many failed attempts due to timeout.")

if __name__ == "__main__":
    main()  # Run the main function
