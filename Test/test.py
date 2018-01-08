# coding=utf-8

from selenium import webdriver
import time

# step4 后台打印-------------------------------------------------------------------------'''
driver = webdriver.Chrome()
driver.get('http://test.51taodj.com/businessCenter/login.html')
time.sleep(5)
elem = driver.find_element_by_name('loginName')
elem.send_keys('admin')

elem = driver.find_element_by_name('passwd')
elem.send_keys('tdj999999')
time.sleep(10)
elem = driver.find_element_by_class_name('y_btn1')
elem.click()
time.sleep(10)
driver.quit()


