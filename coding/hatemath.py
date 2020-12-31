#!/usr/bin/env python3

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import getpass

url = "https://ringzer0ctf.com/challenges/32/"

un = input("user: ")
pw = getpass.getpass("password: ")
driver = webdriver.Firefox()
driver.get(url)

username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
username.send_keys(un)
password.send_keys(pw + Keys.ENTER)
time.sleep(1)
s = driver.find_element_by_class_name("message")
e = s.text
e = e[e.find('\n')+1:e.rfind('\n')]
hx = e.split("+")[1].split("-")[0].split("x")[1]
bn = e.split("+")[1].split("-")[1].split("=")[0]
dc = e.split("+")[0]
bruh = int(dc) + int(hx, 16) - int(bn, 2)
print(bruh)
driver.get(url + str(bruh))
