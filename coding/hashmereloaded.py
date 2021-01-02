#!/usr/bin/env python3

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import hashlib
import getpass
import codecs

url = "https://ringzer0ctf.com/challenges/14/"

un = input("user: ")
pw = getpass.getpass("password: ")
driver = webdriver.Firefox()
driver.get(url)

username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
username.send_keys(un)
password.send_keys(pw + Keys.ENTER)
time.sleep(1)

s = driver.find_element_by_class_name("message").text
e = s[s.find('\n')+1:s.rfind('\n')].strip()
e = int(e, 2)
# "'%x' %" turns dec to hex w/o leading 0x, convert to corresponding ascii chars, and UTF-8 encoding :)
# can also use binascii.unhexlify
e = codecs.decode('%x' % e, "hex")
h = hashlib.sha512(e).hexdigest()
new_url = url + h
driver.get(new_url)
