from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

def login(driver, username, password):
    driver.get("https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/")
    time.sleep(2)  # Tunggu sebentar untuk memastikan halaman dimuat

    try:
        # Masukkan username
        username_input = driver.find_element(By.CLASS_NAME, "cc-input-component.cc-input-group-space-prepend")
        username_input.clear()
        username_input.send_keys(username)

        # Masukkan password
        password_input = driver.find_element(By.CLASS_NAME, "cc-input-component.cc-input-group-space-prepend.cc-input-group-space-append")
        password_input.clear()
        password_input.send_keys(password)

        # Klik tombol login
        login_button = driver.find_element(By.ID, "login")
        login_button.click()
        
        time.sleep(5)  # Tunggu sebentar untuk memastikan proses login selesai

        # Cek apakah login berhasil atau tidak
        # Anda bisa menyesuaikan logika ini sesuai dengan elemen yang muncul setelah login berhasil/gagal
        try:
            driver.find_element(By.CLASS_NAME, "promo-title")
            print("Login berhasil")
            return True
        except NoSuchElementException:
            print("Login gagal")
            return False

    except NoSuchElementException as e:
        print("Elemen tidak ditemukan:", e)
        return False

# Inisialisasi Service dan WebDriver
service = Service(executable_path="chromedriver.exe")

# Login berhasil
driver = webdriver.Chrome(service=service)
if login(driver, "raihan14032004@gmail.com", "ASUSTUFGAMINGFX506"):
    print("Proses login pertama berhasil.")
else:
    print("Proses login pertama gagal.")
driver.quit()

# Tunggu beberapa detik sebelum mencoba login kembali
time.sleep(2)

# Login gagal
driver = webdriver.Chrome(service=service)
if login(driver, "raihan14032004@gmail.com", "passwordSALAH01"):
    print("Proses login kedua berhasil.")
else:
    print("Proses login kedua gagal.")
driver.quit()
