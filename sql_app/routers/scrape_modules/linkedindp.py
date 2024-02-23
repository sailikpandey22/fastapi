from selenium.webdriver.common.by import By
import pickle
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def openBrowser(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless=new')
    # options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options)
    print("Options added")
    driver.get(url)
    print("Url added")
    cookies = []
    cookies = pickle.load(
        open("./sql_app/routers/scrape_modules/linkedin_cookies.pkl", "rb"))
    print(type(cookies))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get(url)
    driver.maximize_window()
    print("Cookies loaded")
    return driver


def closeBrowser(driver):
    driver.close()


def get_profile_pic(username: str):
    print("Getting profile pic")
    browser = openBrowser(f'https://www.linkedin.com/in/{username}/')
    print("Opened browser")
    img_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//img[contains(@class, 'pv-top-card-profile-picture__image')]"))
    )
    image_link = img_element.get_attribute("src").replace("amp;", "")
    closeBrowser(browser)
    print(image_link)
    return image_link
