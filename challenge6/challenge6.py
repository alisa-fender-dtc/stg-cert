import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import datetime
import os


class Challenge6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")
        self.driver.implicitly_wait(20)
        # Load page
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        self.wait = WebDriverWait(self.driver, 30)

    def tearDown(self):
        self.driver.close()

    @staticmethod
    def get_timestamp():
        now = datetime.datetime.now()
        now = str(now)
        year = now[:4]
        month = now[5:7]
        day = now[8:10]
        hour = now[11:13]
        minute = now[14:16]
        sec = now[17:19]

        time_string = year + '.' + month + '.' + day + '_' + hour + '.' + minute + '.' + sec
        # print time_string
        return time_string

    def take_screenshot(self):
        directory = '../screenshots'
        if not os.path.exists(directory):
            os.makedirs(directory)
            print("Creating directory " + directory)
        timestamp = self.get_timestamp()
        screenshot_file_name = directory + '/screenshot_' + timestamp + '.png'
        self.driver.save_screenshot(screenshot_file_name)
        print("Saving screenshot: " + screenshot_file_name)

    def test_copart_search_nissan_find_models(self):
        filter_name = 'Model'
        car_make = "nissan"
        car_models = ["altima", "maxima", "skyline", "fail_this"]

        for car_model in car_models:
            # Search for car make
            search_field = self.driver.find_element(By.ID, "input-search")
            search_field.click()
            search_field.clear()
            search_field.send_keys(car_make)
            search_button = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/div/div[2]/button')
            search_button.click()

            try:
                # Filter by model - Start by clearing active filters
                self.driver.find_element(By.XPATH, '//*[@data-uname="watchlistClearall"]').click()

                filters = self.driver.find_elements(By.XPATH, '//*[@data-uname="lotsearchFilterli"]')

                count = 1
                for filter_element in filters:
                    if filter_name in filter_element.text:
                        filter_element.click()
                        break
                    count += 1

                model_filter_xpath = '//*[@id="collapseinside' + str(count) + '"]/form/div/input'
                self.driver.find_element(By.LINK_TEXT, "Model").click()

                model_filter_entry = self.driver.find_element(By.XPATH, model_filter_xpath)
                model_filter_entry.clear()
                model_filter_entry.send_keys(car_model)

                model_element_list = self.driver.find_elements(By.XPATH, '//input[@name="MODL"]')
                print("Found {} variations of {} model: {}.".format(len(model_element_list), car_make, car_model))
                model_element_list[0].click()

            except NoSuchElementException as e:
                print(e)
                print("Looking for listings for {} {}".format(car_make, car_model))
                self.take_screenshot()
            except IndexError as e:
                print(e)
                print("Looking for listings for {} {}".format(car_make, car_model))
                self.take_screenshot()
            except Exception as e:
                print(e)
                print("Looking for listings for {} {}".format(car_make, car_model))
                self.take_screenshot()


if __name__ == '__main__':
    unittest.main()
