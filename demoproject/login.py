import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demo.opencart.com/")
driver.find_element(By.LINK_TEXT,"My Account").click()
driver.find_element(By.LINK_TEXT,"Login").click()

time.sleep(5)

print(driver.title)
driver.find_element(By.ID,"input-email").send_keys("abc@gmail.com")
driver.find_element(By.ID,"input-password").send_keys("abc")

driver.find_element(By.XPATH,"//button[@type='submit']").click()



