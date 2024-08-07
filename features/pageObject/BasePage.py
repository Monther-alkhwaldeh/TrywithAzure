from selenium.common import TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from Utilites import configReader
import logging
from Utilites.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configReader.readConfig("locaters", locator)).click()
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locaters", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configReader.readConfig("locaters", locator)).click()
        log.logger.info(("Clicking on an element:" + str(locator)))


    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configReader.readConfig("locaters", locator)).send_keys(value)
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locaters", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configReader.readConfig("locaters", locator)).send_keys(value)
        log.logger.info(("Typing on an element:" + str(locator) + "value entered as :" + str(value)))

    def select(self, locator, value):
        global dropdown
        if str(locator).endswith("_XPATH"):
            dropdown = self.driver.find_element(By.XPATH, configReader.readConfig("locaters", locator))
        elif str(locator).endswith("_CSS"):
            dropdown = self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locaters", locator))
        elif str(locator).endswith("_ID"):
            dropdown = self.driver.find_element(By.ID, configReader.readConfig("locaters", locator))
        select = Select(dropdown)
        select.select_by_visible_text(value)
        log.logger.info(("Selecting on an element:" + str(locator) + "value selected as :" + str(value)))

    def moveTo(self, locator):
        if str(locator).endswith("_XPATH"):
            element = self.driver.find_element(By.XPATH, configReader.readConfig("locaters", locator))
        elif str(locator).endswith("_CSS"):
            element = self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locaters", locator))
        elif str(locator).endswith("_ID"):
            element = self.driver.find_element(By.ID, configReader.readConfig("locaters", locator))
        elif str(locator).endswith("_TAGNAME"):
            element = self.driver.find_element(By.TAG_NAME, configReader.readConfig("locaters", locator))

        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

        log.logger.info(("Moving  to an element:" + str(locator)))
