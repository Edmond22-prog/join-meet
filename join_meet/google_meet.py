import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from decouple import config


def join_meet(url):

    # Configuration des options de Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('start-maximized')
    chrome_options.add_experimental_option(
        'prefs', {
            'profile.default_content_setting_values.media_stream_mic': 1,
            'profile.default_content_setting_values.media_stream_camera': 1,
            'profile.default_content_setting_values.geolocation': 0,
            'profile.default_content_setting_values.notifications': 1
        }
    )

    # Création de l'instance de Chrome
    browser = webdriver.Chrome(options=chrome_options)

    # Lancement du lien de la réunion
    print("WE ARE AT THIS STEP 0")
    browser.get(url)
    time.sleep(10)

    # Désactivation de la caméra et du micro
    print("WE ARE AT THIS STEP I")
    meet_page = browser.find_element(By.TAG_NAME, 'body')
    meet_page.send_keys(Keys.CONTROL + 'e')
    meet_page.send_keys(Keys.CONTROL + 'd')
    time.sleep(3)

    # Connexion à un compte
    print("WE ARE AT THIS STEP II")
    connexion_button = browser.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[13]/div[3]/div/div[1]/div[1]/div[2]/div/div/span')
    connexion_button.click()
    time.sleep(15)

    email_input = browser.find_element(By.ID, 'identifierId')
    email_input.click()
    email_input.send_keys(config("EMAIL"))

    next_button = browser.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')
    next_button.click()
    time.sleep(10)

    password_input = browser.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]')
    password_input.click()
    password_input.send_keys(config("PASSWORD"))

    next_button2 = browser.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/div[1]')
    next_button2.click()
    time.sleep(10)
