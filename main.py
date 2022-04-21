from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
from config import fb_email, fb_password
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

#On the Facebook login window

driver.maximize_window()
time.sleep(1)
accept_fb_cookies = driver.find_element(by=By.CSS_SELECTOR, value="button[value='1']")
accept_fb_cookies.click()
time.sleep(1)

fb_email_input = driver.find_element(by=By.CSS_SELECTOR, value="input[name='email']")
fb_email_input.send_keys(fb_email)

fb_password_input = driver.find_element(by=By.CSS_SELECTOR, value="input[name='pass']")
fb_password_input.send_keys(fb_password)

fb_login_button = driver.find_element(by=By.ID, value="loginbutton")
fb_login_button.click()

#Back to Tinder

driver.switch_to.window(base_window)
print(driver.title)

time.sleep(8)
allow_location = driver.find_element(by=By.XPATH, value='//*[@id="q-789368689"]/div/div/div/div/div[3]/button[1]/span')
allow_location.click()
time.sleep(1)

not_interested = driver.find_element(by=By.XPATH, value='//*[@id="q-789368689"]/div/div/div/div/div[3]/button[2]/span')
not_interested.click()
time.sleep(1)

accept_tinder_cookies = driver.find_element(by=By.XPATH, value='//*[@id="q939012387"]/div/div[2]/div/div/div[1]/div[1]/button/span')
accept_tinder_cookies.click()
time.sleep(1)

# What if we don't have anyone in the area?

try:
    go_global = driver.find_element(by=By.XPATH, value='//*[@id="q939012387"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/button/span')
    go_global.click()
except NoSuchElementException:
    print("No need to go global")
else:
    pass

for i in range(100):
    try:
        like = driver.find_element(by=By.CSS_SELECTOR,
                                   value="button[data-testid='gamepadLike']")
        like.click()
    except ElementClickInterceptedException:
        try:
            cancel = driver.find_element(by=By.CSS_SELECTOR, value="button[data-testid=cancel]")
            cancel.click()
        except ElementClickInterceptedException:
            back_to_tinder = driver.find_element(by=By.CSS_SELECTOR, value="button[title='Back to Tinder']")
            back_to_tinder.click()
        finally:
            like = driver.find_element(by=By.CSS_SELECTOR,
                                       value="button[data-testid='gamepadLike']")
            like.click()
    finally:
        time.sleep(1.5)

driver.quit()