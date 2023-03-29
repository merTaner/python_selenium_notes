from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pathlib import Path
from datetime import date

class Test_Demo:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.forlder_path_of_name = str(date.today()) 
        Path(self.forlder_path_of_name).mkdir(exist_ok=True)

    def teardown_method(self):
        self.driver.quit()
    
    @pytest.mark.parametrize("username, pasword", [("1", "1"), ("root", "root")])
    def test_invalid_login(self, username, pasword):
        self.visibility_element_located((By.ID, "user-name"))
        user_name = self.driver.find_element(By.ID, "user-name")
        user_name.send_keys(username)

        self.visibility_element_located((By.ID, "password"))
        password = self.driver.find_element(By.ID, "password")
        password.send_keys(pasword)

        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

        error_message = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        
        self.driver.save_screenshot(self.forlder_path_of_name+f"/invalid-test-for-{username}-{pasword}.png")
        assert error_message.text == "Epic sadface: Username and password do not match any user in this service"

    def visibility_element_located(self, located):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((located)))