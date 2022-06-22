from collections import Counter
from random import randint, gauss
from time import sleep
from typing import Dict, List

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from twiggy import log

from settings import REMOTE_DRIVER, ENDING_SLEEPING_TIME


def randint(a, b):
    return min(max(int(gauss((a + b) * 3/4, (a - b) / 2)), a), b)


def _path(p1: Dict[str, int], p2: Dict[str, int], k: int) -> (List[int], List[int],):
    """
    p1, p2: points {"x": int, "y": int}
    k: number of subpoints in path
    Return list of offsets from p1 to p2 with random distribution.
    """

    def _path_for_one_cord(cord: int):
        return [
            int((p2[cord] - p1[cord]) / abs(p2[cord] - p1[cord]) * e) for e in
            Counter(randint(1, k + 1) for _ in range(abs(p2[cord] - p1[cord]))).values()
        ]

    return zip(_path_for_one_cord("x"), _path_for_one_cord("y"))


class Page:

    def __init__(self, url: str):
        self.account: WebElement = None
        self.about: WebElement = None
        self.header: WebElement = None
        self.select: WebElement = None
        self.number_input: WebElement = None
        self.button: WebElement = None
        self.region: WebElement = None
        self._driver: webdriver = None
        self.url: str = url

    def move(self, begin: WebElement, end: WebElement, subpoints: int = 10, time: float = 0.1):
        """Move from begin webelement to end webelement in 10 setes in 0.1s"""
        log.debug(F"Move from {begin} to {end}")
        sleep_time = time / subpoints
        action_chains = webdriver.ActionChains(self._driver)
        for x, y in _path({"x": begin.location["x"] + begin.size["width"] // 2,
                           "y": begin.location["y"] + begin.size["height"] // 2},
                          {"x": end.location["x"] + end.size["width"] // 2,
                           "y": end.location["y"] + end.size["height"] // 2},
                          subpoints):
            action_chains.move_by_offset(x, y).pause(sleep_time)
        action_chains.move_to_element(end).pause(sleep_time)
        action_chains.perform()

    def select_many_times_options(self):
        action_chains = webdriver.ActionChains(self._driver)
        action_chains.move_by_offset(15, -60).pause(0.25).click().pause(0.25)
        action_chains.move_by_offset(-10, 30).pause(0.25).click().pause(0.25)
        action_chains.move_by_offset(10, 90).pause(0.25).click().pause(0.25)
        action_chains.move_by_offset(10, -160).pause(0.25).click().pause(0.25)
        action_chains.perform()

    def click(self):
        webdriver.ActionChains(self._driver).click().perform()

    def move_to_account(self):
        webdriver.ActionChains(self._driver).move_to_element(self.account).perform()

    def fill_number(self):
        sleep(1)
        for i in "14000" + 5 * Keys.BACKSPACE + "15000":
            self.number_input.send_keys(str(i))
            sleep(.2)
        sleep(1)
    
    def select_region(self,value):
        select = Select(self.region)
        select.select_by_visible_text(value)
        
        sleep(1)

    def __enter__(self):
        log.debug("Enter Page >>>>>>>>>>>>>>")
        self._driver = webdriver.Remote(REMOTE_DRIVER,
                                        DesiredCapabilities.CHROME)
        self._driver.get(self.url)
        self._set_webelements()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        sleep(ENDING_SLEEPING_TIME)
        self._driver.close()
        self._driver.quit()
        log.debug("Exit Page >>>>>>>>>>>>>>")

    def _set_webelements(self):
        self.region = self._driver.find_element_by_id("region")
        self.account = self._driver.find_element_by_link_text("Accounts")
        self.about = self._driver.find_element_by_link_text("About")
        self.header = self._driver.find_element_by_tag_name("h2")
        self.select = self._driver.find_element_by_tag_name("select")
        self.number_input = self._driver.find_element_by_id("minvalue")
        self.button = self._driver.find_element_by_id("send")
        self.region = self._driver.find_element_by_id("region")
