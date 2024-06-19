from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
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

time.sleep(2)
#navigasi ke menu ui mode
ui_button = driver.find_element(By.CLASS_NAME, "nav-action.ui-mode")
ui_button.click()

time.sleep(2)
driver.quit()