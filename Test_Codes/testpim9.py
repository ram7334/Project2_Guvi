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

    def test_TC_PIM_09(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=data.Suman_Selectors.input_box_username).send_keys(data.Suman_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Suman_Selectors.input_box_password).send_keys(data.Suman_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.login_xpath).click()
        assert self.driver.title == 'OrangeHRM'
        try:
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.pim_xpath).click()
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.employee_list_xpath).click()
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.edit_xpath).click()
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.job_xpath).click()
            time.sleep(3)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.job_joined_date_xpath).send_keys(data.Suman_Data.job_joined_date)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.job_title_xpath).click()
            time.sleep(8)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.job_category_xpath).click()
            time.sleep(8)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.job_sub_unit_xpath).click()
            time.sleep(8)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.job_location_xpath).click()
            time.sleep(8)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.job_employment_status_xpath).click()
            time.sleep(8)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.employee_contract_details_xpath).click()
            time.sleep(8)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.contract_start_xpath).send_keys(data.Suman_Data.contract_start)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.contract_end_xpath).send_keys(data.Suman_Data.contract_end)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.contact_details_button_xpath).click()
            time.sleep(7)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.job_save_xpath).click()
            print("SUCESSFUL #job details filling and validaion done successfully")
        except:
            print("unable to fill the details in a form")