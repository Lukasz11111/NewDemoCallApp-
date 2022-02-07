from time import sleep

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from settings import REMOTE_DRIVER, ENDING_SLEEPING_TIME
from spring import spring


class Page:

    def __init__(self, url: str):
        self._driver = None
        self.url = url

    def __enter__(self):
        self._driver = webdriver.Remote(REMOTE_DRIVER,
                                        DesiredCapabilities.CHROME)
        self._driver.get(self.url)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        sleep(ENDING_SLEEPING_TIME)
        self._driver.close()
        self._driver.quit()

    def x(self):
        for x, y in spring():
            webdriver.ActionChains(self._driver).move_by_offset(x, y).perform()
            webdriver.ActionChains(self._driver).click()
            sleep(0.25)

    def y(self):
        self._driver.find_element_by_id("minvalue").send_keys("8888888")
        self._driver.find_element_by_id("send").click()
