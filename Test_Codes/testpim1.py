from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Test_Data import data
import pytest
import time

class Test_PIM:
    url = "https://opensource-demo.orangehrmlive.com"
    
    # Booting Method for running the Python Tests
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()
    
    def test_get_title(self, booting_function):
        self.driver.get(self.url)
        assert self.driver.title == 'OrangeHRM'
        print("SUCCESS # Web Title Captured Successfully")
    
    def test_TC_PIM_01(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=data.Suman_Selectors.input_box_username).send_keys(data.Suman_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Suman_Selectors.input_box_password).send_keys(data.Suman_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.login_xpath).click()
        assert self.driver.title == 'OrangeHRM'
        time.sleep(5)
        search_box=self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.search_box_xpath)
        search_box.click()
        time.sleep(4)
        search_box.send_keys("admin")
        time.sleep(4)
        search_box.send_keys(12*Keys.BACKSPACE)
        search_box.send_keys("ADMIN")
        time.sleep(4)
        search_box.send_keys(12*Keys.BACKSPACE)
        search_box.send_keys("pim")
        time.sleep(4)
        search_box.send_keys(12*Keys.BACKSPACE)
        search_box.send_keys("PIM")
        time.sleep(4)
        search_box.send_keys(12*Keys.BACKSPACE)
        search_box.send_keys("leave")
        time.sleep(4)
        search_box.send_keys(12*Keys.BACKSPACE)
        search_box.send_keys("LEAVE")
        time.sleep(4)
        search_box.send_keys(12*Keys.BACKSPACE)
        search_box.send_keys("TIME")
        time.sleep(4)
        search_box.send_keys(12*Keys.BACKSPACE)
        search_box.send_keys("time")
        time.sleep(4)
        search_box.send_keys(12*Keys.BACKSPACE)
        search_box.send_keys("recruitment")
        time.sleep(4)
        search_box.send_keys(12*Keys.BACKSPACE)
        search_box.send_keys("RECRUITMENT")
        time.sleep(4)
        search_box.send_keys(12*Keys.BACKSPACE)
        search_box.send_keys("MYINFO")
        time.sleep(4)
        search_box.send_keys(12*Keys.BACKSPACE)
        search_box.send_keys("myinfo")
        time.sleep(4)
        search_box.send_keys(12*Keys.BACKSPACE)
        search_box.send_keys("performance")
        time.sleep(4)
        search_box.send_keys(12*Keys.BACKSPACE)
        search_box.send_keys("PERFORMANCE")
        time.sleep(4)
        search_box.send_keys(12*Keys.BACKSPACE)
        search_box.send_keys("DASHBOARD")
        time.sleep(4)
        search_box.send_keys(12*Keys.BACKSPACE)
        search_box.send_keys("dashboard")
        time.sleep(4)
        search_box.send_keys(12*Keys.BACKSPACE)
        time.sleep(4)
        search_box.send_keys("directory")
        time.sleep(4)
        search_box.send_keys(12*Keys.BACKSPACE)
        search_box.send_keys("DIRECTORY")
        time.sleep(4)
        search_box.send_keys(12*Keys.BACKSPACE)
        search_box.send_keys("MAINTENANCE")
        time.sleep(4)
        search_box.send_keys(12*Keys.BACKSPACE)
        search_box.send_keys("maintenanace")
        time.sleep(4)
        search_box.send_keys(12*Keys.BACKSPACE)
        search_box.send_keys("buzz")
        time.sleep(4)
        search_box.send_keys(12*Keys.BACKSPACE)
        search_box.send_keys("buzz")
        time.sleep(4)
        print("SEARCH BOX VALIDATION DONE SUCCESSFULLY")

    


        



