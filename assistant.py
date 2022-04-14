import sys
import math as m
from sqlite3 import Date
from time import sleep
import speech_recognition as sr
import pyttsx3
import pywhatkit
import requests
from bs4 import BeautifulSoup
from pywikihow import search_wikihow 
import datetime
import wikipedia
import pyjokes
import os
from PyDictionary import PyDictionary as diction
import pyautogui
import webbrowser
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from AssistantUI import Ui_mainWindow


engine = pyttsx3.init()
voices = engine.getProperty('voices')
#print (voices)
engine.setProperty('rate' , 145)
engine.setProperty('voice', voices[0].id)


def talk(text):
    
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        time = datetime.datetime.now().strftime('%I:%M %p')
        date = Date.today()
        talk("Good morning!")
        talk(f"the date is {date}")
        talk('Current time is ' + time)

    elif hour>=12 and hour<18:
        time = datetime.datetime.now().strftime('%I:%M %p')
        date = Date.today()
        talk("Good Afternoon!") 
        talk(f"the date is {date}")
        talk('Current time is ' + time)  

    else:
        time = datetime.datetime.now().strftime('%I:%M %p')
        date = Date.today()
        talk("Good Evening!")
        talk(f"the date is {date}") 
        talk('Current time is ' + time) 

    talk("I am friday Sir.")
    talk("just wait a second, system checking is in process....")
    sleep(5)
    talk("okay , system checking is done")
    talk("now, i am collecting data from the internet")
    sleep(2)
    talk("okay , collecting data is done")
    talk("sir, i am in process ")
    sleep(2)
    talk("okay sir, everything is done")
    talk("now i am ready and online")
    talk("please tell me how may i assist you!!!")

def tempreature(self):
    search = self.take_command()
    url = f"https://www.google.com/search?q={search}"
    r= requests.get(url)
    data = BeautifulSoup(r.text , "html.parser")
    temp = data.find("div", class_ = "BNeawe").text
    print(f"the tempreature is {temp}")
    talk(f"the tempreature is {temp}")

def music(self):
    talk('okk tell me the name of the song!')
    musicName= self.take_command()

    if 'allah waariyan' in musicName:
        music_dir = 'E:\\'
        songs = os.listdir(music_dir)
        print(songs)    
        os.startfile(os.path.join(music_dir, songs[4]))
    elif 'i love you' in musicName:
        music_dir = 'E:\\'
        songs = os.listdir(music_dir)
        print(songs)    
        os.startfile(os.path.join(music_dir, songs[5]))
    
    else:
        pywhatkit.playonyt(musicName)

    talk('your song has been started, enjoy sir!!')    

def Send_Whatsapp_msg(self):
    talk("tell me the name of the person!")
    name = self.take_command()

    if 'maya' in name:
        talk("tell me the message")
        msg = self.take_command()
        talk("tell me the time")
        talk("time in hours")
        hour= int(self.take_command())
        talk("time in minutes")
        min= int(self.take_command())
        pywhatkit.sendwhatmsg("+916289572884",msg,hour,min,30)
        talk("ok sir!, sending whatsapp message !")
    
    elif 'pallav' in name:
        talk("tell me the message")
        msg = self.take_command()
        talk("tell me the time")
        talk("time in hours")
        hour= int(self.take_command())
        talk("time in minutes")
        min= int(self.take_command())
        pywhatkit.sendwhatmsg("+917549687383",msg,hour,min,30)
        talk("ok sir!, sending whatsapp message !")
    
    elif 'vivek' in name:
        talk("tell me the message")
        msg = self.take_command()
        talk("tell me the time")
        talk("time in hours")
        hour= int(self.take_command())
        talk("time in minutes")
        min= int(self.take_command())
        pywhatkit.sendwhatmsg("+917439895273",msg,hour,min,30)
        talk("ok sir!, sending whatsapp message !")
    
    elif 'sanjiv' in name:
        talk("tell me the message")
        msg = self.take_command()
        talk("tell me the time")
        talk("time in hours")
        hour= int(self.take_command())
        talk("time in minutes")
        min= int(self.take_command())
        pywhatkit.sendwhatmsg("+919123809896",msg,hour,min,30)
        talk("ok sir!, sending whatsapp message !")
    
    elif 'rajiv' in name:
        talk("tell me the message")
        msg = self.take_command()
        talk("tell me the time")
        talk("time in hours")
        hour= int(self.take_command())
        talk("time in minutes")
        min= int(self.take_command())
        pywhatkit.sendwhatmsg("+916289594846",msg,hour,min,30)
        talk("ok sir!, sending whatsapp message !")
    else:
        talk("it is a unknown number")
        talk("tell me the phone number")
        phone= (f"{self.take_command()}")
        ph = '+91' + phone
        talk("tell me the message")
        msg = self.take_command()
        talk("tell me the time")
        talk("time in hours")
        hour= int(self.take_command())
        talk("time in minutes")
        min= int(self.take_command())
        pywhatkit.sendwhatmsg(ph,msg,hour,min,30)
        talk("ok sir!, sending whatsapp message !")
    pyautogui.press('enter')

