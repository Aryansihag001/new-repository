from re import search
import pyttsx3
import datetime
import speech_recognition as sr
from pywikihow import search_wikihow
import wikipedia
import webbrowser
from playsound import playsound
import requests
import bs4
import psutil
from bs4 import BeautifulSoup
#from googlesearch import search



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# print(voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():                                         #wishme edith#
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Boss")

    elif hour>=12 and hour<18:
        speak("Good afternoon Boss")

    else:
        speak("Good evening Boss")

    speak("i am Edith, Please tell me how may i help you")          #Introduction #

def takecommand():                #Taking command #
    # it takes micro phone for the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")                       #searching the result foe boss     
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again Please...")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

                                                                  # search websites
        if 'website' in query: 
            my_result__list=[]
            for i in search(query,   # The query you want to run
                        tld = 'com',  # The top level domain
                        lang = 'en',  # The language
                        num = 10,     # Number of results per page
                        start = 0,    # First result to retrieve
                        stop = 10,  # Last result to retrieve
                        pause = 2.0,  # Lapse between HTTP requests
                        ):
                 my_result__list.append(i)
                 print(i)
            # Logic for axecuting tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            webbrowser.open("wikipedia.com")
        elif 'open youtube' in query:                              #youtube
            webbrowser.open("youtube.com")
        elif 'open google' in query:                               #google   
            webbrowser.open("Google.com")
        elif 'open gmail' in query:                                #gmail          
            webbrowser.open("gmail.com")
        elif "open shop" in query:                                 # online shopping(flipcart)          
            webbrowser.open('flipkart.com')
        elif "shut up" in query:                                   #  sorry to disturb u 
            speak('sorry to disturb you ')
        elif "Bye Bye" in query:                                    #  bye bye 
            speak('have a nice day')
            exit()
        elif "alarm" in query:                                        #alarm#
            speak("Tell me the time !")
            time=input(":tell me the time :")
            
            while True:
                Time_ac=datetime.datetime.now()
                now=Time_ac.strftime("%H:%M:%S") 
                
                if now==time:
                    speak("Time to wake up sir")
                    playsound('"D:\EDITH\JARVIS Wake Up Alarm.mp3"')     
                    speak('Alarm Closed!')
                 
                elif now>time:
                    break 
        elif "how to"in query :                                      ###ASK ANYTHING TO EDITH (SEACRH)###
            speak("Getting data from my collection !") 
            op=query.replace("Edith","")
            max_resutl=1
            how_to_func=search_wikihow(op,max_resutl)
            assert len(how_to_func)==1 
            how_to_func[0].print()
            speak(how_to_func[0].summary)  
            
            
            
        elif "how much power left"in query or "how much power we have "in query or "battery"in query:  #[battery percentage ,{How much batter is left in system}]##
            battery=psutil.sensors_battery()
            percentage= battery.percent
            speak(f"sir our system have{percentage} percent battery") 
            if percentage>=90:
                speak("we have enough power to continue our work")
            elif percentage>=50 and percentage<=90:
                speak(" we should connect our system to charging ")
            elif percentage<=15 and percentage>=30:
                speak("we dont have enough power to work")
            elif percentage<=15:
                speak(" Bad news        we dont have power  system will shut down soon ")        
                
                
def temp():                                                                          #TEMPERATURE#
    search="temperature in rajpura"
    url=f"https://www.google.com/search?q={search}"   
    r=requests.get(url)
    data= BeautifulSoup(r.text,"html.parser") 
    temperature=data.find("div",class_= "BNeawe").text
    speak(f"The Temperature Outside is {temperature}celcius")

       

   