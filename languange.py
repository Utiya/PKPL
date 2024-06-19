from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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
#navigasi ke menu setting
settings_button = driver.find_element(By.CLASS_NAME, "toolbar-action.settings")
settings_button.click()
time.sleep(2)
#navigasi ke menu setting
settings_button = driver.find_element(By.CLASS_NAME, "toolbar-action.settings")
settings_button.click()

time.sleep(2)
#navigasi ke menu languange
language_dropdown = driver.find_element(By.ID, "profile_language")
#mengganti ke bahasa melayu
Select(language_dropdown).select_by_visible_text("Bahasa Melayu")  
#menyimpan perubahan bahasa
profile_save = driver.find_element(By.ID, "profile_save")
profile_save.click()
time.sleep(5)

driver.quit()