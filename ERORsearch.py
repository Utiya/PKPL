from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

service = Service(executeable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/")

#login berhasil
username_input = driver.find_element(By.CLASS_NAME, "cc-input-component.cc-input-group-space-prepend")
username_input.send_keys("raihan14032004@gmail.com")
password_input = driver.find_element(By.CLASS_NAME, "cc-input-component.cc-input-group-space-prepend.cc-input-group-space-append")
password_input.send_keys("ASUSTUFGAMINGFX506")
login_button = driver.find_element(By.ID, "login")
login_button.click()

time.sleep(5)
#navigasi ke search input
#search_input = driver.find_element(By.CLASS_NAME, "ui_v5-input-component.ui_v5-input-dark.ui_v5-input-group-space-right")
search_input = driver.find_element(By.NAME, 'keyword')

search_input.send_keys("Video")
search_input.send_keys(Keys.RETURN)

driver.quit()