import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver1=webdriver.Chrome(ChromeDriverManager().install())
driver1.get("https://demo.opencart.com/")
driver1.find_element(By.LINK_TEXT,"My Account").click()
driver1.find_element(By.LINK_TEXT,"Register").click()

time.sleep(5)

print(driver1.title)

driver1.find_element(By.ID,"input-firstname").send_keys("mala")
driver1.find_element(By.ID,"input-lastname").send_keys("sharma")
driver1.find_element(By.ID,"input-email").send_keys("malas@gmail.com")
driver1.find_element(By.ID,"input-password").send_keys("malasharma")
driver1.find_element(By.XPATH,"//button[@type='submit']").click()




