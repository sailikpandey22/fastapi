import requests
import time
from selenium.webdriver.common.by import By
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def openBrowser(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--incognito')
    options.add_argument('--headless')

    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    driver.get(url)
    cookies = []
    cookies = pickle.load(
        open("./sql_app/routers/scrape_modules/linkedin_cookies.pkl", "rb"))
    # print(type(cookies))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get(url)
    driver.maximize_window()
    print("Cookies loaded")
    return driver


def closeBrowser(driver):
    driver.close()


def download_image(image_url, file_path):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print("Image downloaded successfully.")
            return True
        else:
            print("Failed to download image. Status code:", response.status_code)
            return False
    except Exception as e:
        print("An error occurred:", e)
        return False


def get_profile_pic(username: str):
    browser = openBrowser(f'https://www.linkedin.com/in/{username}/')
    # time.sleep(1)
    # browser = openBrowser(
    #     "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
    # time.sleep(2)
    # email_field = WebDriverWait(browser, 10).until(
    #     EC.visibility_of_element_located((By.ID, 'username'))
    # )
    # email_field.send_keys('xxxxxxxx@gmail.com')
    # password_field = WebDriverWait(browser, 10).until(
    #     EC.visibility_of_element_located((By.ID, 'password'))
    # )
    # password_field.send_keys('xxxxxxxxxxx')
    # sign_in_button = WebDriverWait(browser, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    # )
    # sign_in_button.click()
    # time.sleep(2)
    # browser.get(f'https://www.linkedin.com/in/{username}/')
    img_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//img[contains(@class, 'pv-top-card-profile-picture__image')]"))
    )
    image_link = img_element.get_attribute("src").replace("amp;", "")
    closeBrowser(browser)
    # print(image_link)
    return download_image(image_link, f'./{username}.jpg')
