import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from damage_inventory import DamageInventorySwitch
from time import sleep


class Challenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")
        self.driver.implicitly_wait(30)
        # Load page
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        self.wait = WebDriverWait(self.driver, 30)

    def tearDown(self):
        self.driver.close()

    def test_copart_search_porche_100_inventory_models(self):
        maker = "porsche"
        table_length = '100'

        # Search for maker
        search_field = self.driver.find_element(By.ID, "input-search")
        search_field.click()
        search_field.send_keys(maker)
        search_button = self.driver.find_element(By.XPATH, '//button[@ng-click="search()"]')
        search_button.click()

        # Set table length
        table_length_selector = Select(
            self.driver.find_element(By.XPATH, '//select[@name="serverSideDataTable_length"]'))
        table_length_selector.select_by_visible_text(table_length)

        # Get model names from table
        self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, '//tbody//span[@data-uname="lotsearchLotmodel"]')))
        model_elements_list = self.driver.find_elements(By.XPATH, '//tbody//span[@data-uname="lotsearchLotmodel"]')
        print(len(model_elements_list))

        model_inventory = {}

        for model_element in model_elements_list:
            model = model_element.text
            # print( model )

            if model in model_inventory.keys():
                model_inventory[model] += 1
            else:
                model_inventory[model] = 1

        print(model_inventory)

    def test_copart_search_porche_100_inventory_damage(self):
        maker = "porsche"
        table_length = '100'

        # Search for maker
        search_field = self.driver.find_element(By.ID, "input-search")
        search_field.click()
        search_field.send_keys(maker)
        search_button = self.driver.find_element(By.XPATH, '//button[@ng-click="search()"]')
        search_button.click()

        # Set table length
        table_length_selector = Select(
            self.driver.find_element(By.XPATH, '//select[@name="serverSideDataTable_length"]'))
        table_length_selector.select_by_visible_text(table_length)

        # Get damage types from table
        self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, '//tbody//span[@data-uname="lotsearchLotdamagedescription"]')))

        damage_elements_list = self.driver.find_elements(By.XPATH,
                                                         '//tbody//span[@data-uname="lotsearchLotdamagedescription"]')

        # print( len(damage_elements_list) )

        damage_type_list = list()

        for damage_element in damage_elements_list:
            damage = damage_element.text
            damage_type_list.append(damage)
            # print(damage)

        print(len(damage_type_list))
        damage_switch = DamageInventorySwitch()
        damage_inventory = damage_switch.get_inventory_from_list(damage_type_list)
        print(damage_inventory)


if __name__ == '__main__':
    unittest.main()
