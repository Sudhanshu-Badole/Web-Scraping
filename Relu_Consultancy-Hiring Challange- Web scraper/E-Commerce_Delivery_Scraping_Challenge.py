

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

import csv

# Set up the Chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())

row = 'https://shopee.sg/-Sale!-DW5600-High-Quality-WaterProof-Digital-Watch-560A-i.228561211.15888274757?sp_atk=6c5f17f1-2160-4384-b42d-06cf3cee7b70&xptdk=6c5f17f1-2160-4384-b42d-06cf3cee7b70'

driver.get(row)

try:
    elements = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='shopee-drawer__contents']")))
except TimeoutException:
    pass

for el in elements:       
    ActionChains(driver).move_to_element(el).perform()

    try:
        mouseover = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='tsEATN card']")))
    except TimeoutException:
        continue

    for m in mouseover:
        ActionChains(driver).move_to_element(m).perform() 

    try:
        do = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='AAaUS1']")))
        opt_comma="" # no comma on first print
        for d in do:
            print(opt_comma,d.text,sep="",end="")
            opt_comma="," # use comma for prints after the first one
        print()  #for new line
            
    except TimeoutException:
        continue


# Close the driver 
driver.quit() 
