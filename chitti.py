import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyttsx3
import smtplib
import random
import requests
import pywhatkit
import os
import sys
import json
import subprocess
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from win32com.client import Dispatch

def speak(str):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.speak(str)

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(Time)

def date():
    year = int (datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    speak("Welcome sir!")
    if hour>=5 and hour<=12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    elif hour>=18 and hour<21:
        speak("Good Evening!")

    else:
        speak("Enjoy your night time!!!")
    speak("the current time is")
    time()
    speak("the corrent date is")
    date() 
    speak("i am chitti ,at your service, please tell me how can i help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower() 
                               #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  
                              #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            # print(results)
            speak(results)

        elif 'hello' in query:
            speak('Hello Sir')


        elif "what's up" in query or 'how are you' in query:
            stMsgs = ['just doing my thing!', 'i am fine!', 'nice!', 'i am nice and full of energy']
            speak(random.choice(stMsgs))


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()


        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'the date' in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("the current Date is")
            speak(date)
            speak(month)
            speak(year)


        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s')


        elif 'make you' in query or 'created you' in query or 'develop you' in query:
            ans_m = " For your information Ankit Kumar Ghosh Created me ! I give Lot of Thannks to Him "
            #print(ans_m)
            speak(ans_m)


        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am chitti an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
            #print(about)
            speak(about)


        elif "your name" in query or "sweat name" in query:
            na_me = "Thanks for Asking my name my self ! chitti"  
            #print(na_me)
            speak(na_me)


        elif "your feeling" in query:
            #print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you") 


        elif 'how is the weather' in query:
            url = 'http://api.openweathermap.org/data/2.5/weather?q=kolkata&appid=8de226305ed875b15c242b05f66000a5'#Open api link here

            res = requests.get(url)

            data = res.json()

            weather = data['weather'] [0] ['main'] 
            temp = data['main']['temp']
            wind_speed = data['wind']['speed']

            latitude = data['coord']['lat']
            longitude = data['coord']['lon']

            description = data['weather'][0]['description']
            speak('Temperature : {} degree celcius'.format(temp))
            print('Wind Speed : {} m/s'.format(wind_speed))
            print('Latitude : {}'.format(latitude))
            print('Longitude : {}'.format(longitude))
            print('Description : {}'.format(description))
            print('weather is: {} '.format(weather))
            speak('weather is : {} '.format(weather))


        elif 'send sms' in query:
            speak("ok i am send sms")
            def send_sms(number,message):
                url = 'https://www.fast2sms.com/dev/bulk'
                params={
                    'authorization':'hVJIMyDgWaE90OGYoLmvxfbUcKtw36NCQlPzn57kXpiZ8Td4FuyqWkDZ0js2wefiJT7tEnK8uUg9l3NB',
                    'sender_id':'SMSIND',
                    'message':message,

                    'language':'english',
                    'route':'p',
                    'numbers':number
                }
                response=requests.get(url, params=params)
                dict=response.json()
                print(dict)
            send_sms("9007987374","hi'I am chitti an AI  based computer program ,Ankit Kumar Ghosh Created me. he is my sir, he  tell that he loves you")
 

        elif 'send message' in query:
            speak("ok sir i am send a whatsapp message")
            #for i in range(100):
            pywhatkit.sendwhatmsg("+919903808275", "hi i am chitti",13,45)
            speak("ok sir successful send the message")

        elif 'check the phone number'in query:
            speak("yes sir why not plz give the number , i am justify the number")
            ch_number = phonenumbers.parse("+919677097657",'ch')
            print(geocoder.description_for_number(ch_number,'en'))

            ro_number= phonenumbers.parse("+919677097657","RO")
            print(carrier.name_for_number(ro_number,"en"))


        elif 'email send' in query:
            speak('Who is the recipient? ')
            recipient = takeCommand()

            if 'myself' in recipient:
                try:
                    speak('What should I say? ')
                    content = takeCommand()
                    subject="I am chitti an A I based computer program but i can help you lot like a your close friend,i send this email"

                    message="subject:{}\n\n{}".format(subject,content)
                    #print("message")
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("jaydippramanick123@gmail.com", 'ankitghosh@00')
                    server.sendmail('jaydippramanick123@gmail.com', "ghosh.ankit.00@gmail.com", message, content) #'subject'Causes trouble
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')
        

   #online webside

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")

        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")

        elif 'open tinder' in query:
            webbrowser.open("tinder.com")

        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")

        elif 'open messenger' in query:
            webbrowser.open("messenger.com")

        elif 'open line' in query:
            webbrowser.open("line.com")

        elif 'open telegram' in query:
            webbrowser.open("telegram.com")
        
        elif 'open internshala' in query:
            webbrowser.open("internshala.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open snapchat' in query:
            webbrowser.open("snapchat.com")

        elif 'open google meet' in query:
            webbrowser.open("meetup.com")

        elif 'open xing' in query:
            webbrowser.open("xing.com")

        elif 'open skype' in query:
            webbrowser.open("medium.com")
        
        elif 'open amazon' in query:
            webbrowser.open("amazon.com")

        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")

        elif 'open coursera' in query:
            webbrowser.open("coursera.com")

        elif 'open udamy' in query:
            webbrowser.open("https://www.udemy.com")

        elif 'open hackerrank' in query:
            webbrowser.open("hackerrank.com")

        elif 'open swayam' in query:
            webbrowser.open("swayam.com")

        elif 'open hotstar' in query:
            webbrowser.open("hotstar.com")

        elif 'open hangouts' in query:
            webbrowser.open("hangouts.com")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")

        elif 'open gaana' in query:
            webbrowser.open("gaana.com")

        elif 'open iemcrp' in query:
            webbrowser.open("https://www.iemcrp.com")


        elif 'play music' in query:
            speak('Okay, here is your music! Enjoy!')
            music_dir = 'D:\\Bengali Songs'
            songs = os.listdir(music_dir)
            #print(songs)
            n = len(songs)
            index = random.randint(0,n)
            os.startfile(os.path.join(music_dir,songs[index]))


        elif 'play video from pc' in query or "video" in query:
            speak("ok i am playing videos")
            video_dir = "D:\\Movie\\X-MEN"
            videos = os.listdir(video_dir)
            n = len(videos)
            index = random.randint(0,n)
            os.startfile(os.path.join(video_dir,videos[index]))


        elif 'open code' in query:
            codePath = "C:\\Users\\ANKIT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'Dev' in query:
            codePath = "C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
            os.startfile(codePath)

        elif 'python' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.3\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'open calculator' in query:
            subprocess.call('calc.exe')

        elif 'open notepad' in query:
            subprocess.call('notepad.exe')

        elif 'open' in query:
            os.system('explorer C://{}'.format(query.replace('Open','')))


        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                speak('I don\'t know Sir! Google is smarter than me!')
                webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!')