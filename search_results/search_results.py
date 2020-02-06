from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class search_results:
    def __init__(self, driver):
        print("Initializing search_results.")
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.dropdown_xpath = '//select[@name="serverSideDataTable_length"]'
        self.table_body_xpath = '//*[@id="serverSideDataTable"]/tbody'
        self.result_number_dropdown_options = {"short": "20",
                                               "medium": "50",
                                               "long": "100"}

    def change_dropdown(self, dropdown_option):
        table_length = self.result_number_dropdown_options[dropdown_option]
        print("Selecting number of search results per page: {}".format(table_length))
        table_length_selector = Select(
            self.driver.find_element(By.XPATH, self.dropdown_xpath))
        table_length_selector.select_by_visible_text(table_length)
        self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.table_body_xpath + '/tr')))

    def find_in_table(self, query):
        self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.table_body_xpath + '/tr')))
        table_body = self.driver.find_element(By.XPATH, self.table_body_xpath)
        table_body_source = table_body.get_attribute('innerHTML')
        if query.lower() in table_body_source.lower():
            print("Found {} in table.".format(query))
            return True
        else:
            print("Failed to find {} in table.".format(query))
            return False

    def count_in_table(self, query):
        self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.table_body_xpath + '/tr')))
        table_rows = self.driver.find_elements(By.XPATH, self.table_body_xpath + "/tr")
        hit_count = 0
        for row in table_rows:
            if query.lower() in row.text.lower():
                hit_count += 1
        print("Found {} rows with instances of query {} in table.".format(hit_count, query))

        return hit_count
