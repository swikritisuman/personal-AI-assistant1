import speech_recognition as sr
import pyttsx3
import datetime

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)
        
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please repeat.")
        return get_command()
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def main():
    speak("Hello! I'm your personal assistant. How can I help you today?")

    while True:
        command = get_command()

        if command is not None:
            if "what is your name" in command:
                speak("I am a personal assistant created by  wikriti Suman")
            elif "time" in command:
                current_time = datetime.datetime.now().strftime("%H:%M")
                speak(f"The current time is {current_time}.")
            elif "exit" in command:
                speak("Goodbye!")
                break
            else:
                speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    main()
