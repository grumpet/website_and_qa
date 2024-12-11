from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import logging

# Configure logging
logging.basicConfig(filename='qa.log', level=logging.INFO, 
                    format='%(asctime)s %(levelname)s %(message)s')

def setup_driver():
    driver = webdriver.Chrome()
    return driver

def open_home_page(driver):
    logging.info('Opening the page http://127.0.0.1:5000/')
    driver.get("http://127.0.0.1:5000/")
    try:
        assert "Home Page" in driver.title
        logging.info('Home Page title is present')
    except AssertionError:
        logging.error('Home Page title is not present')
    time.sleep(2)

def navigate_to_signup_page(driver):
    logging.info('Navigating to the sign-up page')
    signup_link = driver.find_element(By.LINK_TEXT, "Sign Up")
    signup_link.click()
    time.sleep(2)

def fill_signup_form(driver):
    logging.info('Filling out the sign-up form')
    username_input = driver.find_element(By.ID, "username")
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")

    username_input.send_keys("testuser")
    email_input.send_keys("testuser@example.com")
    password_input.send_keys("password123")

    logging.info('Submitting the sign-up form')
    signup_button = driver.find_element(By.XPATH, "//button[text()='Sign Up']")
    signup_button.click()
    time.sleep(2)

def verify_home_page(driver):
    try:
        assert "Home Page" in driver.title
        logging.info('Sign-up successful, redirected to Home Page')
    except AssertionError:
        logging.error('Sign-up failed, not redirected to Home Page')

def navigate_to_add_payment_page(driver):
    logging.info('Navigating to the add payment page by user')
    add_payment_link = driver.find_element(By.LINK_TEXT, "add payment")
    add_payment_link.click()
    time.sleep(2)
    try:
        assert "Add Payment" in driver.title
        logging.info('Add Payment Page title is present for user')
    except AssertionError:
        logging.error('Add Payment Page title is not present for user')

def fill_add_payment_form(driver):
    logging.info('Filling out the add payment form')
    card_number_input = driver.find_element(By.ID, "card_number")
    expiry_date_input = driver.find_element(By.ID, "expiry_date")
    cvv_input = driver.find_element(By.ID, "cvv")

    card_number_input.send_keys("123456789")
    expiry_date_input.send_keys("12/24")
    cvv_input.send_keys("123")

    add_payment_method_button = driver.find_element(By.XPATH, "//button[text()='Add Payment Method']")
    add_payment_method_button.click()
    time.sleep(2)

def view_picture(driver):
    logging.info('Viewing a picture')
    picture_link = driver.find_element(By.LINK_TEXT, "View")
    picture_link.click()
    time.sleep(2)

def confirm_picture(driver):
    logging.info('Confirming the picture')
    confirm_button = driver.find_element(By.XPATH, "//button[text()='Yes']")
    confirm_button.click()
    try:
        assert "Picture" in driver.title
        logging.info('Picture confirmed successfully')
    except AssertionError:
        logging.error('Picture confirmation failed')
    time.sleep(2)

def open_settings_page(driver):
    logging.info('Opening the settings page')
    settings_link = driver.find_element(By.LINK_TEXT, "Settings")
    settings_link.click()
    time.sleep(2)
    try:
        assert "Settings" in driver.title
        logging.info('Settings Page title is present')
    except AssertionError:
        logging.error('Settings Page title is not present')
    
def terminate_account(driver):
    logging.info('Terminating the account')
    terminate_button = driver.find_element(By.XPATH, "//button[text()='Terminate Account']")
    terminate_button.click()
    time.sleep(2)
    


    


def main():
    driver = setup_driver()
    open_home_page(driver)
    navigate_to_signup_page(driver)
    fill_signup_form(driver)
    verify_home_page(driver)
    navigate_to_add_payment_page(driver)
    fill_add_payment_form(driver)
    verify_home_page(driver)
    view_picture(driver)
    confirm_picture(driver)
    open_home_page(driver)
    open_settings_page(driver)
    terminate_account(driver)
    driver.quit()
    logging.info('Browser closed')

if __name__ == "__main__":
    main()