# from appium import webdriver
# import time
#
# #启动参数
# dict_caps={
#     "platformName":"Android",
#     "platformversion":"4.4.2",
#     "deviceName":"127.0.0.1:62001",
#     "appPackage":"com.android.settings",
#     "appActivity":"com.android.settings.Settings",
#     "unicodeKeyboard":"True",
#     "resetKeyboard":"True"
# }
#
# #声明driver对象
# driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',dict_caps)
# time.sleep(3)
#
# # 点击WLAN
# driver.find_element_by_id('android:id/title').click()
# time.sleep(2)
# driver.find_element_by_id('android:id/title').click()
# time.sleep(2)
# driver.find_element_by_id('android:id/button2').click()
# time.sleep(2)
# driver.find_element_by_id('android:id/up').click()
# time.sleep(2)
#
# #点击显示
# driver.tap([(87,505),(141,542)],500)
# time.sleep(2)
# #返回设置页面
# driver.find_element_by_id('android:id/up').click()
# time.sleep(2)
# #点击声音
# driver.tap([(87,432),(141,469)],500)
# time.sleep(2)
# #返回设置页面
# driver.find_element_by_id('android:id/up').click()
# time.sleep(2)
# #关闭驱动
# driver.quit()

from app_test.autotest003 import Settest
import HTMLTestRunnerCN
import unittest
import time

#获取文件路径
test_dir='../app_test'

#获取文件路径下的文件
dis=unittest.defaultTestLoader.discover(test_dir,'autotest003.py')

#在添加报告前加入时间戳
# now=time.strftime('%Y_%m_%d %H_%M_%S')

#报告存放路径
# filename='../app_test/'+now+'test_Settest.html'
filename='../app_test/test_Settest.html'

#创建报告
fp=open(filename,'wb')

#定义测试报告
runner=HTMLTestRunnerCN.HTMLTestRunner(stream=fp,title='设置报告',description='1.测试设置点击 2.测试报告滑动')
runner.run(dis)
