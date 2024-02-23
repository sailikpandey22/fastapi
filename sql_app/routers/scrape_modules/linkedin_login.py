import pickle
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(
        options=options,
    )
    browser.get(
        'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

    email_field = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'username'))
    )
    email_field.send_keys('freepaidudemycourses@gmail.com')
    password_field = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'password'))
    )
    password_field.send_keys('Davidgreen12345@')
    sign_in_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    sign_in_button.click()

    time.sleep(60)

    cookies = browser.get_cookies()

    pickle.dump(cookies, open(
        "./sql_app/routers/scrape_modules/linkedin_cookies.pkl", "wb"))
