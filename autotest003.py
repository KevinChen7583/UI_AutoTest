# from appium import webdriver
# import unittest
# import time
#
# # 启动参数
# desired_caps={
#     'platformName':'Android',
#     'platformVersion':'4.4.2',
#     'deviceName':'127.0.0.1:62001',
#     'appPackage':'com.android.settings',
#     'appActivity':'.Settings'
# }
#
# class Settest(unittest.TestCase):
#     def setUp(self):
#         self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#
#     def test_seting(self):
#         #查看WLAN
#         self.driver.find_element_by_id("android:id/title").click()
#         time.sleep(3)
#         #回退到设置页面
#         self.driver.find_element_by_id("android:id/up").click()
#         time.sleep(3)
#         #打开显示页面（当各菜单元素相同时用模拟手指点击（tap），取bounds的值,后面的500是持续时间，单位毫秒）
#         element_info=self.driver.tap([(87,505),(141,542)],500)
#         time.sleep(3)
#         #返回到设置页面
#         self.driver.find_element_by_id("android:id/up").click()
#         time.sleep(3)
#
#     def tearDown(self):
#         #关闭驱动
#         self.driver.quit()

from appium import webdriver
import time
import unittest
import HTMLTestRunnerCN

dict_cap={}
dict_cap['platformName']='Android'
dict_cap['platformVersion']='4.4.2'
dict_cap['deviceName']='127.0.0.1:62001'
dict_cap['appPackage']='com.android.settings'
dict_cap['appActivity']='.Settings'
dict_cap['unicodeKeyboard']=True
dict_cap['resetKeyboard']=True

class Settest(unittest.TestCase):
    def setUp(self):
        #声明驱动对象
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', dict_cap)

    def test01(self):
        #点击WLAN功能
        self.driver.find_element_by_id('android:id/title').click()
        time.sleep(3)
        #点击SSID,查看网络情况
        self.driver.find_element_by_id('android:id/title').click()
        time.sleep(3)
        #断言
        self.assertTrue(self.driver.find_element_by_id('com.android.settings:id/value').is_enabled())
        #点击取消
        self.driver.find_element_by_id('android:id/button2').click()
        time.sleep(3)
        #点击返回键，退回设置页面
        self.driver.find_element_by_id('android:id/home').click()
        time.sleep(3)


    # @unittest.skip('不执行此用例')
    def test02(self):
        #查询窗口尺寸
        width=self.driver.get_window_size()['width']
        height=self.driver.get_window_size()['height']
        x=width * 0.5
        y1=height * 0.75
        y2=height * 0.25
        # 向上滑动页面
        self.driver.swipe(x,y1,x,y2,duration=1000)
        time.sleep(3)
        #向上再次滑动页面
        x1=width * 0.5
        y3=height * 0.95
        y4=height * 0.05
        self.driver.swipe(x1,y3,x1,y4,duration=1000)
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
        time.sleep(3)

# #获取文件路径
# test_dir='../app_test'
#
# #获取文件路径下的文件
# dis=unittest.defaultTestLoader.discover(test_dir,'autotest003.py')
#
# #在添加报告前加入时间戳
# now=time.strftime('%Y_%m_%d %H_%M_%S')
#
# #报告存放路径
# filename='../app_test/'+now+'test_Settest.html'
#
# #创建报告
# fp=open(filename,'wb')
#
# #定义测试报告
# runner=HTMLTestRunnerCN.HTMLTestRunner(stream=fp,title='设置报告',description='1.测试设置点击 2.测试报告滑动')
# runner.run(dis)

