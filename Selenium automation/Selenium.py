"""
Selenium is a powerful tool for controlling web browsers through programs and 
performing browser automation.

It is functional for all browsers, works on all major OS and its scripts are 
written in various languages i.e Python, Java, C#, etc
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

path = "C:/Sudhanshu/Study Material/Selenium/chromedriver.exe"
s = Service(path)
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com/")

box = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
box.send_keys("House of Dragon")
box.send_keys(Keys.ENTER)

driver.find_element_by_xpath("""//*[@id="kp-wp-tab-overview"]/div[3]/div/div/div/div/div/div[1]/div[1]/a""").click()
time.sleep(2)
driver.save_screenshot("C:/Sudhanshu/Study Material/Projects/Web Scraping/mini project of house of dragon/HOD.png")

driver.close()
