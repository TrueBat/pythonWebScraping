from selenium import webdriver
search = input("type something to google... ")
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://google.com/search?q=" + search)
