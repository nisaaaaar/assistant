from gtts import gTTS
import os
import datetime


x=str(datetime.datetime.now())
a=x.split(" ")
a=a[1].split(":")
t=float(a[0])+float(a[1])*.01

print(t)
msg=""
if(t>6.00 and t<=10.00):
    msg="Studying"
if(t>10.00 and t<=17.00):
    msg="College"
if(t>17.00 and t<=18.00):
    msg="Resting"
if(t>18.00 and t<=20.00):
    msg="Studying"
if(t>20.00 and t<=23.00):
    msg="Eating"
if(t>23.00 and t<=0.00):
    msg="Studying"
if(t>0.00 and t<=6.00):
    msg="Sleeping"

msg1="The time is "+str(a[0])+str(a[1])+" and "+"You must be "+msg

tts = gTTS(text=msg1, lang='en')
tts.save("hello.mp3")
os.system("rhythmbox hello.mp3")

