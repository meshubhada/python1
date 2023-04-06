import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from demoproject.PageObject import loginpage
from demoproject.lab5 import loginopencart


class testcase_001:


    def loginopencart1(username, password):

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://demo.opencart.com/")
        driver.find_element(By.LINK_TEXT, "My Account").click()
        driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(5)

        if driver.title == "Your Store":
            print("title is matched")
        else:
            print("title not matched")

        driver.find_element(By.ID, "input-email").send_keys("abc@gmail.com")
        driver.find_element(By.ID, "input-password").send_keys("abc")

        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        time.sleep(5)
        loginopencart(username, password)

        driver.quit()


