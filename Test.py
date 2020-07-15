import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 
import speech_recognition as sr
import pyttsx3
import pyautogui as p
import wikipedia
import webbrowser
import time
from time import sleep
import os
import datetime

def Notepad():
    files = open('C:\\Users\\User\\Desktop\\pynote.txt', 'a+', encoding='utf-8')
    note = ''
    writing = True
    speak('What should i write?')
    while writing:
        note = takecommand().lower()
        if note != 'quit':
            files.write(note)
            speak('Continue')
            print('Listening...')
        else:   
            files.close()    
            writing = False

                

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning Sir')
    elif hour >= 12 and hour< 18:
        speak('Good Afternoon Sir')
    else:
        speak('Good Evening Sir')

    speak("How may i help you?")    


def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        speak('Listening')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print('Please say that again...')
        speak('Please say that again')
        return "None"
    return query    

def facebook_login():
    user = "9706572670"
    paswd = "rishisarmah@"

    driver = webdriver.Chrome()
    driver.get('https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110')

    element = driver.find_element_by_name('email')
    element.send_keys(user)
    element = driver.find_element_by_id('pass')
    element.send_keys(paswd)
    element.send_keys(Keys.RETURN)
    

if __name__ == "__main__":

    wishme()

    while True:
        fquery = takecommand().lower()

        if 'wikipedia' in fquery:
            speak("Searching wikipedia")
            fquery = fquery.replace("wikipedia", "")
            result = wikipedia.summary(fquery, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'facebook' in fquery:
            speak('Logging into facebook')
            facebook_login()    

        elif 'open youtube' in fquery:
            speak('Opening youtube')
            webbrowser.open('Youtube.com')

        elif 'notepad' in fquery:
            Notepad()    

        elif 'terminate program' in fquery:
            exit()    
            






