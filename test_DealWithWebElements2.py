from selenium.webdriver.chrome.service import Service
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
time.sleep(5)
username = driver.find_element(By.NAME,"username")
username.send_keys("Admin")
time.sleep(3)
password = driver.find_element(By.NAME,"password")
password.send_keys("admin123")
time.sleep(3)
LoginButton = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
LoginButton.click()
time.sleep(3)