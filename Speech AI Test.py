import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes

# Initialize the speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 0 for male, 1 for female

def speak(text):
    """Speaks the given text"""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Captures microphone input and converts to text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()

# Main Loop
if __name__ == "__main__":
    speak("Hello, I am your assistant. How can I help?")
    while True:
        query = take_command()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'stop' in query or 'exit' in query:
            speak("Goodbye!")
            break
