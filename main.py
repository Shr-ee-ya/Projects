
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service


path = "D:\prog files\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=path)

driver = webdriver.Chrome(service=service)
driver.get("https://www.python.org")
assert "Python" in driver.title
#print(driver.title) #prints the webpage title

#to find and object tht gives tht search , usually first one
elem= driver.find_element(By.NAME,"q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)# for the enter key
assert "no result found." not in driver.page_source
time.sleep(5)
driver.close()