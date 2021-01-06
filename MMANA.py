import pyttsx3
import datetime
from tkinter import *
import tkinter
import random
import webbrowser
import psutil
import os
from turtle import *
import pywhatkit as kit
import wikipedia
import PyPDF2
from tkinter.filedialog import *
engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #changing index changes voices but ony 0 and 1 are working here
engine.runAndWait()
rate=engine.getProperty('rate')
engine.setProperty('rate',170)
def intro_screen():
    penup()
    bgcolor("black")
    color("blue")
    pensize(10)
    setx(-180)
    sety(0)
    pendown()
    left(90)
    forward(90)
    right(150)
    forward(45)
    left(120)
    forward(45)
    right(150)
    forward(90)
    left(90)
    penup()
    forward(30)
    pendown()
    left(90)
    forward(90)
    right(150)
    forward(45)
    left(120)
    forward(45)
    right(150)
    forward(90)
    left(90)
    penup()
    forward(30)
    pendown()
    left(75)
    forward(95)
    right(150)
    forward(95)
    left(75)
    penup()
    forward(30)
    left(90)
    pendown()
    forward(90)
    right(150)
    forward(100.62)
    right(30)
    right(180)
    forward(90)
    backward(90)
    right(90)
    penup()
    forward(30)
    pendown()
    left(75)
    forward(95)
    right(150)
    forward(95)
    left(75)
    penup()
    forward(30)
    pendown()
    penup()
    right(140)
    forward(500)
    right(90)
    forward(100)
    backward(50)
    left(180)
    pendown()
    pensize(20)
    speed(5)
    circle(300)
    penup()
    setx(-150)
    sety(-270)
    write("Made by Criminal!",True,font=("Algerian",32,"bold"))
    exitonclick()
    for i in range(100):
        print()
    bye()



def speak(audio):
      engine.say(audio)
      engine.runAndWait()
def Greetings():
     hr=int(datetime.datetime.now().hour)
     if(hr>=0 and hr<12):
         speak("Good Morning,sir!")
     elif(hr>=12 and hr<17):
         speak("Good Afternoon,sir!")
     else:
        speak("Good Evening,sir!")
intro_screen()
Greetings()
speak("SAGNIK at your service")
speak("Please wait for a few seconds. ")
speak("Importing Battery Status.....")
battery = psutil.sensors_battery()
plugged = battery.power_plugged
bts=battery.percent
if(bts<=15 and bts>5 and plugged==False):
    speak("Warning! LOW BATTERY! PLEASE PLUGIN")
elif(bts>=15 and plugged==True):
    speak("Charging.......")
elif(bts<=5 and plugged==False):
          speak('Not enough charge to host me')
          os.system('exit')
          window.destroy()
def window():
    global window
    window=Tk()
    input_user = StringVar()
    input_field = Entry(window, text=input_user)
    input_field.pack(side=BOTTOM, fill=X)
    
    def enter_pressed(event):
        input_get = input_field.get().lower()
        if input_get=="exit":
            speak("See You Later")
            window.destroy()
        elif input_get=="<develop>":
            window.destroy()
            login_gui()
        elif (input_get!="play music"or input_get!="play a song")and input_get.split()[0]=="play":
            window.destroy()
            MusicWindow(input_get)
        print(input_get)
        var = StringVar()
        label = Label( textvariable=var, relief=RAISED ,bg="white")
        var.set(response(input_get))
        'speak(response(input_get))'
        label.pack_propagate(True)
        label.pack()
        label.place(x=0,y=120)
        label = Label(frame, text=input_get,relief=RAISED,bg="pale green")
        input_user.set('')
        label.pack_propagate(True)
        label.pack()
        label.place(x=1390,y=0)
        return "break"

    frame = Frame(window, width=1600, height=600)
    frame.pack_propagate(True) # to resize frame according to the labels size
    input_field.bind("<Return>", enter_pressed)
    frame.pack()
    btn1 = Button(window, text ="Exit", command = window.destroy).pack()
    
    
    window.mainloop()
