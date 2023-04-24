from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.ui import Select
import time
# import selenium.webdriver.chrome.service import Service



driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(3)
signupButton = driver.find_element(By.XPATH, "//a[text()='Create new account']")
time.sleep(3)
signupButton.click()
time.sleep(5)

month = driver.find_element(By.XPATH,'//*[@id="month"]')
month.click()
time.sleep(1)
monthDD = Select(month)
ddList = monthDD.options

first_item = monthDD.first_selected_option
print("First Option ", first_item.text )

assert "Apr" == first_item.text
print(len(ddList))
time.sleep(6)


for ele in ddList:
    print("Value  is ", ele.text)






