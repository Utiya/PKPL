from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/")

    # Login
    username_input = driver.find_element(By.CLASS_NAME, "cc-input-component.cc-input-group-space-prepend")
    username_input.send_keys("raihan14032004@gmail.com")
    password_input = driver.find_element(By.CLASS_NAME, "cc-input-component.cc-input-group-space-prepend.cc-input-group-space-append")
    password_input.send_keys("ASUSTUFGAMINGFX506")
    login_button = driver.find_element(By.ID, "login")
    login_button.click()

    # Tunggu 5 detik untuk memastikan halaman setelah login dimuat sepenuhnya
    time.sleep(5)

    # Navigasi ke VS Computer
    play_button = driver.find_element(By.CSS_SELECTOR, '.v5-section-shadow-hover.play-quick-links-link')
    play_button.click()

    # Tunggu sebentar untuk memastikan navigasi berhasil
    time.sleep(3)

finally:
    driver.quit()
