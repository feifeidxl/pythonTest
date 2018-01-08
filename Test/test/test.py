#coding=utf-8


from appium import webdriver
import time
import os

#真实环境
store_account = {'account':'18571161280','psw':'111111','name':u'咪咪虾条'}
buyer_account = {'account':'18727120758','psw':'111111'}

cmd0 ='adb shell ime list -s'
cmd1 ='adb shell settings get secure default_input_method'
cmd2 ='adb shell ime set com.sohu.inputmethod.sogouoem/.SogouIME'
cmd3 ='adb shell ime set io.appium.android.ime/.UnicodeIME'

def enable_sougou():
    print (cmd2)
    os.system(cmd2)

def enable_unicode():
    os.system(cmd3)

def login(name, psw):
    time.sleep(2)
    phone = driver.find_element_by_id('cn.com.taodaji:id/username_edit')
    time.sleep(2)
    phone.send_keys(name)
    time.sleep(2)
    psd = driver.find_element_by_id('cn.com.taodaji:id/password_edit')
    time.sleep(2)
    psd.send_keys(psw)
    time.sleep(2)
    driver.hide_keyboard()
    time.sleep(2)
    btn = driver.find_element_by_id('cn.com.taodaji:id/login_button')
    btn.click()

desired_caps = {}

desired_caps['platformName'] = 'Android'

desired_caps['platformVersion'] = '5.1.1'

desired_caps['deviceName'] = 'Android Emulator'

desired_caps['appPackage'] = 'cn.com.taodaji'

desired_caps['appActivity'] = '.ui.activity.linkPage.StartActivity'

desired_caps['unicodeKeyboard'] = True

desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

'''打开店铺-------------------------------------------------------------------'''

'''点击 我'''
time.sleep(5)
menulist = driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
time.sleep(5)
menulist[4].click()

#采购商登录
print ('---client login---')
enable_sougou()
driver.find_element_by_id('cn.com.taodaji:id/myself_headportrait').click()
driver.find_element_by_id('cn.com.taodaji:id/purchaser_login').click()

#输入用户名密码
login(buyer_account['account'], buyer_account['psw'])

print ('---buy goods---')
#点去挑菜
time.sleep(5)
menuList = driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
time.sleep(5)
menuList[2].click()

#搜索店铺
enable_unicode()
time.sleep(2)
driver.find_element_by_id('cn.com.taodaji:id/search_text').click()
driver.find_element_by_id('cn.com.taodaji:id/search_heard').click()
driver.find_element_by_id('cn.com.taodaji:id/shop').click()
input_txt = driver.find_element_by_id('cn.com.taodaji:id/search_edit')
input_txt.send_keys(store_account['name'])
time.sleep(5)
print (store_account['name'])
print (driver.find_element_by_id('cn.com.taodaji:id/search_edit').get_attribute('text'))
driver.find_element_by_id('cn.com.taodaji:id/right_text').click()
time.sleep(2)
driver.find_element_by_id('cn.com.taodaji:id/stroll_shop').click()
time.sleep(2)

#购买1个第一个商品
goodslist = driver.find_elements_by_id('cn.com.taodaji:id/goods_buy_group')
goodslist[0].click()
numlist = driver.find_elements_by_id('cn.com.taodaji:id/image_name')
numlist[0].click()

driver.find_elements_by_id('cn.com.taodaji:id/action_cart').click()
driver.find_elements_by_id('cn.com.taodaji:id/cart_pay').click()
driver.find_elements_by_id('cn.com.taodaji:id/place_order').click()

bill_money = driver.find_elements_by_id('cn.com.taodaji:id/cart_price_bottom').get_attribute('text')

print(bill_money)

#支付
driver.find_elements_by_id('cn.com.taodaji:id/switch1').check()
driver.find_elements_by_id('cn.com.taodaji:id/pay_ok').check()
time.sleep(2)

txt = driver.switch_to_alert().text[0:]
print(txt)

#获取支付后余额
#点击 我
time.sleep(5)
menulist = driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
time.sleep(5)
menulist[4].click()

driver.quit()