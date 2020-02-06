from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from search_results.search_results import search_results


class filters:
    def __init__(self, driver, filter_name):
        print("Initializing filters.")
        self.driver = driver
        self.search_results = search_results(driver)
        self.filter_name = filter_name
        self.entry_xpath = ""
        self.collapse_xpath = ""
        self.table_body_xpath = '//*[@id="serverSideDataTable"]/tbody'
        self.filter_checkboxes_xpath = '//*[@data-uname="lotsearchFilteroption"]'
        self.filter_tyes_xpath = '//*[@data-uname="lotsearchFilterli"]'
        self.clear_all_filters_xpath = '//*[@data-uname="watchlistClearall"]'
        self.wait = WebDriverWait(driver, 15)
        self._set_xpaths_of_target_filter()

    def click_filter(self):
        self.driver.find_element(By.XPATH, self.collapse_xpath).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.entry_xpath)))

    def clear_filter_entry_field(self):
        filter_entry_element = self.driver.find_element(By.XPATH, self.entry_xpath)
        filter_entry_element.click()
        filter_entry_element.clear()
        while 'ng-not-empty' in filter_entry_element.get_attribute('class'):
            filter_entry_element.send_keys(Keys.END)
            filter_entry_element.send_keys(Keys.BACK_SPACE)
            filter_entry_element = self.driver.find_element(By.XPATH, self.entry_xpath)
            filter_entry_element.click()

    def filter_search_text(self, query):
        self.clear_filter_entry_field()
        filter_entry_element = self.driver.find_element(By.XPATH, self.entry_xpath)
        filter_entry_element.send_keys(query)
        self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.table_body_xpath + '/tr')))

    def click_filter_checkbox_by_index(self, query, index=0):
        checkbox_list = self.get_checkbox_list(query)
        checkbox_list[index].click()

    def clear_all_filters(self):
        self.driver.find_element(By.XPATH, self.clear_all_filters_xpath).click()

    def get_checkbox_list(self, query):
        target_string = query.lower()
        checkboxes = self.driver.find_elements(By.XPATH, self.filter_checkboxes_xpath)
        checkbox_list = list()
        for checkbox in checkboxes:
            checkbox_value = checkbox.get_attribute('value')
            if target_string in checkbox_value.lower():
                checkbox_list.append(checkbox)
        return checkbox_list

    def _get_all_filter_elements(self):
        filter_elements = self.driver.find_elements(By.XPATH, self.filter_tyes_xpath)
        return filter_elements

    def _get_index_of_target_filter(self):
        filter_elements = self._get_all_filter_elements()
        count = 1
        for filter_element in filter_elements:
            if self.filter_name in filter_element.text:
                filter_element.click()

                break
            count += 1
        return count

    def _set_xpaths_of_target_filter(self):
        index = self._get_index_of_target_filter()
        self.entry_xpath = '//*[@id="collapseinside' + str(index) + '"]/form/div/input'
        self.collapse_xpath = '//*[@href="#collapseinside' + str(index) + '"]'

    def enter_and_verify_filter_search(self, query):
        self.click_filter()
        self.filter_search_text(query)
        self.click_filter_checkbox_by_index(query)
        self.search_results.change_dropdown("medium")
        self.search_results.count_in_table(query)

        return self.search_results.find_in_table(query)
