import time
import openpyxl
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from demoproject.PageObject import loginpage

@pytest.fixture()
def setup():
    print("run before every method")

def test_def1():
    print("Hello World")

def test_loginopencart1(uname=None, pword=None):


        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://demo.opencart.com/")
        driver.maximize_window()

        lp=loginpage(driver)
        lp.clickmyaccount()
        lp.clickonloginlink()

        time.sleep(10)
        lp.enteremail(uname)
        lp.enterpassword(pword)
        time.sleep()
        lp.clicksubmit()
        time.sleep(5)