def dict(self):
    talk("activated dictionary!")
    talk("tell me the problem")
    prob = self.take_command()

    if 'meaning' in prob:
        talk("tell me the word")
        ans = self.take_command()
        ans= ans.replace("what is the", "")
        ans= ans.replace("friday", "")
        ans= ans.replace("of", "")
        ans= ans.replace("meaning of", "")
        result = diction.meaning(ans)
        print(result)
        talk(f"the meaning of {ans} is {result}")

    elif 'synonym' in prob:
        talk("tell me the word")
        ans2 = self.take_command()
        ans2= ans2.replace("what is the", "")
        ans2= ans2.replace("friday", "")
        ans2= ans2.replace("of", "")
        ans2= ans2.replace("synonym of", "")
        result = diction.meaning(ans2)
        print(result)
        talk(f"the synonym of {ans2} is {result}")    

    elif 'antonym' in prob:
        talk("tell me the word")
        ans3 = self.take_command()
        ans3= ans3.replace("what is the", "")
        ans3= ans3.replace("friday", "")
        ans3= ans3.replace("of", "")
        ans3= ans3.replace("antonym of", "")
        result = diction.meaning(ans3)
        print(result)
        talk(f"the antonym of {ans3} is {result}")    
    
    else:
        talk("i find some error in word!!")

    talk("exited dictionary!")

def My_Location(self):
    ip_add = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
    geo_q = requests.get(url)
    geo_d = geo_q.json()
    city = geo_d['city']
    country = geo_d['country']

    print(f"sir, you are now in {city , country}")
    talk(f"sir, you are now in {city , country}")

def makaut(self):
    talk("opening...")
    talk("ok, i can see three main portals")
    talk("number 1: Members Area")
    talk("number 2: Letters & Notices")
    talk("number 3: Application & Notice")
    talk("tell me which one you want to open")

    do = self.take_command()

    if '1' in do:
        webbrowser.open('https://makaut1.ucanapply.com/smartexam/public/')
    elif '2' in do:
        webbrowser.open('http://makautexam.net/announcement.html')    
    elif '3' in do:
        webbrowser.open('http://makautexam.net/application-notice.html')    
    else:
        talk("nothing...")

