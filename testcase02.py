#导包
from selenium import webdriver
#导入键盘工具
from selenium.webdriver.common.keys import Keys
#导入时间
import time
def aaa():
#创建浏览对象
    driver=webdriver.Chrome()
#创建窗口最大化
    driver.maximize_window()
#访问百度
    driver.get('https://www.baidu.com')
    time.sleep(2)

#搜索框输入QQ邮箱点击搜索
    driver.find_element_by_id('kw').send_keys('QQ邮箱')
    driver.find_element_by_id('su').click()
    time.sleep(2)

#点击qq邮箱官网
    driver.find_element_by_xpath('//*[@id="1"]/div/div[1]/h3/a[1]/em').click()
    time.sleep(5)

#获取当前所有标签
    handles=driver.window_handles
    driver.switch_to.window(handles[1])

#获取登录框架
    driver.switch_to.frame('login_frame')
    time.sleep(3)

#点击头像登录
    driver.find_element_by_id('img_out_1824565849').click()
    time.sleep(5)

#获取邮箱页面
    driver.find_element_by_xpath('//*[@id="topDataTd"]/div')
    time.sleep(2)

#点击写邮箱
    driver.find_element_by_xpath('//*[@id="composebtn"]').click()
    time.sleep(5)

#获取普通邮件框架
    driver.switch_to.frame('mainFrame')
    time.sleep(1)

#while循坏发送多份邮件
    i=0
    while i<3:

#进入收件人页面并输入内容
        e1=driver.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input')
        e1.send_keys('1391544072')
        time.sleep(2)
        e1.send_keys(Keys.ENTER)
        time.sleep(2)

#填写邮箱主题
        e2=driver.find_element_by_xpath('//*[@id="subject"]')
        e2.send_keys('学习委员')
        time.sleep(2)

#点击添加附件
        driver.find_element_by_xpath('//*[@id="AttachFrame"]/span/input').send_keys('C:/tmp/test.txt')
        time.sleep(2)

#定位正文框架
        driver.switch_to.frame(driver.find_element_by_xpath('//*[@class="qmEditorIfrmEditArea"]'))

#输入正文内容
        driver.find_element_by_xpath('/html/body/div').send_keys('张定坤是学委，他爱看蔡续坤打篮球，你干嘛！！！！')
        time.sleep(2)

#返回上一级
        driver.switch_to.parent_frame()
        time.sleep(2)

#点击发送按钮
        driver.find_element_by_xpath('//*[@id="toolbar"]/div/a[1]').click()
        time.sleep(2)

# 点击再写一封
        driver.find_element_by_id('btnagainl').click()
        time.sleep(2)
        i+=1
# #关闭当前窗口
#     driver.close()
#     time.sleep(2)
#
# # 关闭窗口
#     driver.quit()

aaa()

