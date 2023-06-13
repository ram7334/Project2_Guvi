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

    def test_TC_PIM_05(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=data.Suman_Selectors.input_box_username).send_keys(data.Suman_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Suman_Selectors.input_box_password).send_keys(data.Suman_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.login_xpath).click()
        assert self.driver.title == 'OrangeHRM'
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.pim_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.employee_list_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.edit_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.personal_details_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.drivinglicense_no_xpath).send_keys(data.Suman_Data.driving_license_no)
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.licenseexpiry_xpath).send_keys(data.Suman_Data.license_expiry_date)
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.sin_no_xpath).send_keys(data.Suman_Data.sin_no)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.nationality_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.marital_status_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.dob_xpath).send_keys(data.Suman_Data.dob)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.gender_xpath).click()
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.smoker_xpath).click()
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.save_xpath).click()
        print("SUCCESSFUL #personal details filling and validation successfully")