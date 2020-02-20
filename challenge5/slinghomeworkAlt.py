import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.navigate_to import navigate_to
from common.alt_tag_inventory import alt_tag_inventory

from time import sleep


class Challenge5_sling_alt(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")
        self.driver.implicitly_wait(20)
        print("Go to Sling.com.")
        # Load page
        go = navigate_to(self.driver)
        go.go_to("https://www.sling.com", "sling")
        self.wait = WebDriverWait(self.driver, 20)


    def tearDown(self):
        self.driver.close()

    def test_slingforAltTags(self):
        self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, '//*')))

        elements = self.driver.find_elements(By.XPATH, "//*")
        print("Length of elements list: {}".format(len(elements)))

        inventory = alt_tag_inventory()
        inventory.inventory_element_list(elements)

        tag_names = ["div", "img", "a"]

        for tag_name in tag_names:
            print("{} with alt tags: {}".format(tag_name, inventory.get_tag_name_with_alt(tag_name)))
            print("{} without alt tags: {}".format(tag_name, inventory.get_tag_name_without_alt(tag_name)))

        print("Full inventory: ")
        full_inventory = inventory.get_full_tag_inventory()
        for tag_name in full_inventory.keys():
            print("{} : {}".format(tag_name, full_inventory[tag_name]))



if __name__ == '__main__':
    unittest.main()
