"""
Author: Alexander Angel
Date: 6/04/2019

Project: I get distracted while I am studying on my computer. 
I also have to spend time in setting up my study space.
It's difficult to track my studying time.

Auxiliarly: 
It's hard to find very good learning resources.
Most google searches return a clickbait article rather than a really good source.
I'm reading an article by a  VC at Y Combinator, he has articles on his own website. 
This resource is better than everything I could be taught at university or read in a 500 word article.


How the program will function:
- Start study session.
- Options for which topic to study (Math, Econ, etc)
- Initializes preset music, textbook, articles, resources, and medium to study on (word doc) so everything I 
need to study is ready in the click of a button.
- A timer gives me a break every 30 minutes (option to hide it).
- At the end of my session I will be able to stop the session, and resume where I left off for my next session.
** Usually I have 10 tabs open, my music playing, and multiple pdfs open to study a single topic. After my 
studying I will close all these. When I come back to studying, I have to re-open everything. That's a pain in the
ass.**
- Each session saves the amount of time I studied.
- The program analyzes my studying metrics to give me the optimal time to study, 
which is based on some critera (when do I study the most? <- indicates when I like to study)

Pseudocode:
main.py
    Starts the program.
    Gives me option to start session with which topic. (Option to set amount of time to study?)
maps.py
    Initializes sessions.
    Loads music.
    Loads recent files.
    Loads recent browser tabs.
    Starts an internal clock.
    Notifies me of breaks.
data.py
    Collects my studying data.
    Returns some analysis of my data
"""
import webbrowser
import urllib
from threading import Timer

class Session(object):
    def __init__(self):
        pass

    def choose_session(self):
        topics = ['Mathematics', 'Economics']
        print('\n***List of topics below.***\n' + '\n' + str(topics) + '\n')
        choose_topic = input('Which topic would you like? ').lower()
        for topic in topics:
            if choose_topic == topic.lower():
                self.session = choose_topic
                self.break_time = int(input('How much break time would you like? '))
                self.start_session()
                break
            elif topic == topics[-1]:
                print('\nTopic not found. Please select again. \n')
                self.choose_session()
    def start_session(self):
        """
        Get urls.
        Get playlist.
        Get files.
        Start session clock.
        """
        print(self.session)
        self.get_urls()
        #self.start_clock()
        #webbrowser.open('http://github.com/alexangelj')
    def get_urls(self):
        url_file = open('url_file.txt', 'r')
        for line in url_file:
            #webbrowser.open(line)
            pass
        url_file.close()

    def close_urls(self):
        pass
    
    def start_clock(self):
        time = Timer(self.break_time * 10, 'timeout')
        time.start()
        time.join()

    

Session().get_urls()