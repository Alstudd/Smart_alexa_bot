import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text) 
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'travis' in command:
                command = command.replace('travis', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'time' in user_input:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print(time)
    elif 'play' in user_input:
        song = user_input.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif ('who is' in user_input) or ('what is' in user_input) or ('where' in user_input):
        person = user_input.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
        print('I am in a relationship with wifi')
    elif 'joke' in command:
        funny = pyjokes.get_joke()
        talk(funny)
        print(funny)
    else:
        talk('Please say the command again.')
        print('Please say the command again.')

run_alexa()
