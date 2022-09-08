from selenium import webdriver
from playsound import playsound
from pynput.keyboard import  Key, Controller
from datetime import datetime
import pyperclip
import time

##3060ti "https://www.amazon.com/ASUS-Premium-GeForce-Keyboard-Included/dp/B083Z5P6TX/ref=cm_cr_arp_d_product_top?ie=UTF8"
####3070 "https://www.amazon.com/ASUS-GeForce-Graphics-DisplayPort-Bearings/dp/B08L8KC1J7/ref=cm_cr_arp_d_product_top?ie=UTF8"
###alarm r'C:\Users\kelly\OneDrive\Documents\alarm.wav'

now = datetime.now()
log = open('Log.txt', 'a')

driver = webdriver.Chrome("chromedriver.exe")
keep_going = True;
addtocart = False;
captcha = False;
keyboard = Controller()
driver.get("https://www.amazon.com/ASUS-Premium-GeForce-Keyboard-Included/dp/B083Z5P6TX/ref=cm_cr_arp_d_product_top?ie=UTF8")

while keep_going:
    
    if not captcha:
        try:
            captcha = driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/form/div[2]/div/span/span/button');
        except:
            captcha = False;
        
        try:
            addtocart = driver.find_element_by_xpath('//*[@id="add-to-cart-button"]') or driver.find_element_by_xpath('//*[@id="buybox-see-all-buying-choices"]/span/a');
        except:
            addtocart = False;

        if addtocart:
            pyperclip.copy("https://www.amazon.com/ASUS-Premium-GeForce-Keyboard-Included/dp/B083Z5P6TX/ref=cm_cr_arp_d_product_top?ie=UTF8");
            keep_going = False;

        else:
            driver.refresh()
    elif captcha:
        playsound('error.mp3')
        time.sleep(3)

    try:
        captcha = driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/form/div[2]/div/span/span/button');
    except:
        captcha = False;

    time.sleep(1)
    
#presses the key
keyboard.press(Key.ctrl)
keyboard.press('v')
keyboard.release(Key.ctrl)
keyboard.release('v')

keyboard.press(Key.enter)
keyboard.release(Key.enter)

playsound('alarm.mp3')

current_time = now.strftime("%c")
log.write("RTX3060ti TUF drop on " + current_time + "\n")
log.close()

