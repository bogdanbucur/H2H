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
            'automationName': 'Appium',
            'platformName': 'Android',
            'platformVersion': '6.0',
            'deviceName': 'Pixel API 23',
            'app': '/Users/bogdanbucur/PycharmProjects/H2H/src/H2H.apk',
            'appPackage': 'com.udev.alidemirel.maintamanceandroid',
            'appActivity': 'activities.ActivityLogin',
            'noReset': True,
            'newCommandTimeout': '0'
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
        global create
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
                    categoriesLen += 1
        self.driver.find_elements_by_class_name('android.widget.TextView')[0].click()
        sleep(2)

        for i in range(categoriesLen):

            currentView = self.driver.page_source
            with open('currentView0.xml', 'w+') as a:
                a.write(currentView.replace('>', '>\n'))

            print('Run ' + str(i))
            categorySpinner.click()
            sleep(1)
            self.driver.find_elements_by_class_name('android.widget.TextView')[i].click()
            sleep(1)

            x = 0

            while True:

                with open('currentView' + str(x) + '.xml', 'r') as b:
                    EditTextIndex = 0
                    SpinnerIndex = 0
                    LinearLayoutIndex = 0
                    TextViewIndex = 0
                    CheckBoxIndex = 0
                    ViewViewIndex = 0
                    previousView = 0
                    print(type(b))
                    try:
                        for item in b:

                            if 'xml version' in item:
                                pass

                            elif 'hierarchy rotation' in item:
                                pass

                            elif 'android.widget.FrameLayout' in item:
                                pass

                            elif 'android.widget.ScrollView' in item:
                                pass

                            elif 'android.widget.RelativeLayout' in item:
                                pass

                            elif 'android.widget.ImageView' in item:
                                pass

                            elif '</android.widget.ImageView>' in item:
                                pass

                            elif '</android.widget.LinearLayout>' in item:
                                pass

                            elif '</android.widget.ScrollView>' in item:
                                pass

                            elif '</android.widget.FrameLayout>' in item:
                                pass

                            elif '</android.widget.Spinner>' in item:
                                pass

                            elif '<android.view.View' in item:
                                pass

                            elif 'class="android.widget.ViewAnimator"' in item:
                                pass

                            elif 'class="android.view.ViewGroup"' in item:
                                pass

                            elif 'class="com.android.internal.widget.ViewPager"' in item:
                                pass

                            elif 'android.widget.LinearLayout' in item:
                                if 'clickable="true"' in item:
                                    self.driver.find_elements_by_class_name('android.widget.LinearLayout')[LinearLayoutIndex].click()
                                    try:
                                        if self.driver.find_element_by_id('android:id/button2').get_attribute('text') == 'Camera':
                                            self.driver.find_element_by_id('android:id/button2').click()
                                            sleep(2)
                                            self.driver.find_element_by_id('com.android.camera:id/shutter_button').click()
                                            sleep(1)
                                            self.driver.find_element_by_id('com.android.camera:id/btn_done').click()
                                            sleep(2)
                                    except:
                                        pass
                                else:
                                    pass
                                LinearLayoutIndex += 1
                                pass

                            elif 'android.widget.TextView' in item:
                                if 'text="Create"' in item:
                                    create = self.driver.find_elements_by_class_name('android.widget.TextView')[TextViewIndex]
                                elif 'text="Fgas Certificate"' in item:
                                    pass
                                elif 'text="Data Sheets"' in item:
                                    pass
                                TextViewIndex += 1
                                pass

                            elif 'class="android.widget.EditText"' in item:
                                if 'text="Buc"' in item:
                                    textField = self.driver.find_elements_by_class_name('android.widget.EditText')[EditTextIndex]
                                    textField.click()
                                    textField.send_keys('1')
                                    self.driver.back()
                                elif 'text="Duration"' in item:
                                    textField = self.driver.find_elements_by_class_name('android.widget.EditText')[EditTextIndex]
                                    textField.click()
                                    textField.send_keys('1')
                                    self.driver.back()

                                elif 'text="Width"' in item:
                                    textField = self.driver.find_elements_by_class_name('android.widget.EditText')[EditTextIndex]
                                    textField.click()
                                    textField.send_keys('102 cm')
                                    self.driver.back()
                                else:
                                    textField = self.driver.find_elements_by_class_name('android.widget.EditText')[EditTextIndex]
                                    textField.click()
                                    textField.send_keys('Wrote something')
                                    self.driver.back()
                                EditTextIndex += 1

                            elif 'class="android.widget.Spinner"' in item:
                                self.driver.find_elements_by_class_name('android.widget.Spinner')[SpinnerIndex].click()
                                sleep(1)

                                spinnerView = self.driver.page_source

                                if ('text="Impianti Speciali"' and 'text="Impianto Idraulico"' in spinnerView) and ('text="Impianti Speciali"' and 'text="Impianto Idraulico"' in categories):
                                    print('equals')
                                    pass
                                else:
                                    self.driver.find_elements_by_class_name('android.widget.TextView')[0].click()

                                SpinnerIndex += 1
                                sleep(2)

                            elif 'class="android.widget.CheckBox"' in item:
                                self.driver.find_elements_by_class_name('android.widget.CheckBox')[CheckBoxIndex].click()
                                CheckBoxIndex += 1
                                sleep(1)

                            elif 'class="android.widget.DatePicker"' in item:
                                pass

                            else:
                                try:
                                    create.click()
                                    sleep(1)
                                    self.driver.find_elements_by_class_name('android.widget.ImageView')[0].click()
                                    b.close()
                                except:
                                    self.driver.swipe(550, 1700, 550, 100)
                                    currentView = self.driver.page_source

                                    with open('currentView' + str(x + 1) + '.xml', 'w+') as c:
                                        c.write(currentView.replace('>', '>\n'))
                                    sleep(2)

                                    x += 1
                    except:
                        break

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(H2H)
    unittest.TextTestRunner(verbosity=2).run(suite)
