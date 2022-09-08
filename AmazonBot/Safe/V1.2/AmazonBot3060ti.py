from selenium import webdriver
from playsound import playsound
import pyperclip
import time

##3060ti "https://www.amazon.com/ASUS-Premium-GeForce-Keyboard-Included/dp/B083Z5P6TX/ref=cm_cr_arp_d_product_top?ie=UTF8"
####3070 "https://www.amazon.com/ASUS-GeForce-Graphics-DisplayPort-Bearings/dp/B08L8KC1J7/ref=cm_cr_arp_d_product_top?ie=UTF8"
###alarm r'C:\Users\kelly\OneDrive\Documents\alarm.wav'

driver = webdriver.Chrome(r"C:\Users\Mining Rig\Downloads\AmazonBots\chromedriver.exe")
keep_going = True;
addtocart = False;
captcha = False;
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
            playsound(r'C:\Users\Mining Rig\Downloads\AmazonBots\alarm.mp3')
            keep_going = False;

        else:
            driver.refresh()
    elif captcha:
        playsound(r'C:\Users\Mining Rig\Downloads\AmazonBots\error.mp3')
        time.sleep(3)

    try:
        captcha = driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/form/div[2]/div/span/span/button');
    except:
        captcha = False;

    time.sleep(1)
