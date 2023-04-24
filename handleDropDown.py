from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(5)
signupButton = driver.find_element(By.XPATH, "//a[text()='Create new account']")
signupButton.click()
time.sleep(3)
month = driver.find_element(By.ID,'month')
monthDD = Select(month)
#march
monthDD.select_by_index(3)





