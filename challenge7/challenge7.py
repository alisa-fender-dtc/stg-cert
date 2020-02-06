import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from common.navigate_to import navigate_to

class Challenge7(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")
        self.driver.implicitly_wait(20)
        print("Go to Copart.")
        # Load page
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)


    def tearDown(self):
        self.driver.close()


    def test_challenge_3_for_loop(self):

        ## Make try except block

        # Find list of trending makes and models
        print("Get popular models.")
        nav = navigate_to(self.driver)
        cars = self.driver.find_elements(By.XPATH, '//*[@id="tabTrending"]//a')
        for car in cars:
            url = car.get_attribute("href")
            if nav.go_to(url):
                pass
            else:
                pass

    def test_challenge_3_while_loop(self):
        # Find popular categories
        print("Get popular categories.")
        categories = self.driver.find_elements(By.XPATH, '//*[@ng-if="popularSearches"]/../div[3]//a')

        indexes = len(categories)

        i=0
        while i < indexes:
            print(categories[i].text + " - " + categories[i].get_attribute("href"))
            i+=1



if __name__ == '__main__':
    unittest.main()
