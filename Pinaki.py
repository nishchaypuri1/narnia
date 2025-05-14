import json
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit 
from fnmatch import translate
from time import sleep
from googletrans import Translator
import googletrans #pip install googletrans +
from gtts import gTTS
import googletrans
from playsound import playsound
import time
from pynput.keyboard import Key,Controller
from time import sleep
import random
import pyautogui
import matplotlib as pt
import requests
from bs4 import BeautifulSoup
import webbrowser
import bs4
import wolframalpha
import ctypes,sys
import plyer
import speedtest
import pyjokes
import math
import enum
import cv2
from enum import IntEnum
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from google.protobuf.json_format import MessageToDict
import screen_brightness_control as sbcontrol
import json
from urllib.request import urlopen
import phonenumbers
from phonenumbers import timezone,geocoder,carrier
from opencage.geocoder import OpenCageGeocode
import folium
from tkinter import *
import tkinter as tk
import holidays
from datetime import date
import openai

openai.api_key = "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"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def answer_questions(input_text):
    completion = openai.Completion()
    response = completion.create(
        model = "text-davinci-002",
        prompt = input_text,
        temperature = 0.5,
        max_tokens = 100,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0
    )
    answer = response.choices[0].text.strip()
    return answer


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!!")
    else:
        speak("Good Evening!")

    speak("I am Pinaki a virtual assistant. How may I assist you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query
    except Exception as e:
        print("Say that again please...")
        return "None"

while True:
    if __name__ == "__main__":
        permission = takeCommand().lower()
        if "Pinaki" in permission or "Pinakin" in permission or "pinaki" in permission:
            wishMe()
            while True:
                query = takeCommand().lower()

                if 'wikipedia' in query:
                    speak('Searching online for best results...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2 )
                    speak("According to online search results")
                    print(results)
                    speak(results)

                elif "type mode" in query or "type mod" in query:
                        while True:
                            speak("Type mode on")
                            ques = input("ASK HERE : ")
                            print(answer_questions(ques))
                            speak(answer_questions(ques))

                            if "type mode off" in ques:
                                break
                            
                            
                            
                

                elif 'open youtube' in query:
                    webbrowser.open("youtube.com")

                elif 'open google' in query:
                    webbrowser.open("google.com")

                elif 'open gmail' in query:
                    webbrowser.open("mail.google.com")

                elif 'open stackoverflow' in query:
                    webbrowser.open("stackoverflow.com")

                elif 'open aniwatch' in query:
                    webbrowser.open("aniwatch.to")

                elif 'open whatsapp' in query:
                    webbrowser.open("web.whatsapp.com")

                elif 'open poki game online' in query:
                    webbrowser.open("poki.com")

                elif 'open chat gpt' in query:
                    webbrowser.open('chat.openai.com')

                elif 'open amazon' in query:
                    webbrowser.open('amazon.in')

                elif 'open flipkart' in query:
                    webbrowser.open('flipkart.com')

                elif 'play music' in query:
                    music_dir = 'C:\\Users\\User\\Music\\spotifydown.com'
                    music = os.listdir(music_dir)
                    print(music)
                    os.startfile(os.path.join(music_dir, music[0]))
                    

                elif 'open youtube' in query:
                    webbrowser.open("youtube.com")

                elif 'open google' in query:
                    webbrowser.open("google.com")

                elif 'open stackoverflow' in query:
                    webbrowser.open("stackoverflow.com")   


                elif 'play music' in query:
                    music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                    songs = os.listdir(music_dir)
                    print(songs)    
                    os.startfile(os.path.join(music_dir, songs[0]))

                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"the time is {strTime}")

                elif 'open code' in query:
                    codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)


                elif "search" in query:
                    import wikipedia as googleScrap
                    query = query.replace("raksha","")
                    query = query.replace("google search","")
                    query = query.replace("google","")
                    speak("This is what i found on google")
                                
                    try:
                        pywhatkit.search(query)
                        result = googleScrap.summary(query,1)
                        speak(result)

                    except:
                        speak("No speakable output available")

                    if "play" in query:
                        speak("This is what i found for your search!")
                        query = query.replace("youtube search","")
                        query = query.replace("youtube","")
                        query = query.replace("Raksha","")
                        web = "https://www.youtube.com/results?search_query=" + query
                        webbrowser.open(web)
                        pywhatkit.playonyt(query)
                        speak("Done")

                elif "what" in query or "who" in query or "when" in query or "where" in query :
                        print(answer_questions(query))
                        speak(answer_questions(query))

                elif "who is" in query:
                    speak("Searching from wikipedia....")
                    query = query.replace("wikipedia","")
                    query = query.replace("search wikipedia","")
                    query = query.replace("raksha","")
                    Results = wikipedia.summary(query,sentences = 2)
                    speak("According to wikipedia..")
                    print(Results)
                    speak(Results)

                elif "who is" in query:
                    speak("Searching from wikipedia....")
                    query = query.replace("wikipedia","")
                    query = query.replace("search wikipedia","")
                    query = query.replace("who is","")
                    query = query.replace("raksha","")
                    Results = wikipedia.summary(query,sentences = 2)
                    speak("According to wikipedia..")
                    print(Results)
                    speak(Results)

                elif 'volume up' in query:
                    for i in range(5):
                        keyboard = Controller()
                        keyboard.press(Key.media_volume_up)
                        keyboard.release(Key.media_volume_up)
                        sleep(0.1)

                elif 'volume down' in query:
                    for i in range(5):
                        keyboard = Controller()
                        keyboard.press(Key.media_volume_down)
                        keyboard.release(Key.media_volume_down)
                        sleep(0.1)

                elif 'game' in query:
                            speak("Lets Play ROCK PAPER SCISSORS !!")
                            print("LETS PLAYYYYYYYYYYYYYY")
                            i = 0
                            Me_score = 0
                            Com_score = 0
                            while(i<5):
                                choose = ("rock","paper","scissors") #Tuple
                                com_choose = random.choice(choose)
                                query = takeCommand().lower()
                                if (query == "rock"):
                                    if (com_choose == "rock"):
                                        speak("ROCK")
                                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                                    elif (com_choose == "paper"):
                                        speak("paper")
                                        Com_score += 1
                                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                                    else:
                                        speak("Scissors")
                                        Me_score += 1
                                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

                                elif (query == "paper" ):
                                    if (com_choose == "rock"):
                                        speak("ROCK")
                                        Me_score += 1
                                        print(f"Score:- ME :- {Me_score+1} : COM :- {Com_score}")

                                    elif (com_choose == "paper"):
                                        speak("paper")
                                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                                    else:
                                        speak("Scissors")
                                        Com_score += 1
                                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

                                elif (query == "scissors" or query == "scissor"):
                                    if (com_choose == "rock"):
                                        speak("ROCK")
                                        Com_score += 1
                                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                                    elif (com_choose == "paper"):
                                        speak("paper")
                                        Me_score += 1
                                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                                    else:
                                        speak("Scissors")
                                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                                        i += 1
                    
                                        print(f"FINAL SCORE :- ME :- {Me_score} : COM :- {Com_score}")

                                elif (query == "stop"):
                                    break
                            
                elif "pause" in query:
                                    pyautogui.press("k")
                                    speak("video paused")
                elif "start" in query:
                                    pyautogui.press("k")
                                    speak("video played")
                elif "mute" in query:
                                    pyautogui.press("m")
                                    speak("video muted")
                elif "forward"in query:
                                    pyautogui.press("l")
                                    speak("done")
                elif "rewind" in query:
                                    pyautogui.press("j")
                                    speak("done")

                elif "weather" in query:
                                    search = "temperature in delhi"
                                    url = f"https://www.google.com/search?q={search}"
                                    r  = requests.get(url)
                                    data = BeautifulSoup(r.text,"html.parser")
                                    temp = data.find("div", class_ = "BNeawe").text
                                    speak(f"current{search} is {temp}")
                elif "temperature" in query:
                                    search = "temperature in delhi"
                                    url = f"https://www.google.com/search?q={search}"
                                    r  = requests.get(url)
                                    data = BeautifulSoup(r.text,"html.parser")
                                    temp = data.find("div", class_ = "BNeawe").text
                                    speak(f"current{search} is {temp}")

                elif "google" in query:
                            import wikipedia as googleScrap
                            query = query.replace("raksha","")
                            query = query.replace("google search","")
                            query = query.replace("google","")
                            speak("This is what i found on google")

                            try:
                                pywhatkit.search(query)
                                result = googleScrap.summary(query,1)
                                speak(result)

                            except:
                                speak("No speakable output available")

                elif "who is" in query:
                            speak("Searching from wikipedia....")
                            query = query.replace("wikipedia","")
                            query = query.replace("search wikipedia","")
                            query = query.replace("raksha","")
                            Results = wikipedia.summary(query,sentences = 2)
                            speak("According to wikipedia..")
                            print(Results)
                            speak(Results)

                elif "youtube" in query:
                            speak("This is what i found for your search!")
                            query = query.replace("youtube search","")
                            query = query.replace("youtube","")
                            query = query.replace("Pinaki","")
                            web = "https://www.youtube.com/results?search_query=" + query
                            webbrowser.open(web)
                            pywhatkit.playonyt(query)
                            speak("Done, Sir")

                elif "open" in query:
                            query = query.replace("raksha","")
                            query = query.replace("open","")
                            pyautogui.press("super")
                            pyautogui.typewrite(query)
                            pyautogui.sleep(2)
                            pyautogui.press("enter")
                        
                elif "alarm" in query:
                            speak("Enter the time")
                            Time = input(":Enter the time:")

                            while True:
                                Time_Ac = datetime.datetime.now()
                                now = Time_Ac.strftime("%H:%M:%S")

                                if now==Time:
                                    speak("Time to wake up")
                                    playsound("https://www.youtube.com/watch?v=xfMN4SpIxIA")
                                elif Time>now:
                                    break

                        
                elif "one tab" in query or "1 tab" in query:
                            pyautogui.hotkey("ctrl","w")
                            speak("All tabs closed")
                elif "2 tab" in query:
                            pyautogui.hotkey("ctrl","w")
                            sleep(0.5)
                            pyautogui.hotkey("ctrl","w")
                            speak("All tabs closed")
                elif "3 tab" in query:
                            pyautogui.hotkey("ctrl","w")
                            sleep(0.5)
                            pyautogui.hotkey("ctrl","w")
                            sleep(0.5)
                            pyautogui.hotkey("ctrl","w")
                            speak("All tabs closed")
                            
                elif "4 tab" in query:
                            pyautogui.hotkey("ctrl","w")
                            sleep(0.5)
                            pyautogui.hotkey("ctrl","w")
                            sleep(0.5)
                            pyautogui.hotkey("ctrl","w")
                            sleep(0.5)
                            pyautogui.hotkey("ctrl","w")
                            speak("All tabs closed")
                elif "5 tab" in query:
                            pyautogui.hotkey("ctrl","w")
                            sleep(0.5)
                            pyautogui.hotkey("ctrl","w")
                            sleep(0.5)
                            pyautogui.hotkey("ctrl","w")
                            sleep(0.5)
                            pyautogui.hotkey("ctrl","w")
                            sleep(0.5)
                            pyautogui.hotkey("ctrl","w")
                            speak("All tabs closed")

                elif ".com" in query or ".co.in" in query or ".org" in query:
                            dictapp = {"commandprompt":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt"}
                            query = query.replace("open","")
                            query = query.replace("raksha","")
                            query = query.replace("launch","")
                            query = query.replace(" ","")
                            webbrowser.open(f"https://www.{query}")


                elif "thanks" in query or "thankyou" in query:
                            speak("No need , that's my job")
                elif "nice" in query:
                            speak("thankyou")
                elif "how are you" in query:
                            speak("i am fine , thanks for asking. what about you")
                elif "hello" in query:
                            speak("namaste")
                elif "i am fine" in query:
                            speak("great to hear")            

                elif "off" in query:
                            speak("You can still call me anytime")
                            break
                elif "hello" in query:
                            wishMe()
                elif "yourfather" in query:
                            speak("Nishchay")
                elif "your creator" in query:
                            speak("Nishchay Puri")
                        

                elif "i am tired" in query:
                            speak("Let me play your favourite anime")
                            webbrowser.open("https://aniwatch.to/watch/one-piece-100?ep=107275")

                elif "shutdown system" in query:
                            speak("Are You sure you want to shutdown")
                            shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                            if shutdown == "yes":
                                os.system("shutdown /s /t 1")

                            elif shutdown == "no":
                                break

                elif "focus mode" in query:
                            def is_admin():
                                try:
                                    return ctypes.windll.shell32.IsUserAnAdmin()
                                except:
                                    return False
                            if is_admin():
                                current_time = datetime.datetime.now().strftime("%H:%M")
                                Stop_time = input("Enter time example:- [10:10]:- ")
                                a = current_time.replace(":",".")
                                a = float(a)
                                b = Stop_time.replace(":",".")
                                b = float(b)
                                Focus_Time = b-a
                                Focus_Time = round(Focus_Time,3)
                                host_path ='C:\Windows\System32\drivers\etc\hosts'
                                redirect = '127.0.0.1'

                    
                                print(current_time)
                                time.sleep(2)
                                website_list = ["www.facebook.com","facebook.com","www.instagram.com","instagram.com"]
                                if (current_time < Stop_time):
                                    with open(host_path,"r+") as file: #r+ is writing+ reading
                                        content = file.read()
                                        time.sleep(2)
                                        for website in website_list:    
                                            if website in content:
                                                pass
                                        else:
                                            file.write(f"{redirect} {website}\n")
                                            print("DONE")
                                            time.sleep(1)
                                            print("FOCUS MODE TURNED ON !!!!")


                                    while True:     
                        
                                        current_time = datetime.datetime.now().strftime("%H:%M")
                                        website_list = ["www.facebook.com","facebook.com","www.instagram.com","instagram.com","youtube.com","www.youtube.com"]
                                        if (current_time >= Stop_time):
                                            with open(host_path,"r+") as file:
                                                content = file.readlines()
                                                file.seek(0)

                                                for line in content:
                                                    if not any(website in line for website in website_list):
                                                        file.write(line)

                                                        file.truncate()

                                                        print("Websites are unblocked !!")
                                                        file = open("focus.txt","a")
                                                        file.write(f",{Focus_Time}")        #Write a 0 in focus.txt before starting
                                                        file.close()
                                                        break 

                                                else:
                                                    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                                                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                                                    if (a==1):
                                                        speak("Entering the focus mode....")
                                                        exit()
                                                    else:
                                                        pass

                elif "match score" in query:
                                    from plyer import notification  #pip install plyer
                                    import requests #pip install requests
                                    from bs4 import BeautifulSoup #pip install bs4
                                    url = "https://www.cricbuzz.com/"
                                    page = requests.get(url)
                                    soup = BeautifulSoup(page.text,"html.parser")
                                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                                    a = print(f"{team1} : {team1_score}")
                                    b = print(f"{team2} : {team2_score}")

                                    notification.notify(
                                        title = "MATCH SCORE :- ",
                                        message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                                        timeout = 15
                                    )

                elif "cricket" in query:
                            speak("loading")
                            webbrowser.open("https://www.google.com/search?q=cricket+&rlz=1C1VDKB_enIN1014IN1014&sxsrf=ALiCzsY38KD1ZCXqGRXwDdX3ogaHu-lHhQ%3A1661843974982&ei=BroNY6LHO46OseMP_riT4AM&ved=0ahUKEwii4rOeg-75AhUOR2wGHX7cBDwQ4dUDCA4&uact=5&oq=cricket+&gs_lcp=Cgdnd3Mtd2l6EAMyDQguELEDEIMBENQCEEMyCggAEIAEEIcCEBQyEAgAEIAEEIcCELEDEIMBEBQyCwgAEIAEELEDEIMBMgoIABCxAxCDARBDMgsIABCABBCxAxCDATINCC4QsQMQgwEQ1AIQQzILCC4QgAQQsQMQgwEyCwgAEIAEELEDEIMBMgQIABBDOgcIABBHELADOgcIABCwAxBDOgoIABDkAhCwAxgBOgwILhDIAxCwAxBDGAI6CAgAEIAEELEDOgUIABCABEoECEEYAEoECEYYAVDtB1jCEWCBGmgBcAF4AIABnwGIAfoIkgEDMC45mAEAoAEByAETwAEB2gEGCAEQARgJ2gEGCAIQARgI&sclient=gws-wiz")

                elif "internet speed" in query:
                                    wifi  = speedtest.Speedtest
                                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                                    download_net = wifi.download()/1048576
                                    print("Wifi Upload Speed is", upload_net)
                                    print("Wifi download speed is ",download_net)
                                    speak(f"Wifi download speed is {download_net}")
                                    speak(f"Wifi Upload speed is {upload_net}")

                elif "screenshot" in query:
                                    import pyautogui #pip install pyautogui
                                    im = pyautogui.screenshot()
                                    im.save("ss.jpg")

                elif "click my photo" in query:
                                    pyautogui.press("super")
                                    pyautogui.typewrite("camera")
                                    pyautogui.press("enter")
                                    pyautogui.sleep(2)
                                    speak("SMILE")
                                    pyautogui.press("enter")
                        
                elif "joke" in query:
                            print(pyjokes.get_joke())
                            speak(pyjokes.get_joke())


                elif "remember that" in query:
                                    rememberMessage = query.replace("remember that","")
                                    rememberMessage = query.replace("raksha","")
                                    speak("You told me to"+rememberMessage)
                                    remember = open("Remember.txt","a")
                                    remember.write(rememberMessage)
                                    remember.close()
                elif "what do you remember" in query:
                                    remember = open("Remember.txt","r")
                                    speak("You told me to remember that" + remember.read())

                elif "show my focus" in query:
                            def focus_graph():
                                file = open("focus.txt","r")
                                content = file.read()
                                file.close()

                                content = content.split(",")
                                x1 = []
                                for i in range(0,len(content)):
                                    content[i] = float(content[i])
                                    x1.append(i)

                                print(content)
                                y1 = content

                                pt.plot(x1,y1,color = "red",marker = "o")
                                pt.title("YOUR FOCUSED TIME",fontsize = 16)
                                pt.xlabel("Times",fontsize = 14)
                                pt.ylabel("Focus Time", fontsize = 14)
                                pt.grid()
                                pt.show()
                elif "send a message" in query:
                            def sendMessage():
                                speak("Who do you wan to message")
                                a = int(input('''Person 1 - 1
                                Person 2 - 2'''))
                                if a == 1:
                                    speak("Whats the message")
                                    message = str(input("Enter the message- "))
                                    pywhatkit.sendwhatmsg("+919990220076",message,time_hour=21,time_min=8) #Enter The number here instead of +91000
                                elif a==2:
                                    speak("Whats the message")
                                    message = str(input("Enter the message- "))
                                    pywhatkit.sendwhatmsg("+918447172277",message,time_hour=14,time_min=14)
                                    pass
                            sendMessage()


                elif "current location" in query:
                            url = 'http://ipinfo.io/json'
                            response = urlopen(url)
                            data=json.load(response)

                            print(data)
                            speak(data)

                elif "phone details" in query:
                            number = input("ENTER YOUR NUMBER WITH +__")
                            phone = phonenumbers.parse(number)
                            location = geocoder.description_for_number(phone , "en")
                            car = carrier.name_for_number(phone , "en")
                            key = 'a6b06c274260424aae368a5f9be1cf97'

                            geocoder = OpenCageGeocode(key)
                            loc = str(location)
                            lamp = geocoder.geocode(loc)
                            print(lamp)

                            lat = lamp[0]['geometry']['lat']
                            lng = lamp[0]['geometry']['lng']

                            print(lat , lng)
                            print(phone)
                            print(car)
                            print(key)
                            print(location)
                            speak(phone)
                            speak(car)
                            speak(key)
                            speak(location)
                            

                            myMap = folium.Map(location=[lat , lng] , zoom_start=9)
                            folium.Marker([lat , lng],popup=location).add_to(myMap)
                            myMap.save("mylocation.html")
                            

                elif "convert unit" in query:
                            speak("Which unit would you like to convert")
                            print("1. Length")
                            print("2. Weight")
                            ch = input()
                            if "length" in ch:
                                window = Tk()
                                window.title("Lenght Converter")
                                window.geometry("500x300+550+355")
                                def lengthconv():
                                    
                                    km = float(e2_value.get())/1000
                                    mm = float(e2_value.get())*1000
                                    cm = float(e2_value.get())*100
                                    mile=float(e2_value.get())*0.00062
                                    yard=float(e2_value.get())*1.094
                                    inch=float(e2_value.get())*39.37 
                                    foot=float(e2_value.get())*3.281
                                    dm=float(e2_value.get())*10
                                    
                                    t1.delete("1.0", END)
                                    t1.insert(END,km)
                                    
                                    t2.delete("1.0", END)
                                    t2.insert(END,mm)
                                    
                                    t3.delete("1.0", END)
                                    t3.insert(END,cm)
                                    
                                    t4.delete("1.0", END)
                                    t4.insert(END,mile)
                                
                                    t5.delete("1.0", END)
                                    t5.insert(END,yard)
                                    
                                    t6.delete("1.0", END)
                                    t6.insert(END,inch)
                                    
                                    t7.delete("1.0", END)
                                    t7.insert(END,foot)
                                    
                                    t8.delete("1.0", END)
                                    t8.insert(END,dm)
                                    
                                # Creating Label widgets
                                e1 = Label(window, text = "Enter length in meters",bg="light gray")
                                e2_value = StringVar()
                                e2 = Entry(window, textvariable = e2_value)
                                e3 = Label(window, text = 'km',bg="light gray")
                                e4 = Label(window, text = 'mm',bg="light gray")
                                e5 = Label(window, text = 'cm',bg="light gray")
                                e6 = Label(window, text = 'mile',bg="light gray") 
                                e7 = Label(window, text = 'yard',bg="light gray") 
                                e8 = Label(window, text = 'inch',bg="light gray") 
                                e9 = Label(window, text = 'foot',bg="light gray") 
                                e10 = Label(window, text = 'dm',bg="light gray") 
                                # Creating Text Widgets
                                t1 = Text(window, height = 1, width = 15)
                                t2 = Text(window, height = 1, width = 15)
                                t3 = Text(window, height = 1, width = 15)
                                t4 = Text(window, height = 1, width = 15) 
                                t5 = Text(window, height = 1, width = 15) 
                                t6 = Text(window, height = 1, width = 15)
                                t7 = Text(window, height = 1, width = 15)
                                t8 = Text(window, height = 1, width = 15)
                                # Creating  Button Widget
                                b1 = Button(window, text = "Convert", command = lengthconv)
                                
                                e1.grid(row = 0, column = 0,padx=10,pady=10)
                                e2.grid(row = 0, column = 1,pady=10,padx=10)
                                e3.grid(row = 4, column = 0,pady=10,padx=10)
                                e4.grid(row = 2, column = 0,pady=10,padx=10)
                                e5.grid(row = 3, column = 0,pady=10,padx=10)
                                e6.grid(row = 2, column = 2,pady=10,padx=10)
                                e7.grid(row = 4, column = 2,pady=10,padx=10)
                                e8.grid(row = 3, column = 2,pady=10,padx=10)
                                e9.grid(row = 5, column = 0,pady=10,padx=10)
                                e10.grid(row = 5, column = 2,pady=10,padx=10)
                                t1.grid(row = 4, column = 1,pady=10,padx=10)
                                t2.grid(row = 2, column = 1,pady=10,padx=10)
                                t3.grid(row = 3, column = 1,pady=10,padx=10)
                                t4.grid(row = 2, column = 3,pady=10,padx=10)
                                t5.grid(row = 4, column = 3,pady=10,padx=10)
                                t6.grid(row = 3, column = 3,pady=10,padx=10)
                                t7.grid(row = 5, column = 1,pady=10,padx=10)
                                t8.grid(row = 5, column = 3,pady=10,padx=10)
                                b1.grid(row = 1, column = 1,padx=10,pady=10)
                                
                                exit_button = Button(window, text="Exit", command=window.destroy) 
                                exit_button.place(x=450,y=255)

                                window.mainloop()

                            lengthconv()

                            if "weight" in ch:
                                window = Tk()
                                window.title("Weight Converter")
                                window.geometry("500x300+550+355")
                                def weightconv():
                                    
                                    kg = float(e2_value.get())/1000
                                    mg = float(e2_value.get())*1000
                                    cg = float(e2_value.get())/100
                                    dcg=float(e2_value.get())/10
                                    hg=float(e2_value.get())*100
                                    tonne=float(e2_value.get())/1000000
                                    dg=float(e2_value.get())*10
                                    g=float(e2_value.get())*1
                                    
                                    t1.delete("1.0", END)
                                    t1.insert(END,kg)
                                    
                                    t2.delete("1.0", END)
                                    t2.insert(END,mg)
                                    
                                    t3.delete("1.0", END)
                                    t3.insert(END,cg)
                                    
                                    t4.delete("1.0", END)
                                    t4.insert(END,dcg)
                                
                                    t5.delete("1.0", END)
                                    t5.insert(END,hg)
                                    
                                    t6.delete("1.0", END)
                                    t6.insert(END,tonne)

                                    t7.delete("1.0", END)
                                    t7.insert(END,g)
                                    
                                    t8.delete("1.0", END)
                                    t8.insert(END,dg)
                                    
                                # Creating Label widgets
                                e1 = Label(window, text = "Enter weight in grams",bg="light gray")
                                e2_value = StringVar()
                                e2 = Entry(window, textvariable = e2_value)
                                e3 = Label(window, text = 'kg',bg="light gray")
                                e4 = Label(window, text = 'mg',bg="light gray")
                                e5 = Label(window, text = 'cg',bg="light gray")
                                e6 = Label(window, text = 'decigram',bg="light gray") 
                                e7 = Label(window, text = 'hectagram',bg="light gray") 
                                e8 = Label(window, text = 'tonne',bg="light gray")
                                e9 = Label(window, text = 'gram',bg="light gray")  
                                e10 = Label(window, text = 'decagram',bg="light gray") 
                                # Creating Text Widgets
                                t1 = Text(window, height = 1, width = 15)
                                t2 = Text(window, height = 1, width = 15)
                                t3 = Text(window, height = 1, width = 15)
                                t4 = Text(window, height = 1, width = 15) 
                                t5 = Text(window, height = 1, width = 15) 
                                t6 = Text(window, height = 1, width = 15)
                                t7 = Text(window, height = 1, width = 15)
                                t8 = Text(window, height = 1, width = 15)
                                # Creating  Button Widget
                                b1 = Button(window, text = "Convert", command = weightconv)
                                
                                e1.grid(row = 0, column = 0,padx=10,pady=10)
                                e2.grid(row = 0, column = 1,pady=10,padx=10)
                                e3.grid(row = 4, column = 0,pady=10,padx=10)
                                e4.grid(row = 2, column = 0,pady=10,padx=10)
                                e5.grid(row = 3, column = 0,pady=10,padx=10)
                                e6.grid(row = 2, column = 2,pady=10,padx=10)
                                e7.grid(row = 4, column = 2,pady=10,padx=10)
                                e8.grid(row = 3, column = 2,pady=10,padx=10)
                                e9.grid(row = 5, column = 0,pady=10,padx=10)
                                e10.grid(row = 5, column = 2,pady=10,padx=10)
                                t1.grid(row = 4, column = 1,pady=10,padx=10)
                                t2.grid(row = 2, column = 1,pady=10,padx=10)
                                t3.grid(row = 3, column = 1,pady=10,padx=10)
                                t4.grid(row = 2, column = 3,pady=10,padx=10)
                                t5.grid(row = 4, column = 3,pady=10,padx=10)
                                t6.grid(row = 3, column = 3,pady=10,padx=10)
                                t7.grid(row = 5, column = 1,pady=10,padx=10)
                                t8.grid(row = 5, column = 3,pady=10,padx=10)
                                b1.grid(row = 1, column = 1,padx=10,pady=10)
                                
                                exit_button = Button(window, text="Exit", command=window.destroy) 
                                exit_button.place(x=450,y=255)

                                window.mainloop()

                            weightconv()

                elif "date" in query:
                            current_date = datetime.datetime.now().strftime("%D:%M:%Y")
                            speak(f"The date today is{current_date}")

                elif "zodiac"in query:
                            Year = input("year of birth:" )
                            Month = input("month of birth:" )
                            Day = input("day of birth:" )
                            Date_of_Birth = (Day + "/" + Month + "/" + Year)
                            print('Your Date of Birth is ' + Date_of_Birth)
                            d = date.today()
                            y = d.year
                            os.system("cls")
                            age = y - int(Year)
                            print('Your age is ' + str(age))

                            if ((int(Month)==12 and int(Day) >= 22)or(int(Month)==1 and int(Day)<= 19)):
                                    Signo_Zodiacal = ("\n Capricorn")
                            elif ((int(Month)==1 and int(Day) >= 20)or(int(Month)==2 and int(Day)<= 17)):
                                    zodiac_sign = ("\n aquarium")
                            elif ((int(Month)==2 and int(Day) >= 18)or(int(Month)==3 and int(Day)<= 19)):
                                    zodiac_sign = ("\n Pices")
                            elif ((int(Month)==3 and int(Day) >= 20)or(int(Month)==4 and int(Day)<= 19)):
                                    zodiac_sign = ("\n Aries")
                            elif ((int(Month)==4 and int(Day) >= 20)or(int(Month)==5 and int(Day)<= 20)):
                                    zodiac_sign = ("\n Taurus")
                            elif ((int(Month)==5 and int(Day) >= 21)or(int(Month)==6 and int(Day)<= 20)):
                                    zodiac_sign = ("\n Gemini")
                            elif ((int(Month)==6 and int(Day) >= 21)or(int(Month)==7 and int(Day)<= 22)):
                                    zodiac_sign = ("\n Cancer")
                            elif ((int(Month)==7 and int(Day) >= 23)or(int(Month)==8 and int(Day)<= 22)): 
                                    zodiac_sign = ("\n Leo")
                            elif ((int(Month)==8 and int(Day) >= 23)or(int(Month)==9 and int(Day)<= 22)): 
                                    Signo_Zodiacal = ("\n Virgo")
                            elif ((int(Month)==9 and int(Day) >= 23)or(int(Month)==10 and int(Day)<= 22)):
                                    zodiac_sign = ("\n Libra")
                            elif ((int(Month)==10 and int(Day) >= 23)or(int(Month)==11 and int(Day)<= 21)): 
                                    zodiac_sign = ("\n Scorpio")
                            elif ((int(Month)==11 and int(Day) >= 22)or(int(Month)==12 and int(Day)<= 21)):
                                    zodiac_sign = ("\n Sagittarius")

                            print(zodiac_sign)


                elif "holidays" in query:
                            speak("Which year would you like to know")
                            year = int(input("Enter the year : "))

                            for day in sorted(holidays.India(years = year).items()):
                                print(day)
                                speak(day)

                elif "go" in query:
                        speak("Thankyou , you can still call me anytime")
                        print("Thankyou , you can still call me anytime")
                        break
 



# 5th issue in focus mode
