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


    def test_search_for_airtv(self):
        target = "AirTV"

        # Go to Help Center
        print("Go to Sling Help Center.")
        # Load page
        self.driver.get("https://help.sling.com")

        search_input = self.driver.find_element(By.XPATH, '//*[@id="support-search-input"]')
        search_input.send_keys(target)
        search_input.submit()

        search_results = self.driver.find_elements(By.XPATH, '//*[@class="search-results-list"]//child::div')

        num_results = len(search_results)
        num_target = 0

        for search_result in search_results:
            print(search_result.text)
            if target in search_result.text:
                num_target += 1

        print("Returned {} results for {}.".format(num_results, target))
        print("Found {} in title of {} articles.".format(target, num_target))
        self.assertGreaterEqual(num_target, 1)


if __name__ == '__main__':
    unittest.main()
