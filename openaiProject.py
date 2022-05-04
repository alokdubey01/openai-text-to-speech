import datetime
import json
import openai
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 150)


def wish():
    time = datetime.datetime.now().hour
    if time == 12:
        print("Good Noon Sir")
        speak("Good Noon Sir")
    elif time >= 0 or time < 12:
        print("Good Morning Sir")
        speak("Good Morning Sir")
    else:
        print("Good Evening Sir")
        speak("Good Evening Sir")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 3000
        audio = r.listen(source)

    try:
        print("Recognizing...")
        response = r.recognize_google(audio, language='en-in')
        print(f"User Said:{response}\n")

    except Exception as e:
        print("Say that again please...")
        speak("say that again please...")
        return "None"
    return response


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def gpt3(stext):
    openai.api_key = "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"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=stext,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text


if __name__ == "__main__":
    wish()
    while True:
        question = takecommand()
        response = gpt3(question)
        print(response)
        speak(response)
