from selenium.webdriver.common.by import By

class top_nav_search:
    def __init__(self, driver):
        self.driver = driver

    def run_search(self, query):
        search_field = self.driver.find_element(By.ID, "input-search")
        search_field.click()
        search_field.send_keys(query)
        search_button = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/div/div[2]/button')
        search_button.click()

