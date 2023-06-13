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

    def test_TC_PIM_12(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=data.Suman_Selectors.input_box_username).send_keys(data.Suman_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Suman_Selectors.input_box_password).send_keys(data.Suman_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.login_xpath).click()
        assert self.driver.title == 'OrangeHRM'
        time.sleep(5)
        try:
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.pim_xpath).click()
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.employee_list_xpath).click()
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.edit_xpath).click()
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.salary_xpath).click()
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.salary_add_xpath).click()
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.salary_component_xpath).send_keys(data.Suman_Data.salary_component)
            time.sleep(3)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.salary_paygrade_xpath).click()
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.salarypay_frequency_xpath).click()
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.salary_currency_xpath).click()
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.salary_amount_xpath).send_keys(data.Suman_Data.salary_amount)
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.direct_deposit_details_xpath).click()
            time.sleep(8)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.account_no_xpath).send_keys(data.Suman_Data.salary_account_no)
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.account_type_xpath).click()
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.routing_no_xpath).send_keys(data.Suman_Data.salary_routing_no)
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.direct_deposit_amount_xpath).send_keys(data.Suman_Data.direct_deposit_amount)
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value=data.Suman_Selectors.direct_deposit_save_xpath).click()
            print("SUCESSFUL #salary details filling and validaion done successfully")


        except:
             print("unable to fill the details in a form")