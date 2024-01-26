from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from projects.config.globals import CHROMIUM_BINARY_PATH

__options = Options()
__options.add_experimental_option("detach", True)

# especifica un directorio de la instalación de Chrome
__options.binary_location = CHROMIUM_BINARY_PATH

# inicializo el driver de Chrome
driver = webdriver.Chrome(
    options=__options
)

# maximizo la ventana
driver.maximize_window()