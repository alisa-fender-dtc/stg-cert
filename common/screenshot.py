import os
from common.slingqa_utils import utils
from Screenshot import Screenshot_Clipping


class screenshot:
    def __init__(self, driver):
        print("Initializing screenshot")
        self.driver = driver

    def take_screenshot(self, test_name):
        ut = utils()
        timestamp = ut.get_timestamp()
        directory = r'../screenshots/'
        if not os.path.exists(directory):
            os.makedirs(directory)
            print("Creating directory " + directory)
        timestamp = ut.get_timestamp()

        screenshot_file_name = 'screenshot_' + test_name + '_' + timestamp + '.png'

        shooter = Screenshot_Clipping.Screenshot()
        print("Saving screenshot: " + directory + '/' + screenshot_file_name)
        img_url = shooter.full_Screenshot(self.driver, save_path=directory, image_name=screenshot_file_name)
        print(img_url)