def MusicWindow(cmd):
    window = Tk()
    speak("Music Or Video")
    input_user = StringVar()
    input_field = Entry(window, text=input_user)
    input_field.pack(side=BOTTOM, fill=X)
    Label(text="Music Or Video").pack()
    
    def enter_pressed(event):
        
        
        input_get = input_field.get().lower()
        print(input_get)
        url=""
        if input_get=="music":
            var = StringVar()
            label = tkinter.Label( background="pale green",textvariable=var, relief=RAISED )
            var.set("Playing...")
            speak("Playing...")
            input_user.set('')
            label.pack()
            label.place(height=40, width=210,x=0,y=20)
            url="https://www.gaana.com/search/"+cmd[5:].replace(" ","%20")
            webbrowser.open(url)
        elif input_get=="video":
            var = StringVar()
            label = Message( background="pale green",textvariable=var, relief=RAISED )
            var.set("Playing...")
            speak("Playing...")
            input_user.set('')
            label.pack()
            label.place(height=40,width=210,x=0,y=20)
            url="https://www.youtube.com/results?search_query="+cmd[5:].replace(" ","+")
            webbrowser.open(url)
        label = tkinter.Label(frame, text=input_get,relief=RAISED)
        input_user.set('')
        label.pack()
        label.place(width=50,x=250,y=0)
        return "break"
    frame = Frame(window, width=300, height=300)
    frame.pack_propagate(False) # prevent frame to resize to the labels size
    input_field.bind("<Return>", enter_pressed)
    frame.pack()
    Button(window,text="Done",command=window.destroy).pack()
    
    
    
    window.mainloop()
       
