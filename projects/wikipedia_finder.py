"""
Busca un artículo de Wikipedia con Selenium
"""
from projects.config.selenium import driver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


if __name__ == '__main__':
    driver.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")

    search = driver.find_element(By.NAME, value="search")
    search.send_keys("python", Keys.ENTER)

    article = driver.find_element(By.ID, value="mw-content-text")

    print(article.text)

    driver.close()
