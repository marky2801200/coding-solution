import playsound as p
import time

def play(hour,min,sec,e):
    d=hour*3600+min*60+sec
    d=d-e

    if(d%5==0):
        print(str(hour).zfill(2) + ":" + str(min).zfill(2) + ":" + str(sec).zfill(2))
        print("playing 15 min alaram")
        p.playsound('a.mp3')
    if(d%2==0):
        print("playing 45 min alaram")
        p.playsound('b.mp3')

    if(d%3==0):
        print("playing 90 min alaram")
        p.playsound('c.mp3')




def print_time():
    hour = 0
    min = 0
    sec = 1
    e = hour * 3600 + min * 60 + sec
    while(True):
        print(str(hour).zfill(2)+":"+str(min).zfill(2)+":"+str(sec).zfill(2))
        sec+=1
        if(sec==60):
            sec=0
            min+=1
        if(min==60):
            min=0
            hour+=1
        if(hour==24 and min==0 and sec==0):
            hour=0
        time.sleep(1)
    
        play(hour,min,sec,e)


print_time()