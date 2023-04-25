from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(10)
search_box = driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']")
search_box.click()
search_box.send_keys("phones")
time.sleep(3)
search_button = driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']")
search_button.click()
time.sleep(3)
samsung_checkbox = driver.find_element(By.XPATH,"//li[@id='p_89/Samsung']//i[@class='a-icon a-icon-checkbox']")
samsung_checkbox.click()
time.sleep(3)
phone_list = driver.find_elements(By.XPATH,"//span[contains(@class,'a-size-medium a-color-base a-text-normal')]")
time.sleep(3)
price_list = driver.find_elements(By.XPATH,"//span[contains(@class,'a-price-whole')]")
time.sleep(3)

for phone in phone_list:
    print(phone.text)
time.sleep(3)
print("*"*50)

for price in price_list:
    print(price.text)

time.sleep(3)


driver.quit()