#!/usr/bin/env python3

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import hashlib
import getpass

url = "https://ringzer0ctf.com/challenges/56/"
url_2 = "https://hashes.com/en/decrypt/hash"
un = input("user: ")
pw = getpass.getpass("password: ") 
driver = webdriver.Firefox()
   
driver.get(url)
driver.execute_script("window.open('" + url_2 + "');")
driver.switch_to.window(driver.window_handles[0])                                                                 
driver.find_element_by_name("username").send_keys(un)
driver.find_element_by_name("password").send_keys(pw + Keys.ENTER)
time.sleep(1)                                                                                                     
s = driver.find_element_by_class_name("message").text
s = s.strip()[s.find('\n')+1:s.rfind('\n')]
driver.switch_to.window(driver.window_handles[1])                                                                 
driver.find_element_by_id("hashes").send_keys(s)
driver.find_element_by_xpath("//button[@type='submit' and @class='px-4 btn btn-primary']").click()                
decrypted_hash = driver.find_element_by_class_name("py-1").text                                                   
d = decrypted_hash.split(":")[1]                                                                                  
driver.switch_to.window(driver.window_handles[0])                                                                 
driver.get(url + d)
