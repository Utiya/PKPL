from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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

#navigasi ke menu sosial
social_button = driver.find_element(By.CLASS_NAME, "nav-link-component.nav-link-main-design.nav-link-top-level.sprite.social-page")
social_button.click()

#navigasi ke menu teman
friend_button = driver.find_element(By.CLASS_NAME, "landing-card-component")
friend_button.click()

#mencari akun teman
addfriend_input = driver.find_element(By.CLASS_NAME, "ui_v5-input-component.friends-search-input")
addfriend_input.send_keys("utiyas")
time.sleep(5)

driver.quit()