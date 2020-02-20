from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from common.slingqa_utils import utils


class navigate_to:
    def __init__(self, driver):
        print("Initializing navigate_to.")
        self.driver = driver

    def go_to(self, url, verify_text):
        got_text = False
        self.driver.get(url)
        page_source = self.driver.page_source
        verify_text = verify_text.lower()
        page_source = page_source.lower()

        if verify_text in page_source:
            got_text = True
        else:
            sleep(5)
            page_source = page_source.lower()
            if verify_text in page_source:
                got_text = True
            else:
                print("Dumping page source...")
                ut = utils()
                ut.dump_to_text_file(page_source, ut.convert_to_file_name_string([verify_text]))

        return got_text
