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
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import time


class PIM02:
    url = "https://opensource-demo.orangehrmlive.com"

    # Booting Method for running the Python Tests
    def __init__(self):
        self.driver = None

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.close()

    def test_get_title(self, booting_function):
        self.driver.get(self.url)
        assert self.driver.title == 'OrangeHRM'
        print("SUCCESS # Web Title Captured Successfully")

    def test_menuitems(self, booting_function):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=test_data.Selectors.input_box_username).send_keys(
            test_data.Data.username)
        self.driver.find_element(by=By.NAME, value=test_data.Selectors.input_box_password).send_keys(
            test_data.Data.password)
        self.driver.find_element(by=By.XPATH, value=test_data.Selectors.login_xpath).click()
        assert self.driver.title == 'OrangeHRM'
        print("SUCCESS # LOGGED IN WITH USERNAME {username} and PASSWORD {password}".format(
            username=test_data.Data.username, password=test_data.Data.password))
        time.sleep(5)

        # Wait for the Admin menu to be clickable
        admin_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "menu_admin_viewAdminModule"))
        )
        admin_menu.click()

        # Validate options
        expected_options = [
            "User Management",
            "Job",
            "Organization",
            "Qualifications",
            "Nationalities",
            "Corporate Banking",
            "Configuration"
        ]

        options_elements = self.driver.find_elements(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li')
        options_text = [element.text for element in options_elements]

        for option in options_text:
            if option in expected_options:
                print("{options_text} present in webpage") 
            else:
                print("Items missing in webpage")

