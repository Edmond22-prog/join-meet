import time

from decouple import config
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def join_teams_meet(url):
    # Definition des options de Chrome
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--start-maximized')
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 0,
        "profile.default_content_setting_values.notifications": 0
    })

    # Creation de l'instance de Chrome
    browser = webdriver.Chrome(config("CHROME_DRIVER_PATH", "DEFAULT_EXECUTABLE_PATH"), options=options)
    browser.get(url)
    browser.implicitly_wait(100)

    # On désactive la caméra et le micro
    camera = browser.find_element(By.XPATH, '//*[@id="page-content-wrapper"]/div['
                                            '1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div['
                                            '2]/div/div/section/div[2]/toggle-button[1]/div/button')
    camera.click()
    browser.implicitly_wait(10)
    micro = browser.find_element(By.XPATH, '//*[@id="preJoinAudioButton"]/div/button')
    micro.click()
    browser.implicitly_wait(10)

    # On entre le nom pour rejoindre le meet et on clique sur le bouton pour rejoindre
    browser.find_element(By.ID, 'username').send_keys(config("MEET_NAME"))
    browser.find_element(By.XPATH, '//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div['
                                   '2]/div[1]/div[2]/div/div/section/div[1]/div/div[2]/button').click()
    browser.implicitly_wait(100)
