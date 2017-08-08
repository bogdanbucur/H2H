import os
import unittest
from time import sleep
from random import randint

from appium.webdriver import webelement
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from appium import webdriver


class H2H(unittest.TestCase):

    def setUp(self):
        capabilities = {
            'automationName' : 'Appium',
            'platformName'   : 'Android',
            'platformVersion': '6.0',
            'deviceName'     : 'Pixel API 23',
            'app'            : '/Users/bogdanbucur/PycharmProjects/H2H/src/H2H.apk',
            'appPackage'     : 'com.udev.alidemirel.maintamanceandroid',
            'appActivity'    : 'activities.ActivityLogin',
            'noReset'        : True
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)

    # Login
    def test_001(self):
        sleep(2)

        try:
            self.driver.find_elements_by_class_name('android.widget.Button')[1].click()
            sleep(1)
            self.driver.find_elements_by_class_name('android.widget.Button')[1].click()

        except:
            pass

        emailField = self.driver.find_elements_by_class_name('android.widget.EditText')[0]
        emailField.click()
        emailField.clear()
        emailField.send_keys('bogdan.bucur+tech@udevoffice.ro')
        self.driver.back()

        passField = self.driver.find_elements_by_class_name('android.widget.EditText')[1]
        passField.click()
        passField.clear()
        passField.send_keys('supersecret')
        self.driver.back()

        self.driver.find_element_by_class_name('android.widget.TextView').click()

        sleep(3)
        print('Finished 1st test')

    # Create a Product of type Refrigerator
    def test_002(self):
        sleep(2)
        self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout').click()
        sleep(1)

        self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]').click()

        # Add Product
        self.driver.find_elements_by_class_name('android.widget.ImageView')[0].click()

        # Product Name
        nameField = self.driver.find_elements_by_class_name('android.widget.EditText')[0]
        nameField.click()
        nameField.clear()
        nameField.send_keys('Refrigerator type Product made in automated test')
        self.driver.back()

        # Serial Number
        snField = self.driver.find_elements_by_class_name('android.widget.EditText')[1]
        snField.click()
        snField.clear()
        snField.send_keys('11111')
        self.driver.back()

        # Label Code
        labelField = self.driver.find_elements_by_class_name('android.widget.EditText')[2]
        labelField.click()
        labelField.clear()
        labelField.send_keys('00001')
        self.driver.back()

        # Location
        self.driver.find_elements_by_class_name('android.widget.Spinner')[0].click()
        sleep(1)
        self.driver.find_elements_by_class_name('android.widget.TextView')[0].click()

        # Category
        self.driver.find_element_by_class_name('android.widget.Spinner')[1].click()
        sleep(1)
        self.driver.find_elements_by_class_name('android.widget.TextView')[0].click()
        sleep(3)

        print(self.driver.page_source)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(H2H)
    unittest.TextTestRunner(verbosity=2).run(suite)
