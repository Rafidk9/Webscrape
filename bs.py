import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

chrome_profile_path = 'C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\User Data\\Default'
chrome_options = Options()
chrome_options.add_argument(f'--user-data-dir={chrome_profile_path}')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

clst = []
all = []
for i in range(1):
    page = driver.get(f'https://www.daraz.com.bd/wireless-earbuds/?spm=a2a0e.searchlistcategory.card.1.6a823e31yqsrqf&item_id=327961640&from=onesearch_category_148')
    time.sleep(6)

    names = driver.find_elements(By.CLASS_NAME, "description--H8JN9")
    for name in names:
        # title = titles.append(name.text.split('\n')[0])
        data = [x for x in name.text.split('\n') if x.startswith("Free") == False]

        for d in data:
            if d.endswith('Off') or d.endswith('Vouchers'):
                data.remove(d)

        if len(data) == 6:
            clst.append(data)
            for n,r,nr,s,cp,op in clst:
                raw_dict = {
                    'Name': n,
                    'Rating': r,
                    'Number of Raters': nr,
                    'Sold': s,
                    'Current Price': cp,
                    'Original Price': op,
                }
                all.append(raw_dict)


        # clst.append(data)
         

# print(clst)
            

df = pd.DataFrame(all)
df.to_csv('daraz.csv',index=False)
print(df)