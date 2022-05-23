import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib







engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour =int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("good morning")
        
    elif hour>=12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")

    speak("hii shagun  whats up")


def takecommand():
# it takes micro phone input form the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("lisening....")
        r.pause_threshold = 1 #pause threshold seconds of non speaking audio before a phase is considered complete
        audio = r.listen(source)

    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        print(e)
        print ("say that again please....")
        return"none"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gamil.com",587)
    server.ehlo()
    server.starttls()
    server.login('shagunpandit8988@gamil.com','8988357690')
    server.sendEmail('shagunpandit8988@gmail.com',to , content)
    server.close()



if __name__ == "__main__":
    wishme()
    
    while True:
        query = takecommand().lower()# lower case is helping to keep up with queery /or to match with it

# logic for excuting task based on query
        
        if 'wikipedia' in query:
            speak('serarching wikipedia....')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak (results)
        
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dr = 'E:\\music'
            songs = os.listdir(music_dr)            
            print(songs)
            os.startfile(os.path.join(music_dr, songs[23]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")             

        elif 'open code' in query:
            codepath = "C:\\Users\\asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif 'email to shagun' in query:
            try:
                speak ('what should i say')
                content = takecommand()
                to = "shagunpandit8988@gmail.com"
                sendEmail(to, content)
            
            except Exception as e:
                print (e)
                speak("sorry shagun , i am not able to send mail")
        elif 'quit' in query:
            quit()



