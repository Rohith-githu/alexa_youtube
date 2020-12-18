from modules import *
"""
Microphone input
"""
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print('Listening...')
        audio = r.listen(source)
    try :
        print('recognizing...')
        query = r.recognize_google(audio, language = 'en-in')
        print(f'You said : {query}\n')
    except Exception as e :
        print(e)
        print('Please say that again...')
        return 'None'
    return query
"""
speaker
"""
def speak(para) :
    engine =  pyttsx3.init()
    engine.say(para)
    engine.runAndWait()

def sp(para) :
    engine =  pyttsx3.init()
    print(para)
    engine.say(para)
    engine.runAndWait()
"""
greet
"""
def greeting() :
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <=12 :
        print('Good morning!')
        speak('Good morning sir, what can i help you with')
    elif hour >= 12 and hour < 16 :
        print('Good afternoon!')
        speak('Good afternoon sir, what can i help you with')
    elif hour >= 16 and hour < 20 :
        print('Good Evening!')
        speak('Good Evening sir, what can i help you with')
    else :
        sp('Ohh it\'s not a time to work with PC')