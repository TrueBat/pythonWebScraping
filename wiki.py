from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


search = input("type something to wiki... ")

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.wikipedia.org/")

searchInput = driver.find_element_by_id("searchInput")
searchInput.send_keys(search)
searchInput.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "bodyContent"))
    )
    print(main.text)

finally:
    driver.quit()
