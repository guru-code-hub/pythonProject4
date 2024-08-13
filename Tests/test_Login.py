# Selenium Mini Project #4
# Open the URL - https://www.idrive360.com/enterprise/login
# Enter the username, password
# Verify that Trial is finished and current URL also
# Add a logic to add Allure Screen for the Trail end
# augtest_040823@idrive.com / 123456

import time
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@allure.title("Verify login to the katalon-demo-cura.herokuapp.com")
@allure.description("Verify login to the katalon-demo-cura.herokuapp.com is successful")
def test_Login():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.idrive360.com/enterprise/login")
    driver.maximize_window()
    user_name = driver.find_element(By.ID, value='username')
    user_name.send_keys('augtest_040823@idrive.com')
    pass_word = driver.find_element(By.ID, value='password')
    pass_word.send_keys('123456')
    login_button = driver.find_element(By.ID, value='frm-btn')
    login_button.click()
    time.sleep(20)
    current_URL = "https://www.idrive360.com/enterprise/account?upgradenow=true"
    isFreeTrialExp = "Your free trial has expired"
    freeTrialElement = driver.find_element(By.XPATH, value='//*[@id="expiredmsg"]/div/h5').text
    print(freeTrialElement)
    curnt_URL = driver.current_url
    time.sleep(10)
    assert current_URL == curnt_URL
    assert isFreeTrialExp == freeTrialElement
    driver.quit()
