import os
import unittest
from time import sleep
import lxml.etree as etree
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
        categoriesLen = 0

        sleep(2)
        self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout').click()
        sleep(1)

        self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]').click()

        # Add Product
        self.driver.find_elements_by_class_name('android.widget.ImageView')[0].click()

        # Category
        categorySpinner = self.driver.find_elements_by_class_name('android.widget.Spinner')[1]
        categorySpinner.click()
        sleep(1)

        categories = self.driver.page_source

        with open('categories.xml', 'w') as f:
            f.write(categories.replace('>', '>\n'))

        with open('categories.xml', 'r') as g:
            for item in g:
                if 'class="android.widget.TextView"' in item:
                    categoriesLen = categoriesLen + 1

        for i in range(categoriesLen):
            self.driver.find_elements_by_class_name('android.widget.TextView')[i].click()

            currentView = self.driver.page_source

            with open('currentView.xml', 'w') as a:
                a.write(currentView.replace('>', '>\n'))

                with open('currentView.xml', 'r') as b:
                    for item in b:
                        if 'class="android.widget.EditText"' in item:
                            EditTextList = self.driver.find_elements_by_class_name('android.widget.EditText')
                            for j in range(len(EditTextList)):
                                textField = self.driver.find_elements_by_class_name('android.widget.EditText')[j]
                                textField.click()
                                textField.clear()
                                textField.send_keys('Wrote something' + str(j))
                                self.driver.back()

                        elif 'class="android.widget.Spinner"' in item:
                            SpinnerList = self.driver.find_elements_by_class_name('android.widget.Spinner')
                            for j in range(len(SpinnerList) - 1):
                                self.driver.find_elements_by_class_name('android.widget.Spinner')[j].click()

                                spinnerView = self.driver.page_source

                                with open('secondaryView.xml', 'w') as c:
                                    c.write(spinnerView.replace('>', '>\n'))

                                self.driver.find_elements_by_class_name('android.widget.TextView')[0].click()
                        elif 'class="android.widget.CheckBox"' in item:
                            checkboxList = self.driver.find_elements_by_class_name('android.widget.CheckBox')
                            for l in range(len(checkboxList)):
                                self.driver.find_elements_by_class_name('android.widget.CheckBox')[l].click()

                        elif '' in item:


                        else:
                            self.driver.swipe(550, 1700, 550, 100)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(H2H)
    unittest.TextTestRunner(verbosity=2).run(suite)
