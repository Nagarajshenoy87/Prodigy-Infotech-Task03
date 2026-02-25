from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def setup_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    return driver


# Positive Test Case
def test_valid_login():
    driver = setup_driver()

    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    success_message = driver.find_element(By.ID, "flash").text

    assert "You logged into a secure area!" in success_message

    driver.quit()


# Negative Test Case
def test_invalid_login():
    driver = setup_driver()

    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("wrongpassword")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    error_message = driver.find_element(By.ID, "flash").text

    assert "Your username is invalid!" in error_message

    driver.quit()


# Empty Fields Test Case
def test_empty_login():
    driver = setup_driver()

    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    error_message = driver.find_element(By.ID, "flash").text

    assert "Your username is invalid!" in error_message

    driver.quit()