#!/usr/bin/env python3

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import hashlib
import getpass

url = "https://ringzer0ctf.com/challenges/13/"

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
h = hashlib.sha512(e.encode("utf-8"))
new_url = h.hexdigest()
driver.get(url + new_url)