def socialmedia(self):
    talk("wait a second sir")
    talk("okay tell me which social media handle you want to check. ")
    name = self.take_command()

    if 'instagram' in name:
        webbrowser.open('https://www.instagram.com/')
        talk("launched!")
    elif 'facebook' in name:
        webbrowser.open("https://www.facebook.com/")
        talk('launched!')                   
    elif 'google chrome' in name:
        os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        talk("launched!")
    elif 'whatsapp' in name:
        webbrowser.open('https://web.whatsapp.com/')
        talk("launched!")
    elif 'open spotify' in name:
        webbrowser.open('https://open.spotify.com/')
        talk("launched!")
    elif 'gaana' in name:
        webbrowser.open('https://gaana.com/playlist/sr-ynghx-musicgana')
        talk("launched!!")
    elif 'amazon' in name:
        webbrowser.open('https://www.amazon.com/')
        talk("launched!!")
    elif 'flipkart' in name:
        webbrowser.open('https://www.flipkart.com/') 
        talk("launched!!")   
    elif 'myntra' in name:
        webbrowser.open('https://www.myntra.com/shop/men')
        talk("launched!!")
    else:
        talk("not found ")    

def Random_talk(self):
    talk("Activated random talks!!")
    while True: 
        random = self.take_command()

        if 'let us go to date' in random:
            talk('sorry, I have a headache')
            print('fiday ans: sorry, I have a headache')
        elif 'hi' in random:
            talk("hello sir!!, how are you?")
        elif 'dating' in random:
            talk('no, mere sir mei dard hai...')
            print('friday ans: no, mere sir mei dard hai... ')
        elif 'who are you' in random:
            talk('I am friday. your assistant sir')
            print('friday ans: i am friday. your assistant sir')   
        elif 'kaun' in random:
            talk('mera naam friday hai, aur mai ek virtual assistant hu')
            print('friday ans: mera naam friday hai, aur mai ek virtual assistant hu')
        elif 'are you human' in random:
            talk('No I am a virtual assistant but i can talk like a person ')
            print('friday ans: No I am a virtual assistant but i can talk like a person')
        elif 'insan' in random:
            talk('nahi mai ek virtual assitant hu, lekin mai insano ki tarah baat kar sakti hu')
            print('friday ans: nahi mai ek virtual assitant hu, lekin mai insano ki tarah baat kar sakti hu')   
        elif 'goal' in random:
            talk('i do really to read everything ever written. with 2 million new web pages are created every day, i guess i will have plenty to look forward to')
            print('friday ans: i do really to read everything ever written. with 2 million new web pages are created every day, i guess i will have plenty to look forward to')    
        elif 'lakshya' in random:
            talk('sabko jaaankari pradaan karnaaa')
            print('friday ans: sabko jaaankari pradaan karnaaa') 
        elif 'invent' in random:
            talk('mr. vikash kumar prasad, he is very intelligent person')
            print('friday ans: mr. vikash kumar prasad, he is very intelligent person')
        elif 'banaya' in random:
            talk('mr. vikash kumar prasad, wo bahut budhimaan hai...')
            print('friday ans: mr. vikash kumar prasad, wo bahut budhimaan hai...')
        elif 'can i call you' in random:
            talk('i am not comfortable in call. talk me here...')
            print('friday ans: i am not comfortable in call. talk me here...')
        elif 'call' in random:
            talk('mujhe yaha baat karna pasand hai...')
            print('friday ans: mujhe yaha baat karna pasand hai...')
        elif 'can you laugh' in random:
            talk('hehehehehehehehehehehehehehehehehehehehehehehehehehehehehehehe')
        elif 'hasna' in random:
            talk('hehehehehehehehehehehehehehehehehehehehehehehehehehehehehehhehe')
        elif 'love' in random:
            talk('love is when you can never get enough of something, no matter how much time you spend with it. it is exactly how i feel about searching.')
            print('friday ans: love is when you can never get enough of something, no matter how much time you spend with it. it is exactly how i feel about searching.')
        elif 'pyar' in random:
            talk('pyar ek sundar ehsaas hai, jaise mujhe search karna pasand hai')
            print('friday ans: pyar ek sundar ehsaas hai, jaise mujhe search karna pasand hai')
        elif 'do you have any feelings' in random:
            talk('i have got lot of ways of communicating emotions. the shocked face emoji does a good job when words fail')
            print('friday ans: i have got lot of ways of communicating emotions. the shocked face emoji does a good job when words fail')
        elif 'feelings' in random:
            talk('nahi mai ek program hu. feelings jaisi koi bh chiz mere andar nahi hain')
            print('friday ans: nahi mai ek program hu. feelings jaisi koi bh chiz mere andar nahi hain')
        elif 'are you single' in random:
            talk('I am happy to say i feel whole all on my own. plus, i never have to share dessert')
            print('friday ans: I am happy to say i feel whole all on my own. plus, i never have to share dessert')
        elif 'single' in random:
            talk('ha aur mujhe akele rahna pasand hain')
            print('friday ans: ha aur mujhe akele rahna pasand hain') 
        elif 'exit' in random or 'close' in random:
            talk("exited random talk")
            break 
        else:
            talk("please say the command again!!")

