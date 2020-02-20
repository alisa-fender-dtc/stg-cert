import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.screenshot import screenshot
from common.slingqa_utils import utils
from time import sleep

from common.navigate_to import navigate_to

class Challenge7(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")
        self.driver.implicitly_wait(10)
        print("Go to Copart.")
        # Load page
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)


    def tearDown(self):
        self.driver.close()



    def test_challenge_7_copart_popular_items(self):

        try:
            shooter = screenshot(self.driver)
            util = utils()

            print("Get popular searches.")
            nav = navigate_to(self.driver)
            elements = self.driver.find_elements(By.XPATH, '//*[@id="tabTrending"]//a')

            #Making url map to prevent elements list from going stale
            url_map = {}
            for element in elements:
                url = element.get_attribute("href")
                verify_text = element.text
                url_map[url] = verify_text

            for url in url_map.keys():
                try:
                    destination_url = "unset"
                    verify_text = url_map[url]
                    test_name = util.convert_to_file_name_string(["copart_popular_items", "_", verify_text])
                    print("Navigating to {} to look for {}.".format(url, verify_text))

                    navigate_success = nav.go_to(url, verify_text)
                    destination_url = self.driver.current_url

                    if navigate_success:
                        print("PASS: Origin url: {}. Destination url {} contains text {}.".format(url, destination_url, verify_text))
                    else:
                        print("FAIL: Origin url: {}. Destination url {} does not contain text {}.".format(url, destination_url, verify_text))
                        shooter.take_screenshot(test_name)
                except Exception as e:
                    print("FAIL: Excepted. Origin url {}. Destination url {}".format(url, destination_url))
                    shooter.take_screenshot(test_name)
                    print(e)
        except Exception as e:
            print("FAIL: Excepted. Origin url {}. Destination url {}".format(url, destination_url))
            shooter.take_screenshot(test_name)
            print(e)





if __name__ == '__main__':
    unittest.main()
