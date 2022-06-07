from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


search = input("type something to monkey... ")

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://libraryofbabel.info/search.cgi")

find = driver.find_element_by_id("find")
find.send_keys(search)
find.send_keys(Keys.RETURN)
