"""
LinkedIn Tracker
Proyecto sin terminar dado que LinkedIn me bloquea con test de robots...
"""
import time
import pandas as pd
from selenium.common import NoSuchElementException

from projects.config.selenium import driver
from selenium.webdriver.common.by import By
from projects.config.globals import LINKEDIN_USER, LINKEDIN_PASSWORD
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def login():
    driver.get("https://www.linkedin.com/uas/login?")

    driver.find_element(By.ID, "username").send_keys(LINKEDIN_USER)
    driver.find_element(By.ID, "password").send_keys(LINKEDIN_PASSWORD)
    driver.find_element(By.CSS_SELECTOR, '[data-litms-control-urn="login-submit"]').click()

    wait = WebDriverWait(driver, 60 * 5)
    wait.until(ec.url_matches("https://www.linkedin.com/feed/"))


def auto_publish():
    driver.find_element(By.CLASS_NAME, "share-box-feed-entry__top-bar").click()

    time.sleep(2)

    message = "Prueba de texto con #selenium"

    driver.find_element(By.CSS_SELECTOR, ".ql-editor").send_keys(message)

    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, ".share-box_actions button").click()


PAGE_LIMIT = 5
TERM = "sap%20btp"
ROLE = "SAP"


def get_profile_info(page, profile_list):
    if page >= PAGE_LIMIT + 1:
        return profile_list

    # url de búsqueda
    driver.get(
        f"https://www.linkedin.com/search/results/people/?keywords={TERM}&origin=CLUSTER_EXPANSION&page={page}&sid=E6B"
    )

    # Obtengo lista de profiles
    try:
        web_profile_list = driver.find_element(By.CSS_SELECTOR, "ul.reusable-search__entity-result-list")
        web_profile_items = web_profile_list.find_elements(By.CSS_SELECTOR, "li")
    except NoSuchElementException:
        # si llega a una pagina sin elementos, retorna la lista cargada con recursividad
        return profile_list

    for profile in web_profile_items:
        profile_keep_attrs = []
        profile_attrs = profile.text.split('\n')

        profile_keep_attrs.append(profile_attrs[0])  # nombre

        try:
            role_index = next(i for i, item in enumerate(profile_attrs) if ROLE in item)
            profile_keep_attrs.append(profile_attrs[role_index])
        except StopIteration:
            print(f"Su rol no contiene {ROLE}: {profile_attrs}")

        profile_link = profile.find_element(By.CSS_SELECTOR, "a.app-aware-link").get_attribute("href")
        profile_keep_attrs.append(profile_link)

        profile_list.append(profile_keep_attrs)

    return get_profile_info(page + 1, profile_list)


def save_profile_info(profile_list):
    """Guarda los perfiles en formato CSV"""
    profiles_df = pd.DataFrame(profile_list)
    profiles_df.to_csv('profiles.csv', index=False)


if __name__ == '__main__':
    login()
    # activar para publicar texto automáticamente
    # auto_publish()

    profiles = get_profile_info(1, [])
    save_profile_info(profiles)
