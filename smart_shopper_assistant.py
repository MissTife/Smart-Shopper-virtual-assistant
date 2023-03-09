#!/usr/bin/env python
# coding: utf-8

# In[1]:


import speech_recognition as sr
import pyttsx3
import pyaudio
import datetime
import sys
import webbrowser


# In[ ]:



#create a function to get a reply
def speak(audio):
    lady=pyttsx3.init() 
    voices=lady.getProperty('voices')
    lady.setProperty('voice',voices[1].id)
    lady.say(audio)
    lady.runAndWait()
    print(audio)

# create a function to give command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening,please speak...")
        r.adjust_for_ambient_noise(source,duration=0.7)
        r.pause_threshold= 0.7
        audio= r.listen(source)
    try:
        print("Recognizing...") 
        command=r.recognize_google(audio,language='en-in') 
        print("user:" ,command)          
    except Exception as e:
        print(e)
        speak("sorry,i did not get that...")
        return "None"
        
    return command

#define any other additional function or task that you <br> want the assistant to do.
def username():
    speak("what should i call you?")
    name=takeCommand()
    speak("Hello "  + name)
    speak("welcome to Smart shopper,what would you like to shop for today?")

    
       
                                       
                    
def greet():
    hour=datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("Good Morning to you") 
    elif hour  >= 12 and hour < 18:
        speak("Good day to you") 
    elif hour >= 18 and hour < 24:
        speak("Good evening,hope you had a good day.")
    
# create the assistant function that execute the assistant as well as <br> other task that has been defined    
def run_lady():
    greet()
    username()
    
    while(True):
        query = takeCommand().lower()
        if "shop for" in query:
            speak('Loading result')  
            result_one=webbrowser.open("https://smart-shopper.onrender.com/",new=1)
            
        elif "my name" in query:
            username()
            continue
       
        elif "get"  in query:
            speak('Loading result')
            result_two=webbrowser.open("https://smart-shopper.onrender.com/",new=1)
            
            
        elif "brands"  in query:
            speak('Loading result')  
            result_three=webbrowser.open("https://smart-shopper.onrender.com/",new=1)

              
        elif "want" in query:
            speak("loading result")
            result=webbrowser.open("https://smart-shopper.onrender.com/",new=1)
            
          
        elif "buy" in query:
            speak('Loading result') 
            result_four=webbrowser.open("https://smart-shopper.onrender.com/",new=1)
            
            
        elif "prices"  in query:
            speak('Loading result') 
            result_five=webbrowser.open("https://smart-shopper.onrender.com/",new=1)
            
             
            
        elif "stores"  in query:
            speak('Loading result ')
            result_six=webbrowser.open("https://smart-shopper.onrender.com/",new=1)
            
        
                        
if __name__=='__main__':
    run_lady()
    


# In[ ]:




