import time

from decouple import config
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def join_zoom_meet(url):
    # Definition des options de Chrome
    options = Options()
    # options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--start-maximized')
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 0,
        "profile.default_content_setting_values.notifications": 0
    })

    # Creation de l'instance de Chrome
    browser = webdriver.Chrome(config("CHROME_DRIVER_PATH", "DEFAULT_EXECUTABLE_PATH"), options=options)

    # On se dirige vers la page de reunion
    browser.get(url)
    # browser.switch_to.alert.accept()
    browser.implicitly_wait(100)

    # On ferme l'alerte et accepte les cookies
    browser.find_element(By.ID, 'onetrust-accept-btn-handler')

    # On clique sur le bouton pour lancer le meet, ce bouton activera l'instruction qui suit
    browser.find_element(By.XPATH, '//*[@id="zoom-ui-frame"]/div[2]/div/div[1]/div').click()
    # browser.switch_to.alert.dismiss()

    # On clique sur le lien pour joindre depuis le navigateur
    join_from_browser_button = browser.find_element(By.XPATH, '//*[@id="zoom-ui-frame"]/div[2]/div/div[2]/h3[2]/span/a')
    join_from_browser_button.click()
    browser.implicitly_wait(50)

    # On entre le nom pour rejoindre le meet
    input_name = browser.find_element(By.ID, 'inputname')
    input_name.send_keys(config("MEET_NAME"))
    time.sleep(3)
    browser.find_element(By.ID, 'rememberMyNameChecked').click()

    # On rejoins  le meet
    browser.find_element(By.ID, 'joinBtn').click()
    time.sleep(3)
    browser.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/button')
    browser.implicitly_wait(100)
