from selenium import webdriver
from selenium.webdriver.chrome.options import Options


 
class Chromedriver:

    def gera_driver(self) -> webdriver.Chrome:
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(options=options)
        return driver