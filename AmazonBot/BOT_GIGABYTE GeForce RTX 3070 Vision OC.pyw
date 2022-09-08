from selenium import webdriver
from playsound import playsound
from pynput.keyboard import  Key, Controller
from datetime import datetime
import pyperclip
import pyautogui
import time
import os

#define Amazon Link
link = "https://www.amazon.com/dp/B08M13DXSZ";

#define product name
name = "GIGABYTE GeForce RTX 3070 Vision OC"

now = datetime.now()
log = open('Log.txt', 'a')

driver = webdriver.Chrome("chromedriver.exe")
keep_going = True;
addtocart = False;
captcha = False;
keyboard = Controller()
driver.get(link)

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
            pyperclip.copy(link);
            keep_going = False;

        else:
            driver.refresh()
    elif captcha:
        playsound('Sounds/error.mp3')
        time.sleep(3)

    try:
        captcha = driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/form/div[2]/div/span/span/button');
    except:
        captcha = False;

    time.sleep(1)

os.startfile("chrome.exe")
time.sleep(1)
#presses the key
keyboard.press(Key.ctrl)
keyboard.press('v')
keyboard.release(Key.ctrl)
keyboard.release('v')

keyboard.press(Key.enter)
keyboard.release(Key.enter)

#check if buy button exists
buy = pyautogui.locateCenterOnScreen('safe/BuyNow.PNG')

while str(buy) == "None":
    buy = pyautogui.locateCenterOnScreen('safe/BuyNow.PNG')

#click buy now button
pyautogui.click(buy)

#check if order is ready
placeorder = pyautogui.locateCenterOnScreen('safe/PlaceOrder.PNG')

while str(placeorder) == "None":
    placeorder = pyautogui.locateCenterOnScreen('safe/PlaceOrder.PNG')
    if str(pyautogui.locateCenterOnScreen('safe/PlaceOrder2.PNG')) != "None":
        placeorder = pyautogui.locateCenterOnScreen('safe/PlaceOrder2.PNG')

pyautogui.click(placeorder)
#pyautogui.moveTo(placeorder)

playsound('Sounds/alarm.mp3')

current_time = now.strftime("%c")
log.write(name + " drop on " + current_time + "\n")
log.close()

