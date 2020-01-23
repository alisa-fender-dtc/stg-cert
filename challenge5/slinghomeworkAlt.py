import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")
        self.driver.implicitly_wait(20)
        print("Go to Sling.com.")
        # Load page
        self.driver.get("https://www.sling.com")
        self.wait = WebDriverWait(self.driver, 20)


    def tearDown(self):
        self.driver.close()

    def test_slingforAltTags(self):
        # self.wait.until(EC.presence_of_all_elements_located(
        #     (By.XPATH, '//')))
        sleep(10)
        elements = self.driver.find_elements(By.XPATH, "//*")
        print("Length of elements list: {}".format(len(elements)))

        for e in elements:
            print(str(e.tag_name) + ": " + str(e.get_attribute("alt")))



if __name__ == '__main__':
    unittest.main()
