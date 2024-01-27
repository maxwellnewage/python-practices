from selenium import webdriver
from selenium_stealth import stealth
from projects.config.globals import CHROMIUM_BINARY_PATH

__options = webdriver.ChromeOptions()

__options.add_argument("start-maximized")
__options.add_experimental_option("excludeSwitches", ["enable-automation"])
__options.add_experimental_option('useAutomationExtension', False)
__options.add_experimental_option("detach", True)
__options.binary_location = CHROMIUM_BINARY_PATH

driver = webdriver.Chrome(options=__options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
