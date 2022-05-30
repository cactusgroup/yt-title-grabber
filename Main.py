# -*- coding: utf-8 -*-
"""
Created on Fri May 27 17:22:03 2022

@author: Server
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

import time

DRIVER_PATH = "./chromedriver"
s = Service(DRIVER_PATH)
driver = webdriver.Chrome(service=s)
driver.get('https://www.youtube.com/c/Freecodecamp/videos')

SCROLL_PAUSE_TIME = 3

# Get scroll height
last_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    
video_titles = driver.find_elements(By.ID, "video-title")

for e in video_titles:
    print(e.text)