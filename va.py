import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text to speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

def listen():
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    # Recognize speech using Google Speech Recognition
    try:
        print("Recognizing...")
        return r.recognize_google(audio)
    except Exception as e:
        print("Could not understand audio")
        return ""

def speak(text):
    # Use the text to speech engine to say the text
    engine.say(text)
    engine.runAndWait()

while True:
    # Listen for speech and convert it to text
    text = listen()

    # Respond based on the text
    if "hello" in text.lower():
        speak("Hello! How can I assist you?")
    elif "goodbye" in text.lower():
        speak("Goodbye!")
        break
    elif "run detection model" in text.lower():
         speak("The model is about to start running")
         import run
