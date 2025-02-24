import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture voice command and convert it to text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return None
        except sr.RequestError:
            print("Could not connect to the speech recognition service.")
            return None

def process_command(command):
    """Process user commands and perform actions"""
    if "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}")

    elif "search" in command:
        speak("What do you want to search for?")
        query = listen()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching Google for {query}")

    elif "wikipedia" in command:
        speak("What do you want to know about?")
        query = listen()
        if query:
            summary = wikipedia.summary(query, sentences=2)
            speak(summary)

    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("I'm not sure how to respond to that.")

if __name__ == "__main__":
    speak("Hello! How can I assist you today?")
    while True:
        command = listen()
        if command:
            process_command(command)
