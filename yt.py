import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
yt = driver.get('https://www.youtube.com/@WesRoth/videos')

titles = (driver.find_elements(By.ID,'video-title'))

views = driver.find_elements(By.XPATH,'//*[@id="metadata-line"]/span[1]')

times = driver.find_elements(By.XPATH,'//*[@id="metadata-line"]/span[2]')

x = list(zip(titles,views,times))

lst = []

for title,view,time in x:
    a = {
        'title': title.text,
        'view': view.text,
        'time': time.text
    }
    lst.append(a)

df = pd.DataFrame(lst)
print(df)