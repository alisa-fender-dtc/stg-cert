from selenium import webdriver
from selenium.webdriver.common.by import By


class navigate_to:
    def __init__(self, driver):
        self.driver = driver

    def go_to(self, url, verify_text):
        got_text = False
        self.driver.get(url)
        page_source = self.driver.page_source
        if verify_text in page_source:
            got_text = True

        return got_text
