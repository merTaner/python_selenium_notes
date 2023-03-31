from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SaucedemoTest():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    def empty_skip(self):
        self.driver.get("https://www.saucedemo.com/")
        
        sleep(3)

        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

        sleep(2)

        error_message = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        result = error_message.text == "Epic sadface: Username is required"
        
        print(f"Test Result : {result}")

        skip_button = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3/button")
        sleep(1)
        skip_button.click()

        sleep(3)

    def password_skip(self):
        self.driver.get("https://www.saucedemo.com/")
        
        sleep(2)
        
        user_name = self.driver.find_element(By.ID, "user-name")
        user_name.send_keys("test user name")

        sleep(1)

        password = self.driver.find_element(By.ID, "password")

        sleep(2)

        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

        sleep(2)

        error_message = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        result = error_message.text == "Epic sadface: Password is required"
        
        print(f"Test Result : {result}")

    def special_user(self):
        self.driver.get("https://www.saucedemo.com/")
        
        sleep(2)
        
        user_name = self.driver.find_element(By.ID, "user-name")
        user_name.send_keys("locked_out_user")

        sleep(1)

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")
        sleep(2)

        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

        sleep(2)

        error_message = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        result = error_message.text == "Epic sadface: Sorry, this user has been locked out."
        
        print(f"Test Result : {result}")

    def route(self):
        self.driver.get("https://www.saucedemo.com/")
        
        sleep(2)
        
        user_name = self.driver.find_element(By.ID, "user-name")
        user_name.send_keys("standard_user")

        sleep(1)

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        sleep(2)

        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

        sleep(5)

        product_list = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"Gösterilen ürün sayısı {len(product_list)} adet.")

    def visibility_element_located(self, located):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((located)))

    def expencive_top_product_of_page(self):
        self.driver.get("https://www.saucedemo.com/")
        self.visibility_element_located((By.ID, "user-name"))
        user_name = self.driver.find_element(By.ID, "user-name")
        user_name.send_keys("standard_user")

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

        # find of filter option
        self.visibility_element_located((By.XPATH, "//*[@id='header_container']/div[2]/div/span/select"))
        self.driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/div/span/select").click()

        # click on the filter for high price of option 
        self.visibility_element_located((By.XPATH, "//*[@id='header_container']/div[2]/div/span/select/option[4]"))
        self.driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/div/span/select/option[4]").click()

        self.visibility_element_located((By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div"))
        top_price = self.driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
        
        print(f"price : {top_price.text}")
        assert top_price

SaucedemoTest1 = SaucedemoTest()
# SaucedemoTest1.empty_skip()
# SaucedemoTest1.password_skip()
# SaucedemoTest1.special_user()
SaucedemoTest1.expencive_top_product_of_page()