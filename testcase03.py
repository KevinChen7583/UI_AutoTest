# 登录英雄联盟
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome()
driver.maximize_window()
#访问百度页面
driver.get('https:\\www.baidu.com')

#搜索框输入lol
driver.find_element_by_id('kw').send_keys('lol')
time.sleep(2)

#点击搜索按钮
driver.find_element_by_id('su').click()
time.sleep(2)

driver.back()
time.sleep(1)

driver.forward()
time.sleep(1)

#点击lol官方网站
driver.find_element_by_xpath('//*[@id="1"]/div/div[1]/h3/a[1]').click()
time.sleep(2)

#获取多页面窗口
handles=driver.window_handles
driver.switch_to.window(handles[1])
time.sleep(1)

#获取英雄联盟头部页面
driver.find_element_by_xpath('/html/body/div[2]/div[3]')
time.sleep(1)

#点击登录按钮
e1=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/p[1]/a')
e1.click()
time.sleep(2)

#获取登录页面
driver.switch_to.frame('loginIframe')
time.sleep(3)

#点击头像登录
driver.find_element_by_id('img_out_1824565849').click()
time.sleep(3)

#点击绑定大区
e2=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/p[2]/a[1]')
e2.click()
time.sleep(2)

#点击同意协议
driver.find_element_by_xpath('//*[@id="milo_policy_tips"]/div').click()

# #点击下拉框按钮
# driver.find_element_by_xpath('//*[@id="areaContentId_lol"]').click()
# time.sleep(2)

#定位下拉框对象
sel=driver.find_element_by_id('areaContentId_lol')

#构建选择对象
selobj=Select(sel)

#使用可见文本选择对象
selobj.select_by_visible_text('征服之海 电信')
time.sleep(3)

#点击选择大区确认按钮
driver.find_element_by_id('confirmButtonId_lol').click()
time.sleep(2)
#点击注销按钮
driver.find_element_by_class_name('logined-logout').click()
time.sleep(2)
#关闭所有窗口
driver.quit()
time.sleep(2)



# #爱奇艺登录
# from selenium import webdriver
# import time
# #创建浏览器对象
# driver=webdriver.Chrome()
#
# #访问百度
# driver.get('https://www.baidu.com/')
#
# #定位文本
# driver.find_element_by_partial_link_text('犯我中华者必将受到惩处').click()
# time.sleep(2)
#
# a=driver.window_handles
# driver.switch_to.window(a[1])
# time.sleep(1)
#
# #定位搜索框，清空搜索内容
# e1=driver.find_element_by_id('kw')
# e1.clear()
# time.sleep(2)

# 搜索爱奇艺
# e1.send_keys('爱奇艺')
# driver.find_element_by_id('su').click()
# time.sleep(2)
#
# #访问爱奇艺进入官网
# driver.find_element_by_xpath('//*[@id="1"]/div/div[1]/h3/a[1]').click()
# time.sleep(2)
#
# #获取爱奇艺官网
# b=driver.window_handles
# driver.switch_to.window(b[2])
# time.sleep(1)
#
# #获取爱奇艺头部页面
# driver.find_element_by_xpath('//*[@id="block-B"]/div[1]/div')
# time.sleep(2)
#
# #点击登录按钮
# driver.find_element_by_xpath('//*[@id="J-user-wrap"]/span').click()
# time.sleep(3)
#
#
# #点击协议
# e1=driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[2]/div/div[1]/div[11]/div/a[1]/span')
# e1.click()
# time.sleep(2)
#
# #选择qq登录
# driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[2]/div/div[1]')
#
# e2=driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[2]/div/div[1]/div[12]/div[2]/a[2]')
# e2.click()
# time.sleep(2)
#
# #点击QQ方式登录
# driver.find_element_by_xpath('/html/body')
# time.sleep(2)
#
# #获取登录界面
# a=driver.window_handles
# driver.switch_to.window(a[-1])
# driver.switch_to.frame('ptlogin_iframe')
# time.sleep(1)
#
# #点击密码登录
# driver.find_element_by_link_text('密码登录').click()
# time.sleep(2)
#
# #输入QQ账号
# driver.find_element_by_id('u').send_keys('1824565849')
# time.sleep(2)
#
# #输入密码
# driver.find_element_by_id('p').send_keys('xxxxxxxxxx')
# time.sleep(2)
#
# #点击登录按钮
# driver.find_element_by_id('login_button').click()
# time.sleep(2)
#
# #获取框架
# b=driver.window_handles
# driver.switch_to.window(b[-1])
#
# #输入手机号
# e2=driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[2]/div/div[1]/div[6]/div[2]/div[1]/div[3]/input')
# e2.send_keys('18718966267')
# time.sleep(2)
#
# #点击验证码
# driver.find_element_by_class_name('send-code').click()
# time.sleep(2)
#
# #输入验证码
# e3=driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[2]/div/div[1]/div[6]/div[2]/div[2]/div[2]/input')
# e3.send_keys('785740')
# time.sleep(10)
#
# #点击登录按钮
# e4=driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[2]/div/div[1]/div[6]/div[3]/div[1]/div')
# e4.click()
# time.sleep(2)
#
# #关闭页面
# driver.quit()