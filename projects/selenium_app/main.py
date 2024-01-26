"""
Web Scrapping con Selenium
https://youtu.be/SPM1tm2ZdK4
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from projects.config.globals import CHROMIUM_BINARY_PATH

if __name__ == '__main__':
    options = Options()
    options.add_experimental_option("detach", True)

    # especifica un directorio de la instalación de Chrome
    options.binary_location = CHROMIUM_BINARY_PATH

    # inicializo el driver de Chrome
    driver = webdriver.Chrome(
        options=options
    )

    # accedo a una URL
    driver.get("https://www.neuralnine.com/")

    # maximizo la ventana
    driver.maximize_window()

    # busco los links en la navbar
    links = driver.find_elements(By.XPATH, "//a[@href]")

    for link in links:
        # busco la opción Books y entro
        if "Books" in link.get_attribute("innerHTML"):
            link.click()
            break

    # recorro la lista de libros y busco el que contiene un titulo "7 IN 1"
    div_container = "//div[contains(@class, 'elementor-column-wrap')]"
    contains_text = "text()[contains(., '7 IN 1')]"
    h2 = f"[.//h2[{contains_text}]]"
    count_a = "[count(.//a)=2]//a"

    book_links = \
        driver.find_elements(By.XPATH, f"{div_container}{h2}{count_a}")

    # hago click en ese libro
    book_links[0].click()

    # cambio a la tab del libro en amazon
    driver.switch_to.window(driver.window_handles[1])

    # espero 3 segundos
    time.sleep(3)

    # busco el precio de Tapa Blanda
    a_span = "//a[.//span[text()[contains(., 'Pasta blanda')]]]"
    span_dollar = "//span[text()[contains(., 'US$')]]"

    buttons = driver.find_elements(By.XPATH, f"{a_span}{span_dollar}")

    for button in buttons:
        # imprimo el valor en US$
        print(button.get_attribute("innerHTML").replace("&nbsp;", ""))
