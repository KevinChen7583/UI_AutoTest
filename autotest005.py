from appium import webdriver
import time
import unittest
import HTMLTestRunnerCN

dict_case={
    "platformName":"Android",
    "platformVersion":"4.4.2",
    "deviceName":"127.0.0.1:62001",
    "appPackage":"com.android.calculator2",
    "appActivity":"com.android.calculator2.Calculator",
    "unicodeKeyboard":"True",
    "resetKeyboard":"True"
}

#声明对象
class app_test(unittest.TestCase):
    #声明对象
    def setUp(self):
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',dict_case)
        time.sleep(2)

    def test01(self):
        #点击计算机'7'
        self.driver.find_element_by_id('com.android.calculator2:id/digit7').click()
        time.sleep(2)
        #点击计算机'+'
        self.driver.find_element_by_id('com.android.calculator2:id/plus').click()
        time.sleep(2)
        #点击计算机'5'
        self.driver.find_element_by_id('com.android.calculator2:id/digit5').click()
        time.sleep(2)
        #点击'='
        self.driver.find_element_by_id('com.android.calculator2:id/equal').click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()
        time.sleep(2)

# #文件路径
# Test_dir='../app_test'
#
# #获取读取文件
# dis=unittest.defaultTestLoader.discover(Test_dir,'autotest005.py')
#
# #存放报告路径
# filename='../app_test/test_005report.html'
#
# fp=open(filename,'wb')
#
# runner=HTMLTestRunnerCN.HTMLTestRunner(stream=fp,title='APP设置自动化测试报告',description='用例执行情况')
#
# runner.run(dis)
#
# fp.close()
