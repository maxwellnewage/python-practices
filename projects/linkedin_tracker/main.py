"""
LinkedIn Tracker
Proyecto sin terminar dado que LinkedIn me bloquea con test de robots...
"""
import time

from projects.config.selenium import driver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from projects.config.globals import LINKEDIN_USER, LINKEDIN_PASSWORD
from profile import Profile


def login():
    driver.get("https://www.linkedin.com/uas/login?")

    driver.find_element(By.ID, "username").send_keys(LINKEDIN_USER)
    driver.find_element(By.ID, "password").send_keys(LINKEDIN_PASSWORD)
    driver.find_element(By.CSS_SELECTOR, '[data-litms-control-urn="login-submit"]').click()


def auto_publish():
    driver.find_element(By.CLASS_NAME, "share-box-feed-entry__top-bar").click()

    time.sleep(2)

    message = "Prueba de texto con #selenium"

    driver.find_element(By.CSS_SELECTOR, ".ql-editor").send_keys(message)

    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, ".share-box_actions button").click()


def get_profile_info():
    # url de búsqueda
    term = "python"
    driver.get(f"https://www.linkedin.com/search/results/people/?keywords={term}&origin=CLUSTER_EXPANSION&sid=2U%40")

    # Obtengo lista de profiles
    web_profile_list = driver.find_element(By.CSS_SELECTOR, "ul.reusable-search__entity-result-list")
    web_profile_items = web_profile_list.find_elements(By.CSS_SELECTOR, "li")

    profiles: list[Profile] = []
    for profile in web_profile_items:
        avatar = profile.find_element()

    driver.close()


if __name__ == '__main__':
    login()
    # activar para publicar texto automáticamente
    # auto_publish()

    get_profile_info()






