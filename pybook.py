import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
from termcolor import cprint

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

names_lst = []
for i in range(3,18):
    driver.get("https://github.com/jackfrued/Python-100-Days/tree/master/Day01-15")
    time.sleep(5)
    names = driver.find_element(By.XPATH,f"//*[@id='folder-row-{i}']/td[2]/div/div/h3/div/a")
    
    names = names.text
    names_lst.append(names)
    print(names_lst)
    input_elems = driver.find_element(By.LINK_TEXT,f"{names}").click()
    time.sleep(10)
    driver.find_element(By.XPATH,'//*[@id="repos-sticky-header"]/div[1]/div[2]/div[2]/div[1]/div/button').click()
    time.sleep(3)

    # Get the text from the clipboard
    clipboard_text = pyperclip.paste()

    # Write the clipboard text to a file named "clipboard_output.txt"
    with open(f"chapter {i-2}.txt", "w",encoding="utf-8") as file:
        file.write(clipboard_text)

    cprint(f"The clipboard text has been written to clipboard_output.txt{i-2}.","green")

# driver.quit()