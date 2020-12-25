from modules import *
from settings import *
greeting()
while True:
    takecommand()
    query = takecommand().lower()

    if query == 'hi' :
        sp('hi sir')
    elif 'bye' in query:
        sp('bye sir lets meet next time')
        exit()
    elif 'who are you' in query :
        sp('Hi i am alexa made by Rohith')
    elif 'open chrome' in query :
        webbrowser.open('chrome.exe')
    elif 'open edge' in query :
        webbrowser.open('msedge.exe')
    elif 'google' in query :
        query = query.replace('google', '')
        webbrowser.open('https://www.google.com/search?q=' + query)
    elif 'github' in query :
        query = query.replace('github', '')
        webbrowser.open('https://www.github.com/search?q=' + query)
    elif 'git hub' in query :
        query = query.replace('git hub', '')
        webbrowser.open('https://www.github.com/search?q=' + query)
    elif 'wikipedia' in query :
        sp('Searching wikipedia....')
        query = query.replace('wikipedia', '')
        results = wikipedia.summary(query, sentences = 3)
        sp('According to wikipedia...')
        sp('results')
    elif 'the time' in query :
        strtime = datetime.datetime.now().strtime('%H:%M')
        sp(f'the time is {strtime}')
    elif 'youtube' in query :
        query = query.replace('youtube', '')
        webbrowser.open(f'https://www.youtube.com/results?search_query={query}')
    elif 'play' in query :
        query = query.replace('play', '')
        pywhatkit.playonyt(query)