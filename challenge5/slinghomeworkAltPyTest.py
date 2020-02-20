import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

@pytest.fixture(params=["chrome", "firefox", "mobileIphoneX"], scope="class")

class Challenge3():

    def tesst_doterra_shop(self):
        # self.wait.until(EC.presence_of_all_elements_located(
        #     (By.XPATH, '//')))
        sleep(10)
        elements = self.driver.find_elements(By.XPATH, "//*")
        print("Length of elements list: {}".format(len(elements)))

        for e in elements:
            print(str(e.tag_name) + ": " + str(e.get_attribute("alt")))

            #divs with alt tags, img with alt a tag with alt check "" and None type
            #count how many with or without and print out at the end


