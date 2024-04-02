from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import test_data
from Test_Locators import locators
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import time



class Test_AT2:
    url = "https://opensource-demo.orangehrmlive.com"

    def __init__(self):
        self.driver = None

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.close()

    def test_get_title(self, booting_function):
        self.driver.get(self.url)
        assert self.driver.title == 'AT2'
        print("SUCCESS # Web Title Captured Successfully")

    def test_forget_password(self, booting_function):
        try:
            self.driver.get(self.url)
            time.sleep(5)

            # xpath for forget password
            self.driver.find_element(by=By.XPATH, value=locators.Locators.xpath).click()
            time.sleep(2)

            self.driver.find_element(by=By.NAME, value=test_data.Selectors.input_box_username).send_keys(
            test_data.Data.username)

            # Reset password link
            self.driver.find_element(by=By.NAME, value=test_data.Selectors.input_box_username).send_keys(
                test_data.Data.username)

            self.driver.find_element(by=By.XPATH, value=locators.Locators.xpath1).click()
            
            success_message = self.driver.find_element(by=By.XPATH, value=locators.Locators.xpath2)

            expected_success_message = "Reset password link sent successfully."
            assert expected_success_message in success_message.text, "Unexpected success message: " + success_message.text
            print("Success message found:", success_message.text)

        except NoSuchElementException as e:
            print("Error!")

