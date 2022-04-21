from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

# Setting up Selenium
chrome_driver_path = "C:\Development\chromedriver.exe"
s = Service(chrome_driver_path)

driver = webdriver.Chrome(service=s)
driver.get("https://tinder.com/app/recs")
driver.maximize_window()

time.sleep(1)
log_in_button = driver.find_element(by=By.XPATH, value='//*[@id="q939012387"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
log_in_button.click()

time.sleep(1)
log_in_with_fb_button = driver.find_element(by=By.XPATH, value='//*[@id="q-789368689"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
log_in_with_fb_button.click()
time.sleep(3)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)


driver.maximize_window()
time.sleep(3)
accept_cookies = driver.find_element(By.CSS_SELECTOR, value="button[value='1']")
accept_cookies.click()


