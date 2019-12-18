import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep


class ChallengeSling1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.close()

    def test_sling_orange_channel_logos(self):
        print("Go to Sling.")
        # Load page
        self.driver.get("https://www.sling.com")
        self.assertIn("Sling", self.driver.title)

        # Go to Sling Orange
        orange = self.driver.find_element(By.XPATH, '//*[@id="planOne"]')
        orange.click()

        # Get channel logos
        print("Get channel logos.")
        elements = self.driver.find_elements(By.XPATH, '//*[@id="channelList"]//..//child::img')
        indexes = len(elements)

        i = 0
        while i < indexes:
            print(elements[i].get_attribute("title") + " - " + elements[i].get_attribute("src"))
            i += 1

        print("Number of logo images: {}".format(indexes))

        self.assertGreaterEqual(indexes, 1)


if __name__ == '__main__':
    unittest.main()
