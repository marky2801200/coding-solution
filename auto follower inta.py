from splinter import Browser
import time
br=Browser('chrome')
br.visit('https://www.instagram.com/')
username='kuma_r2801'
password='import__cv2'
br.find_by_name('username').fill(username)
br.find_by_name('password').fill(password)
br.find_by_text('Log In').click()
time.sleep(3)
br.find_by_text('Not Now').click()
try:
    br.find_by_text('Not Now').click()
except:
    pass
#br.execute_script("window.scrollTo(2000, document.body.scrollHeight);")
br.find_by_text('See All').click()
time.sleep(1)
while(1):
    try:
        bot=br.find_by_text('Follow')
        for i in range(0,len(bot)):
            br.find_by_text('Follow')[i].click()
        #br.find_by_class('sqdOP  L3NKy   y3zKF     ').click()
    except:
        br.reload()
