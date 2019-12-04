import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.close()

    @staticmethod
    def has_element_text(element_list, element_name):
        for element in element_list:
            try:
                # print(element.text)
                if element.text == element_name:
                    return True
            except Exception as e:
                print(e)
                pass
        return False

    def test_copart_search_exotics_find_porsche(self):
        found_target = False
        target = "PORSCHE"

        # Load page
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)

        # Search for exotics
        search_field = self.driver.find_element(By.ID, "input-search")
        search_field.click()
        search_field.send_keys("exotics")
        search_button = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/div/div[2]/button')
        search_button.click()

        # Find target make in search results
        makes = self.driver.find_elements(By.XPATH, '//*[@id="serverSideDataTable"]/tbody/tr/td[5]')
        found_target = self.has_element_text(makes, target)
        # print(found_target)

        # Page through if not found -- TODO: not detecting end. class comes back empty.
        #  TODO: Sometimes get Message: stale element reference: element is not attached to the page document on subsequent pages
        while not found_target:
            try:
                next_button = self.driver.find_element(By.XPATH, '//*[@id="serverSideDataTable_next"]/a')
                # next_button = self.driver.find_element(By.LINK_TEXT, "Next")
                # print("Class: " + next_button.get_attribute("class"))
                if "disabled" in next_button.get_attribute("class"):
                    break
                else:
                    next_button.click()
                    makes = self.driver.find_elements(By.XPATH, '//*[@id="serverSideDataTable"]/tbody/tr/td[5]')
                    found_target = self.has_element_text(makes, target)
                    sleep(1)
            except Exception as e:
                print(e)
                break

        self.assertTrue(found_target)


if __name__ == '__main__':
    unittest.main()
