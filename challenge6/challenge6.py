import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from filters.filters import filters as filt
from header.header_search import header_search
from common.screenshot import screenshot
from common.navigate_to import navigate_to
import inspect


class Challenge6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")
        self.driver.implicitly_wait(20)

        # Load page
        self.go = navigate_to(self.driver)
        self.assertTrue(self.go.go_to("https://www.copart.com", "Copart"))

    def tearDown(self):
        self.driver.close()

    def test_copart_search_nissan_find_models(self):
        filter_name = 'Model'
        car_make = "nissan"
        car_models = ["altima", "maxima", "skyline", "fail_this"]
        shooter = screenshot(self.driver)

        for car_model in car_models:
            # Search for car make
            hsearch = header_search(self.driver)
            self.assertTrue(hsearch.search_for(car_make))

            # Search car models using filters
            test_name = inspect.stack()[1][3] + '_' + car_make + '_' + car_model
            fl = filt(self.driver, filter_name)

            try:
                self.assertTrue(fl.enter_and_verify_filter_search(car_model))

            except NoSuchElementException as e:
                print(e)
                print("Looking for listings for {} {}".format(car_make, car_model))
                shooter.take_screenshot(test_name)
            except IndexError as e:
                print(e)
                print("Looking for listings for {} {}".format(car_make, car_model))
                shooter.take_screenshot(test_name)
            except Exception as e:
                print(e)
                print("Looking for listings for {} {}".format(car_make, car_model))
                shooter.take_screenshot(test_name)


if __name__ == '__main__':
    unittest.main()
