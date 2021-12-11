import pyttsx3
import datetime as dt
import speech_recognition
import wikipedia
import webbrowser
import os
import smtplib
import random
import pyautogui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greeting():
    hour = int(dt.datetime.now().hour)
    if 0 <= hour < 12:
        print("Good Morning!")
        speak("Good Morning!")
    elif 12 <= hour < 18:
        print("Good Afternoon")
        speak("Good Afternoon")
    else:
        print("Good Evening!")
        speak("Good Evening!")
    print("Hello Shivam, i'm corpas How can i help you")
    speak("Hello Shivam, i'm corpas How can i help you")


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening..............")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('login email address', 'login email password')
    server.sendmail('receiving person email id', to, content)
    server.close()


if __name__ == '__main__':
    greeting()
    if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            # print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open notepad' in query:
            notepad_path = "C:\\Windows\\notepad.exe"
            os.startfile(notepad_path)

        elif 'open Chrome' in query:
            chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(chrome_path)

        elif 'take screenshot' in query:
            image = pyautogui.screenshot()
            image.save('screenshot.png')
            speak('Screenshot taken.')

        elif 'search' in query:
            speak("What do you want me to search for (please type) ? ")
            search_term = input()
            search_url = f"https://www.google.com/search?q={search_term}"
            webbrowser.get('C:\Program Files\Google\Chrome\Application\chrome.exe %s').open(search_url)
            speak(f"here are the results for the search term: {search_term}")

        elif 'open google' in query:
            chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(chrome_path)

        elif 'Saumil' in query:
            speak("Shaumil Bhosadi vale")

        elif 'search from google' in query:
            speak("Sir, what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open music' in query:
            music_dir = 'File Path'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open music' in query:
            music_path = ''
            song = os.listdir(music_path)
            rd = random.choice(song)
            for song in song:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_path, song))


        elif 'what is time' in query:
            strTime = dt.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'open VS code' in query:
            codePath = "C:\\Users\\Shivam Upadhyay\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = " email id hare"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sir Email not send please check the error")

        else:
            print("Sorry Sir i can't do this")
            speak("Sorry Sir i can't do this")