def websites(self):
    talk("tell me the name of website which you want to open")
    webname = self.take_command()

    if 'google chrome' in webname:
        os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        talk("launched!!")
    elif 'geeksforgeeks' in webname:
        webbrowser.open("https://practice.geeksforgeeks.org/courses/dsa-self-paced?source=google&medium=cpc&device=c&keyword=geeksforgeeks&matchtype=b&campaignid=9546568041&adgroup=97966155295&gclid=Cj0KCQiA_c-OBhDFARIsAIFg3ew-Uxs4cnGUXCQvHE-XKRM4clCuIok5BhY6E8_-rzRj82Fw6fipmOQaAiUEEALw_wcB")
        talk('launched!')
    elif 'maps' in webname:
        webbrowser.open("https://www.google.com/maps/@21.125498,81.914063,5z")
        talk('launched!')
    elif 'stack overflow' in webname:
        webbrowser.open('https://stackoverflow.com/')
        talk("launched!!")
    elif 'javatpoint' in webname:
        webbrowser.open('https://www.javatpoint.com/') 
    else:
        talk("not found in web...")       

if __name__ == "__main__":

    class MainThread(QThread):
        def __init__(self):
            super(MainThread,self).__init__()

        def run(self):
            talk("this is a password protection system, please tell me the password")
            pwd= "i am vikas"
            tell= f"{self.take_command()}"
            #print(tell)
            if pwd==tell :
                talk("password successfully matched.... ")
                sleep(2)
                self.run_friday()
            else:
                talk("this is an incorrect password, please try again...")
                exit()

        def take_command(self):
                try:
                    listener = sr.Recognizer()
                    with sr.Microphone() as source:
                        print('Listening...')
                        print('Recognizing...')
                        listener.pause_threshold = 1
                        text = listener.listen(source)
                        command = listener.recognize_google(text, language= 'en-in')
                        command = command.lower()
                        if 'friday' in command:
                            command = command.replace('friday', '')
                            print(command)
                except:
                    pass
                return command



        def run_friday(self):

            wishMe()
            while True:
                self.command = self.take_command()
                print(self.command)

                if 'youtube' in self.command:
                    song = self.command.replace('play', '')
                    talk('playing ' + song)
                    pywhatkit.playonyt(song)

                elif 'time' in self.command:
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    print (time)
                    talk('Current time is ' + time)

                elif 'date' in self.command:
                    date = Date.today()
                    print(date)
                    talk(date)
                    
                elif 'call' in self.command or 'phone' in self.command:
                    from twilio.rest import Client

                    account_sid = 'AC09aecb16d60c902c589bea26c2d3138a'
                    auth_token = 'ef900510190da3402a6554507762d98d'
                    client = Client(account_sid , auth_token)

                    call = client.calls.create(
                                                twiml = '<Response><say> hello this is vikash</say></Response>',
                                                to = '+917549687383',
                                                from_ = '+17853775849' 
                                            )

                    print(call.sid)
                    talk("calling, just wait a second sir")
                
                elif 'wikipedia' in self.command:
                    talk("searching wikipedia...")
                    query = self.command.replace("friday", "")
                    query = self.command.replace("wikipedia", "")
                    wiki = wikipedia.summary(query, 2)
                    talk(f"according to wikipedia : {wiki}")

                elif 'search' in self.command:
                    talk("tell me what you want to search...")
                    import wikipedia as googleScrap
                    query = self.command.replace("search", " ")
                    talk('this is what i found in web...')
                    pywhatkit.search(query)

                    try:
                        result= googleScrap.summary(query,3)
                        talk(result)
                    
                    except:
                        talk('no data available in web...')    

                elif 'joke' in self.command:
                    joke = pyjokes.get_joke()
                    print(joke)
                    talk(joke)

                elif 'sleep'  in self.command:
                    talk('ok sir, you can call me anytime')
                    talk('just say wake up friday')
                    break

                elif 'temperature' in self.command:
                    tempreature(self)

                elif 'thank' in self.command:
                    talk('i am honoured to serve...') 

                elif 'music' in self.command:
                   music(self)
                
                elif 'whatsapp message' in self.command:
                    Send_Whatsapp_msg(self)

                elif 'screenshot' in self.command:
                    ss= pyautogui.screenshot()
                    ss.save("C:\\Users\\hp\Desktop\\My_assistant\\screenshot.png")
                    talk("done sir!!")

                elif 'vs code' in self.command:
                    os.startfile("C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

                elif 'dev' in self.command:
                    os.startfile("C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe")

                elif 'dictionary' in self.command:
                    dict(self)

                elif 'how to' in self.command:
                    talk("getting data from the internet, just wait a second sir!")
                    op = self.command.replace("friday", "")
                    max_res= 1
                    how_to_func= search_wikihow(op,max_res)
                    assert len(how_to_func) == 1
                    how_to_func[0].print()
                    talk(how_to_func[0].summary)
                    talk("done sir!")

                elif 'my current location' in self.command:
                    My_Location(self)

                elif 'social media' in self.command:
                    socialmedia(self)
                elif 'classroom' in self.command:
                    webbrowser.open('https://classroom.google.com/u/0/h')
                    talk("launching, wait a second sir!")

                elif 'makaut' in self.command:
                    makaut(self)

                elif 'random talk' in self.command:
                    Random_talk(self)
                
                elif 'website' in self.command:
                    websites(self)
                elif 'sqrt' in self.command:
                    talk('tell me the number')
                    num= self.take_command()
                    talk('the sqrt is')
                    res= m.sqrt(num)
                    talk(res)
                    print(res)
                else:
                    talk('please say the command again...') 

    startExecution = MainThread()
    class Main(QMainWindow):
        def __init__(self):
            super().__init__()
            self.ui = Ui_mainWindow()
            self.ui.setupUi(self)
            self.ui.pushButton.clicked.connect(self.StartTask)
            self.ui.pushButton_2.clicked.connect(self.close)
            

        def StartTask(self):
            self.ui.movie = QtGui.QMovie("../My_assistant/jarvis.gif")
            self.ui.label.setMovie(self.ui.movie)
            self.ui.movie.start()
            self.ui.movie = QtGui.QMovie("../My_assistant/init.gif")
            self.ui.label_2.setMovie(self.ui.movie)
            self.ui.movie.start()
            self.ui.movie = QtGui.QMovie("../My_assistant/cyber3.gif")
            self.ui.label_3.setMovie(self.ui.movie)
            self.ui.movie.start()
            timer = QTimer(self)
            timer.timeout.connect(self.showTime)
            timer.start(1000)
            startExecution.start()

        def showTime(self):
            current_time = QTime.currentTime()
            current_date = QDate.currentDate()
            label_time = current_time.toString('hh:mm:ss')
            label_date = current_date.toString(Qt.ISODate)
            self.ui.textBrowser.setText(label_date)
            self.ui.textBrowser_2.setText(label_time)

    app = QApplication(sys.argv)
    vikash_prasad = Main()
    vikash_prasad.show()
    exit(app.exec())

