import time

from decouple import config
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def join_meet(url):

    # Definition des options de Chrome
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--start-maximized')
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 0,
        "profile.default_content_setting_values.notifications": 1
    })

    # Creation de l'instance de Chrome
    browser = webdriver.Chrome(config("CHROME_DRIVER_PATH", "DEFAULT_EXECUTABLE_PATH"), options=options)

    # On se connecte a Google
    browser.get(
        'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

    # On entre l'adresse email
    browser.find_element(By.ID, "identifierId").send_keys(config('EMAIL'))
    browser.find_element(By.ID, "identifierNext").click()
    browser.implicitly_wait(10)

    # On entre le mot de passe
    browser.find_element(By.XPATH,
                         '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(config('PASSWORD'))
    browser.implicitly_wait(10)
    browser.find_element(By.ID, "passwordNext").click()
    browser.implicitly_wait(10)

    # On se redirige vers la page d'accueil de Google
    browser.get('https://google.com/')
    browser.implicitly_wait(100)

    # On se redirige vers la page de la reunion
    browser.get(url)
    browser.implicitly_wait(100)

    # On desactive le micro et la camera
    meet_page = browser.find_element(By.TAG_NAME, 'body')
    meet_page.send_keys(Keys.CONTROL + 'e')
    meet_page.send_keys(Keys.CONTROL + 'd')
    time.sleep(3)

    # On demande à rejoindre la reunion
    join_button = browser.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[13]/div[3]/div/div[1]/div['
                                                 '4]/div/div/div[2]/div/div[2]/div[1]/div[1]/button')
    join_button.click()
    browser.implicitly_wait(100)