def response(cmd):
    keyword=[]                          # Declare an empty list named mylines.
    with open ('Intents.txt', 'rt') as myfile: # Open intents.json for reading text data.
        for myline in myfile:                # For each line, stored as myline,
           keyword.append(myline)       # add its contents to mylines.
    questions=[]
    with open('Questions.txt',"rt")as myfile:
        for myline in myfile:
            questions.append(myline)
    response=[]
    with open ("Response.txt","rt")as myfile:
        for myline in myfile:
            response.append(myline)
    a=cmd.split()
    st=""
    greetings = ['hey there', 'hello', 'hi', 'hai', 'hey!', 'hey']
    gret=["good morning","good evening","good night","good afternoon"] 
    question = ['how are you', 'how are you doing']
    var1 = ['who made you', 'who created you']
    var2 = ['I_was_created_by_Soujash_right_in_his_computer.', 'Soujash', 'Some_guy_whom_i_never_got_to_know.']
    var4 = ['who are you', 'what is your name']
    cmd2 = ['play music', 'play songs', 'play a song', 'open music player']
    cmd3 = ['tell a joke', 'tell me a joke', 'say something funny', 'tell something funny']
    jokes = ['Can a kangaroo jump higher than a house?\n Of course,\n a house doesn’t jump at all.', 'My dog used to chase people on a bike a lot.\n It got so bad, finally I had to take his bike away.', "Why cant a aethist solve exponenetial problems?\n  Because he/she doesn't believe in higher power","what did the proton tell the electron?\n  don't be so negative.",'Reaching the end of a job interview,\n the Human Resources Officer asks a young engineer fresh out of the Massachusetts Institute of Technology,\n "And what starting salary are you looking for?"\n The engineer replies,\n "In the region of $125,000 a year, depending on the benefits package."\m The interviewer inquires,\n "Well, what would you say to a package of five weeks vacation,\n 14 paid holidays,\n full medical and dental,\n company matching retirement fund to 50% of salary,\n and a company car leased every two years,\n say, a red Corvette?"\n The engineer sits up straight and says,\n "Wow!\n Are you kidding?" \n The interviewer replies, \n"Yeah, but you started it.']
    cmd4 = ['open youtube', 'i want to watch a video']
    cmd5 = ['tell me the weather', 'weather', 'what about the weather','what is the weather today']
    cmd7 = ['what is your color', 'what is your colour', 'your color', 'your color?']
    colrep = ['Right now its rainbow', 'Right now its transparent', 'Right now its non chromatic']
    cmd8 = ['what is you favourite colour', 'what is your favourite color']
    cmd9 = ['thank you']
    repfr9 = ['you are welcome', 'glad i could help you']
    name1=["SAGNIK","Superficially Artificial Gaming Noob but Intelligent Kid"]
    appreciation=["you are great"," you are cool","you are the best","i love you"]
    fav=["play my favourite song"]
    siblings=["do you have any siblings","name your siblings"]
    age=["what is your age","how old are you"]
    stat=["battery status","check battery status"]
    default=["can you train","how is your memory","can you learn","can i train you"]
    command=["train"]
    religion=["do you believe in god","what is your religion","are you an aethist"]
    bday=["when was your birthday","when were you born","when is your bday","when was your bday","when is your birthday"]
    default=["I see","hmmmm","okay","ok","ha"]
    adbk=["read me a pdf","read me a file"]
    if cmd in greetings:
        return "Hey There,buddy!!"
    elif cmd in default:
        return "Hmmm"
    elif cmd in gret:
        hr=int(datetime.datetime.now().hour)
        a=""
        if(hr>=0 and hr<12):
            a="Good Morning"
        elif(hr>=12 and hr<17):
            a="Good Afternoon"
        else:
            a="Good Evening"
        if a.lower()==cmd:
            return a
        else:
            st="Actually sir you should be \n wishing "+a+"\n and not "+cmd+"."+"\n Neverthless "+a+" ,sir!" 
            return st
    
    elif cmd in adbk:
        Audiobook()
    elif "news" in a:
        webbrowser.open("news.google.com")
        return "opening news website(Could nnot search for specifics as news.google.com declined permission"
    elif(cmd=="Shutdown"or cmd=="shutdown"):
                speak("Are you sure,sir?(Please check the prompt)")
                window = Tk()

                input_user = StringVar()
                input_field = Entry(window, text=input_user)
                input_field.pack(side=BOTTOM, fill=X)
                Label(text="Are you sure sir?").pack()
                def enter_pressed(event):
                    
                    input_get = input_field.get()
                    print(input_get)
                    if input_get=="yes":
                        var = StringVar()
                        label = tkinter.Label( background="pale green",textvariable=var, relief=RAISED )
                        var.set("Shutting Down")
                        speak("Shutting Down")
                        os.system('shutdown /s /t 1')
                        input_user.set('')
                        label.pack()
                        label.place(height=40, width=210,x=0,y=20)
                    elif input_get=="no":
                        var = StringVar()
                        label = Message( background="pale green",textvariable=var, relief=RAISED )
                        var.set("Shut Down procedure aborted")
                        input_user.set('')
                        label.pack()
                        label.place(height=40,width=210,x=0,y=20)
                    label = tkinter.Label(frame, text=input_get,relief=RAISED)
                    input_user.set('')
                    label.pack()
                    label.place(width=50,x=250,y=0)
                    return "break"
                frame = Frame(window, width=300, height=300)
                frame.pack_propagate(False) # prevent frame to resize to the labels size
                input_field.bind("<Return>", enter_pressed)
                frame.pack()
                
                window.mainloop()
    elif(cmd=="Restart"or cmd=="restart"):
                window = Tk()
                speak("Are you sure sir?")
                input_user = StringVar()
                input_field = Entry(window, text=input_user)
                input_field.pack(side=BOTTOM, fill=X)
                Label(text="Are you sure sir?").pack()
                def enter_pressed(event):
                    input_get = input_field.get()
                    print(input_get)
                    if input_get=="yes":
                            var = StringVar()
                            label = tkinter.Label( background="pale green",textvariable=var, relief=RAISED )
                            var.set("Restarting")
                            speak("Restarting")
                            os.system('shutdown /r /t 1')
                            input_user.set('')
                            label.pack()
                            label.place(height=40, width=210,x=0,y=20)
                    elif input_get=="no":
                            var = StringVar()
                            label = Message( background="pale green",textvariable=var, relief=RAISED )
                            var.set("Restart procedure aborted")
                            input_user.set('')
                            label.pack()
                            label.place(height=40,width=210,x=0,y=20)
                    label = tkinter.Label(frame, text=input_get,relief=RAISED)
                    input_user.set('')
                    label.pack()
                    label.place(width=50,x=250,y=0)
                    return "break"
                frame = Frame(window, width=300, height=300)
                frame.pack_propagate(False) # prevent frame to resize to the labels size
                input_field.bind("<Return>", enter_pressed)
                frame.pack()
                
                window.mainloop()
    elif(cmd=="What is the time?"):
                hr=datetime.datetime.now()
                return(hr)
    elif cmd in age:
            yr=int(datetime.datetime.now().year)
            
            mo=int(datetime.datetime.now().month)
            
            da=int(datetime.datetime.now().day)
            ay=yr-2020
            ad=da-6
            am=mo-11
            if ad<0:
                if mo in [1,3,5,7,10,12]:
                    ad=31+da
                    am=am-1
                else:
                    ad=30+da
                    am=am-1
            st="I'm"+str(ay)+"years"+str(ad)+"months"+str(am)+"days old"
            return st
    elif cmd in bday:
            return "I was born on 17 th of August 2020"
    elif cmd in religion:
            return "I do believe in god.\n  Because just like I've been \n programmed to respond like this \n.So are you.\n Thus I do believe in god "
                
    elif cmd in command:
            Train()
    elif cmd in default:
            return "Yes you can train me.\n you can train me by typing th word 'Train()'"
    elif cmd in stat:
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = str(battery.percent)
            plugged = "Plugged In" if plugged else "Not Plugged In"
            return(percent+'% | '+plugged)
    elif cmd in siblings:
            return("Yes! I have a big brother,\n Robert, who is in Java.\n I also have an elder sister MMANA in Python")
    elif cmd in fav:
        webbrowser.open("https://gaana.com/song/lag-ja-gale-se-phir")        
        return("playing Lag Ja Gale...")
    elif cmd in greetings:
            random_greeting = random.choice(greetings)
            return(random_greeting)
    elif cmd in question:
            return("I am Fine,sir")
    elif cmd in  var1:
            reply='I was made by Soujash Banerjee all alone right in his laptop with some help from the internet'
            return(reply)
    elif cmd  in cmd9:
            return(random.choice(repfr9))
    elif cmd  in cmd7:
            return(random.choice(colrep)+'\n It keeps changing every micro second')
    elif cmd  in cmd8:
            color=random.choice(colrep)
            return(color)
    elif cmd in cmd2:
            webbrowser.open("https://gaana.com/playlist/gaana-dj-gaana-international-top-50")
            return("Playing one of my preferred music playlist")
    elif cmd  in var4:
            return(random.choice(name1))
    elif cmd  in cmd4:
            webbrowser.open('www.youtube.com')
            return "opening"
    elif cmd  in cmd5:
            webbrowser.open("https://www.bing.com/search?q=today%27s+weather+forecast&qs=SC&pq=today%27s+wae&sc=8-11&cvid=529AB3594F30416DB2A557F154BCB435&FORM=GEOTRI&sp=1&ghc=1&isRef=1&showTw=1")
            return "opening"
    elif cmd in cmd3:
            jokrep = random.choice(jokes)
            return(jokrep)

    elif cmd in appreciation:
            return("Thank You ! Sir .  I Like being appreciated!")
     
    else:
            c=False
            for i in range(0,len(questions)):
                if cmd+"\n" == questions[i]:
                    return(response[i//5])
                    c=True
                    break
                   
            
            
            if c==False:
                        err_msg=["Hmm...I don't have an answer to that","I'm not sure I understand"]
                        speak(random.choice(err_msg))
                        speak("I foud this on the web")
                        result= wikipedia.summary(cmd)
                        s=""
                        for i in result:
                            if i==".":
                                s=result.replace(".","\n")
                        return s
                    
                            

def Audiobook():

    
    def Accept():
            root.destroy()
            window=Tk()
            frame = Frame(window, width=300, height=80)
            frame.pack_propagate(False) # prevent frame to resize to the labels size
            frame.pack()
            Label(text="What type of file do you want me to read").pack()
            p_button=Button(window,text="PDF",command=pdf)
            p_button.pack()
            p_button.place(width=50,x=120,y=30)
            t_button=Button(window,text="TXT",command=txt)
            t_button.pack()
            t_button.place(width=50,x=120,y=60)
    def Decline():
            Label(text="Sorry could not access the contents of your computer").pack()
    def pdf():
        window=Tk()
        book = askopenfilename()
        reader= PyPDF2.PdfFileReader(book)
        pages = reader.numPages
        window.mainloop()
        for num in range(0,pages):
            page = reader.getPage(num)
            txt = page.extractText()
            speak(txt)
            print(txt)
        window.destroy()
    def txt():
        window=Tk()
        book = askopenfilename()
        file=open(book)
        speak(file.read())
        print(file.read())
        file.close()
        window.destroy()
        
    root=Tk()
    frame = Frame(root, width=300, height=80)
    frame.pack_propagate(False) # prevent frame to resize to the labels size
    label1=Label(text="SAGNIK would like to access the files on your computer")
    label1.pack()
    a_button=Button(root,text="Allow",command=Accept)
    a_button.pack()
    a_button.place(width=50,x=120,y=30)
    d_button=Button(root,text="Deny",command=Decline)
    d_button.pack()
    d_button.place(width=50,x=120,y=60)
    frame.pack()
    root.mainloop()
def Train():
        q=["","","","",""]
        file=open("intents.txt","a+")
        (speak("Enter recognizer tag"))
        tag=input("Enter recognizer tag").lower()
        tag=tag+"\n"
        file.write(tag)
        file.close()
        file=open("Questions.txt","a+")
        for i in range(0,len(q)):
            speak("Enter an avatar of the question")
            q[i]=input("Enter an avatar of the question").lower()
            q[i]=q[i]+"\n"
            file.write(q[i])    
        file.close()
        file=open("response.txt","a+")
        (speak("Interesting Questions What should I answer for this"))
        res=input("Interesting Questions .What should I answer for this?").lower()
        res=res+"\n"
        file.write(res)
        file.close()
        speak("Learning....")
        for i in range(1,10000000):
            if i==10000000:
                break
        speak("Learning complete")
            
def login_gui():
        
    # Designing window for registration
    
    def register():
        global register_screen
        register_screen = Toplevel(main_screen)
        register_screen.title("Register")
        register_screen.geometry("300x250")
    
        global username
        global password
        global username_entry
        global password_entry
        username = StringVar()
        password = StringVar()
    
        Label(register_screen, text="Please enter details below", bg="blue").pack()
        Label(register_screen, text="").pack()
        username_lable = Label(register_screen, text="Username * ")
        username_lable.pack()
        username_entry = Entry(register_screen, textvariable=username)
        username_entry.pack()
        password_lable = Label(register_screen, text="Password * ")
        password_lable.pack()
        password_entry = Entry(register_screen, textvariable=password, show='*')
        password_entry.pack()
        Label(register_screen, text="").pack()
        Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
    
    
    # Designing window for login 
    
    def login():
        global login_screen
        login_screen = Toplevel(main_screen)
        login_screen.title("Login")
        login_screen.geometry("300x250")
        Label(login_screen, text="Please enter details below to login").pack()
        Label(login_screen, text="").pack()
    
        global username_verify
        global password_verify
    
        username_verify = StringVar()
        password_verify = StringVar()
    
        global username_login_entry
        global password_login_entry
    
        Label(login_screen, text="Username * ").pack()
        username_login_entry = Entry(login_screen, textvariable=username_verify)
        username_login_entry.pack()
        Label(login_screen, text="").pack()
        Label(login_screen, text="Password * ").pack()
        password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
        password_login_entry.pack()
        Label(login_screen, text="").pack()
        Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
    
    # Implementing event on register button
    
    def register_user():
    
        username_info = username.get()
        password_info = password.get()
    
        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()
    
        username_entry.delete(0, END)
        password_entry.delete(0, END)
    
        Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    
    # Implementing event on login button 
    
    def login_verify():
        username1 = username_verify.get()
        password1 = password_verify.get()
        username_login_entry.delete(0, END)
        password_login_entry.delete(0, END)
    
        list_of_files = os.listdir()
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                login_sucess()
    
            else:
                password_not_recognised()
    
        else:
            user_not_found()
    
    # Designing popup for login success
    
    def login_sucess():
        global login_success_screen
        login_screen.destroy()
        main_screen.destroy()
        Develop()
    
    # Designing popup for login invalid password
    
    def password_not_recognised():
        global password_not_recog_screen
        password_not_recog_screen = Toplevel(login_screen)
        password_not_recog_screen.title("Success")
        password_not_recog_screen.geometry("150x100")
        Label(password_not_recog_screen, text="Invalid Password ").pack()
        Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
    
    # Designing popup for user not found
     
    def user_not_found():
        global user_not_found_screen
        user_not_found_screen = Toplevel(login_screen)
        user_not_found_screen.title("Success")
        user_not_found_screen.geometry("150x100")
        Label(user_not_found_screen, text="User Not Found").pack()
        Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
    
    # Deleting popups
    
    def delete_login_success():
        login_success_screen.destroy()
    
    
    def delete_password_not_recognised():
        password_not_recog_screen.destroy()
    
    
    def delete_user_not_found_screen():
        user_not_found_screen.destroy()
    
    
    # Designing Main(first) window
    
    def main_account_screen():
        global main_screen
        main_screen = Tk()
        main_screen.geometry("300x250")
        main_screen.title("Account Login")
        Label(text="DEVELOPER SCREEN",bg="red",width="300", height="2", font=("Calibri", 13)).pack()
        Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()
        Button(text="Login", height="2", width="30", command = login).pack()
        Label(text="").pack()
        Button(text="Register", height="2", width="30", command=register).pack()
    
        main_screen.mainloop()
    
    
    main_account_screen()
    
def Develop():
        print("If you are new type <kwshow> for viewing list of keywords")
        while(True):
            a=input(">>>")
            kw=["<showsrc>","<browse>","<modify>","<test>","<logout>","<version>","<name_style>","<kw_info>","<execute>"]
            kwerr=["showsrc","browse","modify","test","logout","version","name_style","kw_info","exeecute","kwshow"]
            if a=="<kwshow>":
                print(kw)
            elif a=="<showsrc>":
                pwd=input("Enter the Chat_code")
                if pwd=="25/07/2004":
                    file=open("Source.txt")
                    s=file.read()
                    print(s)
                else:
                    print("Wrong Chat_code")
                    break
            elif a=="<browse>":
                webbrowser.open("www.google.com")
            elif a=="<modify>":
                pwd=input("Enter the Chat_code")
                if pwd=="25/07/2004":
                    print("Please visit Spyder(Anaconda 3) for that purpose!")
                else:
                    print("Wrong Chat_code")
            elif a=="<test>":
                Greetings()
            elif a=="<logout>":
                break
            elif a=="<version>":
                print("v.4.3.2.3")
            elif a=="<name_style>":
                naam = input("Enter your name: \n\n")
                namer(naam)
            elif a=="<execute>":
                execute()
    

            elif a in kwerr:
                print("Oops! You missed '<>'! Try again! ")
                continue
            elif a =="return":
                Window()
                    
            else:
                exec(a)
def Window():
    global window
    window=Tk()
    input_user = StringVar()
    input_field = Entry(window, text=input_user)
    input_field.pack(side=BOTTOM, fill=X)
    
    def enter_pressed(event):
        input_get = input_field.get().lower()
        if input_get=="exit":
            speak("See You Later")
            window.destroy()
        elif input_get=="<develop>":
            window.destroy()
            login_gui()
        elif (input_get!="play music"or input_get!="play a song")and input_get.split()[0]=="play":
            window.destroy()
            MusicWindow(input_get)
        print(input_get)
        var = StringVar()
        label = Label( textvariable=var, relief=RAISED ,bg="white")
        var.set(response(input_get))
        speak(response(input_get))
        label.pack()
        label.place(height=100, width=210,x=0,y=120)
        label = Label(frame, text=input_get,relief=RAISED,bg="pale green")
        input_user.set('')
        label.pack()
        label.place(height=100,width=210,x=90,y=0)
        return "break"

    frame = Frame(window, width=300, height=300)
    frame.pack_propagate(False) # prevent frame to resize to the labels size
    input_field.bind("<Return>", enter_pressed)
    frame.pack()
    btn1 = Button(window, text ="Exit", command = window.destroy).pack()
    
    
    window.mainloop()
def execute():
        import tkinter as tk
        import sys
        import re
        from code import InteractiveConsole
        from contextlib import redirect_stderr, redirect_stdout
        from io import StringIO
        
        
        class History(list):
            def __getitem__(self, index):
                try:
                    return list.__getitem__(self, index)
                except IndexError:
                    return
        
        
        class TextConsole(tk.Text):
            def __init__(self, master, **kw):
                kw.setdefault('width', 50)
                kw.setdefault('wrap', 'word')
                kw.setdefault('prompt1', '>>> ')
                kw.setdefault('prompt2', '... ')
                banner = kw.pop('banner', 'Python %s\n' % sys.version)
                self._prompt1 = kw.pop('prompt1')
                self._prompt2 = kw.pop('prompt2')
                tk.Text.__init__(self, master, **kw)
                # --- history
                self.history = History()
                self._hist_item = 0
                self._hist_match = ''
        
                # --- initialization
                self._console = InteractiveConsole() # python console to execute commands
                self.insert('end', banner, 'banner')
                self.prompt()
                self.mark_set('input', 'insert')
                self.mark_gravity('input', 'left')
        
                # --- bindings
                self.bind('<Control-Return>', self.on_ctrl_return)
                self.bind('<Shift-Return>', self.on_shift_return)
                self.bind('<KeyPress>', self.on_key_press)
                self.bind('<KeyRelease>', self.on_key_release)
                self.bind('<Tab>', self.on_tab)
                self.bind('<Down>', self.on_down)
                self.bind('<Up>', self.on_up)
                self.bind('<Return>', self.on_return)
                self.bind('<BackSpace>', self.on_backspace)
                self.bind('<Control-c>', self.on_ctrl_c)
                self.bind('<<Paste>>', self.on_paste)
        
            def on_ctrl_c(self, event):
                """Copy selected code, removing prompts first"""
                sel = self.tag_ranges('sel')
                if sel:
                    txt = self.get('sel.first', 'sel.last').splitlines()
                    lines = []
                    for i, line in enumerate(txt):
                        if line.startswith(self._prompt1):
                            lines.append(line[len(self._prompt1):])
                        elif line.startswith(self._prompt2):
                            lines.append(line[len(self._prompt2):])
                        else:
                            lines.append(line)
                    self.clipboard_clear()
                    self.clipboard_append('\n'.join(lines))
                return 'break'
        
            def on_paste(self, event):
                """Paste commands"""
                if self.compare('insert', '<', 'input'):
                    return "break"
                sel = self.tag_ranges('sel')
                if sel:
                    self.delete('sel.first', 'sel.last')
                txt = self.clipboard_get()
                self.insert("insert", txt)
                self.insert_cmd(self.get("input", "end"))
                return 'break'
        
            def prompt(self, result=False):
                """Insert a prompt"""
                if result:
                    self.insert('end', self._prompt2, 'prompt')
                else:
                    self.insert('end', self._prompt1, 'prompt')
                self.mark_set('input', 'end-1c')
        
            def on_key_press(self, event):
                """Prevent text insertion in command history"""
                if self.compare('insert', '<', 'input') and event.keysym not in ['Left', 'Right']:
                    self._hist_item = len(self.history)
                    self.mark_set('insert', 'input lineend')
                    if not event.char.isalnum():
                        return 'break'
        
            def on_key_release(self, event):
                """Reset history scrolling"""
                if self.compare('insert', '<', 'input') and event.keysym not in ['Left', 'Right']:
                    self._hist_item = len(self.history)
                    return 'break'
        
            def on_up(self, event):
                """Handle up arrow key press"""
                if self.compare('insert', '<', 'input'):
                    self.mark_set('insert', 'end')
                    return 'break'
                elif self.index('input linestart') == self.index('insert linestart'):
                    # navigate history
                    line = self.get('input', 'insert')
                    self._hist_match = line
                    hist_item = self._hist_item
                    self._hist_item -= 1
                    item = self.history[self._hist_item]
                    while self._hist_item >= 0 and not item.startswith(line):
                        self._hist_item -= 1
                        item = self.history[self._hist_item]
                    if self._hist_item >= 0:
                        index = self.index('insert')
                        self.insert_cmd(item)
                        self.mark_set('insert', index)
                    else:
                        self._hist_item = hist_item
                    return 'break'
        
            def on_down(self, event):
                """Handle down arrow key press"""
                if self.compare('insert', '<', 'input'):
                    self.mark_set('insert', 'end')
                    return 'break'
                elif self.compare('insert lineend', '==', 'end-1c'):
                    # navigate history
                    line = self._hist_match
                    self._hist_item += 1
                    item = self.history[self._hist_item]
                    while item is not None and not item.startswith(line):
                        self._hist_item += 1
                        item = self.history[self._hist_item]
                    if item is not None:
                        self.insert_cmd(item)
                        self.mark_set('insert', 'input+%ic' % len(self._hist_match))
                    else:
                        self._hist_item = len(self.history)
                        self.delete('input', 'end')
                        self.insert('insert', line)
                    return 'break'
        
            def on_tab(self, event):
                """Handle tab key press"""
                if self.compare('insert', '<', 'input'):
                    self.mark_set('insert', 'input lineend')
                    return "break"
                # indent code
                sel = self.tag_ranges('sel')
                if sel:
                    start = str(self.index('sel.first'))
                    end = str(self.index('sel.last'))
                    start_line = int(start.split('.')[0])
                    end_line = int(end.split('.')[0]) + 1
                    for line in range(start_line, end_line):
                        self.insert('%i.0' % line, '    ')
                else:
                    txt = self.get('insert-1c')
                    if not txt.isalnum() and txt != '.':
                        self.insert('insert', '    ')
                return "break"
        
            def on_shift_return(self, event):
                """Handle Shift+Return key press"""
                if self.compare('insert', '<', 'input'):
                    self.mark_set('insert', 'input lineend')
                    return 'break'
                else: # execute commands
                    self.mark_set('insert', 'end')
                    self.insert('insert', '\n')
                    self.insert('insert', self._prompt2, 'prompt')
                    self.eval_current(True)
        
            def on_return(self, event=None):
                """Handle Return key press"""
                if self.compare('insert', '<', 'input'):
                    self.mark_set('insert', 'input lineend')
                    return 'break'
                else:
                    self.eval_current(True)
                    self.see('end')
                return 'break'
        
            def on_ctrl_return(self, event=None):
                """Handle Ctrl+Return key press"""
                self.insert('insert', '\n' + self._prompt2, 'prompt')
                return 'break'
        
            def on_backspace(self, event):
                """Handle delete key press"""
                if self.compare('insert', '<=', 'input'):
                    self.mark_set('insert', 'input lineend')
                    return 'break'
                sel = self.tag_ranges('sel')
                if sel:
                    self.delete('sel.first', 'sel.last')
                else:
                    linestart = self.get('insert linestart', 'insert')
                    if re.search(r'    $', linestart):
                        self.delete('insert-4c', 'insert')
                    else:
                        self.delete('insert-1c')
                return 'break'
        
            def insert_cmd(self, cmd):
                """Insert lines of code, adding prompts"""
                input_index = self.index('input')
                self.delete('input', 'end')
                lines = cmd.splitlines()
                if lines:
                    indent = len(re.search(r'^( )*', lines[0]).group())
                    self.insert('insert', lines[0][indent:])
                    for line in lines[1:]:
                        line = line[indent:]
                        self.insert('insert', '\n')
                        self.prompt(True)
                        self.insert('insert', line)
                        self.mark_set('input', input_index)
                self.see('end')
        
            def eval_current(self, auto_indent=False):
                """Evaluate code"""
                index = self.index('input')
                lines = self.get('input', 'insert lineend').splitlines() # commands to execute
                self.mark_set('insert', 'insert lineend')
                if lines:  # there is code to execute
                    # remove prompts
                    lines = [lines[0].rstrip()] + [line[len(self._prompt2):].rstrip() for line in lines[1:]]
                    for i, l in enumerate(lines):
                        if l.endswith('?'):
                            lines[i] = 'help(%s)' % l[:-1]
                    cmds = '\n'.join(lines)
                    self.insert('insert', '\n')
                    out = StringIO()  # command output
                    err = StringIO()  # command error traceback
                    with redirect_stderr(err):     # redirect error traceback to err
                        with redirect_stdout(out): # redirect command output
                            # execute commands in interactive console
                            res = self._console.push(cmds)
                            # if res is True, this is a partial command, e.g. 'def test():' and we need to wait for the rest of the code
                    errors = err.getvalue()
                    if errors:  # there were errors during the execution
                        self.insert('end', errors)  # display the traceback
                        self.mark_set('input', 'end')
                        self.see('end')
                        self.prompt() # insert new prompt
                    else:
                        output = out.getvalue()  # get output
                        if output:
                            self.insert('end', output, 'output')
                        self.mark_set('input', 'end')
                        self.see('end')
                        if not res and self.compare('insert linestart', '>', 'insert'):
                            self.insert('insert', '\n')
                        self.prompt(res)
                        if auto_indent and lines:
                            # insert indentation similar to previous lines
                            indent = re.search(r'^( )*', lines[-1]).group()
                            line = lines[-1].strip()
                            if line and line[-1] == ':':
                                indent = indent + '    '
                            self.insert('insert', indent)
                        self.see('end')
                        if res:
                            self.mark_set('input', index)
                            self._console.resetbuffer()  # clear buffer since the whole command will be retrieved from the text widget
                        elif lines:
                            self.history.append(lines)  # add commands to history
                            self._hist_item = len(self.history)
                    out.close()
                    err.close()
                else:
                    self.insert('insert', '\n')
                    self.prompt()
        
        
        if __name__ == '__main__':
            root = tk.Tk()
            root.title("Develop")
            console = TextConsole(root)
            console.pack(fill='both', expand=True)
            root.mainloop()
              

window()
