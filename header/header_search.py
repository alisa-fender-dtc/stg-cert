from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class header_search:
    def __init__(self, driver):
        print("Initializing header_search.")
        self.driver = driver

    def search_for(self, query):
        found_query = False
        search_field = self.driver.find_element(By.ID, "input-search")
        # search_field.click()
        search_field.clear()
        search_field.send_keys(query)
        search_button = self.driver.find_element(By.XPATH, '//button[@data-uname="homepageHeadersearchsubmit"]')
        search_button.click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH,
                                                                             '//*[@id="serverSideDataTable"]//tbody')))
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@data-uname="lotsearchFilterli"]')))
        table_data = self.driver.find_element(By.XPATH, '//*[@id="serverSideDataTable"]//tbody' )
        visible = table_data.text
        # print("Table data text: {}".format(visible))
        print("Searched for " + query)
        if query.lower() in visible.lower():
            found_query = True
            print("Found {} in data table.".format(query))
        else:
            found_query = False
            print("Failed to find {} in data table.".format(query))
        return found_query
