from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.ui import Select
import time


# import selenium.webdriver.chrome.service import Service


class DemoAutoSuggest():
    def demo_autosuggest_dropdown(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(3)
        depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        time.sleep(3)
        depart_from.send_keys("New Delhi")
        depart_from.send_keys(Keys.ENTER)
        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New")
        search_result = driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")
        print(len(search_result))

        for result in search_result:
            if "New York (JFK)" in result.text:
                result.click()
                break


obj = DemoAutoSuggest()
obj.demo_autosuggest_dropdown()
