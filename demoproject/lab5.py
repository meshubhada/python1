import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def loginopencart(username,password):

    driver1=webdriver.Chrome(ChromeDriverManager().install())
    driver1.get("https://demo.opencart.com/")
    driver1.find_element(By.LINK_TEXT,"My Account").click()
    driver1.find_element(By.LINK_TEXT,"Login").click()

    time.sleep(5)

    if driver1.title=="Your store":

        print("title match")
    else:
        print("title not matched")

    driver1.find_element(By.ID, "input-email").send_keys("abc@gmail.com")
    driver1.find_element(By.ID, "input-password").send_keys("abc")
    driver1.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

loginopencart("abc@gmail.com","abc")
