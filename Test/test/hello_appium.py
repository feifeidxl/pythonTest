#coding=utf-8

from appium import webdriver

 

desired_caps = {}

desired_caps['platformName'] = 'Android'

desired_caps['platformVersion'] = '4.4.2'

desired_caps['deviceName'] = 'Android Emulator'

desired_caps['appPackage'] = 'com.android.calculator2'

desired_caps['appActivity'] = '.Calculator'

 
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_id("com.android.calculator2:id/digit1").click()

driver.find_element_by_id("com.android.calculator2:id/plus").click()

driver.find_element_by_id("com.android.calculator2:id/digit5").click()

driver.find_element_by_id("com.android.calculator2:id/equal").click()

test = driver.find_element_by_id("com.android.calculator2:id/edittext").text

print(test)

assert test == '1+5 \
               =6'

driver.quit()