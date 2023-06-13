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

    def test_TC_PIM_07(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=data.Suman_Selectors.input_box_username).send_keys(data.Suman_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Suman_Selectors.input_box_password).send_keys(data.Suman_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.login_xpath).click()
        assert self.driver.title == 'OrangeHRM'
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.pim_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.employee_list_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.edit_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.emergency_contacts_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.emergency_con_add_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.eme_name_xpath).send_keys(data.Suman_Data.eme_name)
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.eme_rel_xpath).send_keys(data.Suman_Data.eme_relation)
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.eme_mobile_xpath).send_keys(data.Suman_Data.eme_mobile_no)
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.eme_save_xpath).click()
        print("successful # filled details are present in contact page")



