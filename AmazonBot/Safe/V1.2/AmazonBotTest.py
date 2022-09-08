from selenium import webdriver
from playsound import playsound
from pynput.keyboard import  Key, Controller
import pyperclip
import time

##3060ti "https://www.amazon.com/ASUS-Premium-GeForce-Keyboard-Included/dp/B083Z5P6TX/ref=cm_cr_arp_d_product_top?ie=UTF8"
####3070 "https://www.amazon.com/ASUS-GeForce-Graphics-DisplayPort-Bearings/dp/B08L8KC1J7/ref=cm_cr_arp_d_product_top?ie=UTF8"
###alarm r'C:\Users\kelly\OneDrive\Documents\alarm.wav'

driver = webdriver.Chrome("chromedriver.exe")
keep_going = True;
addtocart = False;
captcha = False;
keyboard = Controller()
driver.get("https://www.amazon.com/Oculus-Quest-Head-Strap-Replacement/dp/B08QZ42DBS?ref_=Oct_s9_apbd_obs_hd_bw_bxip&pf_rd_r=3Z24TNDSA07T7MQSC3YT&pf_rd_p=3e7da7f7-27c1-5f1e-b4ac-f3953c4aec9e&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=229575")
driver.execute_script("window.stop();")
