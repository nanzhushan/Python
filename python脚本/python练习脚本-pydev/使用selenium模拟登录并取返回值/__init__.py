#coding=utf-8
from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains 
driver=webdriver.Firefox() 

driver.get("https://crm.winbons.com/index") 
print u'登陆华邦云' 
driver.maximize_window() 
driver.find_element_by_name('username').send_keys('zhoulong@huabangyun.com') 
print u'输入用户名' 
driver.find_element_by_name('password').send_keys('zhoulong') 
print u'输入密码' 
driver.find_element_by_class_name('loginBt').click() 
print u'成功登陆华邦云' 
