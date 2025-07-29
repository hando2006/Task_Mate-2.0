import speech_recognition as sr

def listen_for_task():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("🎙️ Say a task after the beep...")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening now...")
        audio = recognizer.listen(source)

    try:
        task = recognizer.recognize_google(audio)
        print(f"You said: {task}")
        return task
    except sr.UnknownValueError:
        print("Sorry, I couldn’t understand.")
        return None
    except sr.RequestError as e:
        print(f"Error with the speech service: {e}")
        return None
