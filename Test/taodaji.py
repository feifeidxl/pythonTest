#coding=utf-8

'''TODO
获取alert 内容，降低selenuum 版本为3.3.1 pip install selenium==3.3.1
总结python appium 搭建环境，及用例步骤
'''

'''
执行前注意：
退出账号，打开供应商店铺，屏蔽短信提醒
'''

from appium import webdriver
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
#真实环境
supplier_account = {'account': '18571161280', 'psw': '111111', 'name': u'咪咪虾条'}
buyer_account = {'account': '18727120758', 'psw': '111111'}
'''
#测试环境
supplier_account = {'account': '18924665240', 'psw': '111111', 'name': u'打烊了'}
buyer_account = {'account': '18727120758', 'psw': '111111'}

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
    enable_sougou()
    time.sleep(2)
    phone = driver.find_element_by_id('cn.com.taodaji:id/username_edit')
    phone.send_keys(name)
    psd = driver.find_element_by_id('cn.com.taodaji:id/password_edit')
    psd.send_keys(psw)
    driver.hide_keyboard()
    btn = driver.find_element_by_id('cn.com.taodaji:id/login_button')
    btn.click()

def upswipe():
    '''
        Swipe（int    start    x, int    start    y, int    end    x, int    y, duration)
        解释：int
        start    x－开始滑动的x坐标，
        int    start    y －开始滑动的y坐标。
        int    end    x －结束点x坐标，
        int    end    y －结束点y坐标。
        duration    滑动时间（默认5毫秒）
        '''
    # 上滑
    driver.swipe(int(driver.get_window_size()['width'] * 0.5), int(driver.get_window_size()['height'] * 0.9),
                 int(driver.get_window_size()['width'] * 0.5), int(driver.get_window_size()['height'] * 0.2))

def logout():
    #上滑
    upswipe()
    # 退出
    driver.find_element_by_id('cn.com.taodaji:id/login_out').click()

desired_caps = {}

desired_caps['platformName'] = 'Android'

desired_caps['platformVersion'] = '5.1.1'

desired_caps['deviceName'] = 'Android Emulator'

desired_caps['appPackage'] = 'cn.com.taodaji'

desired_caps['appActivity'] = '.ui.activity.linkPage.StartActivity'

desired_caps['unicodeKeyboard'] = True

desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

supplier_money_start = 0
supplier_money_sale = 0
supplier_money_return = 0
bill_money = 0
buyer_money = 0
last_money = 0

#step1 打开店铺，获取店铺供货款-------------------------------------------------------------------------'''

#点击 我
time.sleep(5)
menulist = driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
time.sleep(2)
menulist[4].click()

#供应商登录
print ('---supplier login---')
time.sleep(5)
driver.find_element_by_id('cn.com.taodaji:id/myself_headportrait').click()
driver.find_element_by_id('cn.com.taodaji:id/supplier_login').click()

login(supplier_account['account'], supplier_account['psw'])

#打开店铺
driver.find_element_by_id('cn.com.taodaji:id/shop_state').click()
driver.find_element_by_id('cn.com.taodaji:id/business').click()

#获取供货款
driver.find_element_by_id('cn.com.taodaji:id/supply_money').click()
supplier_money_start = driver.find_element_by_id('cn.com.taodaji:id/supplier_money').get_attribute('text')
print('supplier_money_start: ', supplier_money_start)

#退出店铺
#返回
driver.find_element_by_class_name('android.widget.ImageButton').click()
time.sleep(2)

logout()

#step2 选菜-------------------------------------------------------------------------'''
#点击 我
time.sleep(5)
menulist = driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
time.sleep(5)
menulist[4].click()

#采购商登录
print ('---client login---')
driver.find_element_by_id('cn.com.taodaji:id/myself_headportrait').click()
driver.find_element_by_id('cn.com.taodaji:id/purchaser_login').click()

#输入用户名密码
login(buyer_account['account'], buyer_account['psw'])

#获取余额
driver.find_element_by_id('cn.com.taodaji:id/supply_money').click()
buyer_money = driver.find_element_by_id('cn.com.taodaji:id/supplier_money').get_attribute('text')
print ('buyer_money: ', buyer_money)
#返回
driver.find_element_by_class_name('android.widget.ImageButton').click()

print ('---buy goods---')
#点去挑菜
time.sleep(5)
menuList = driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
time.sleep(5)
menuList[2].click()

#搜索店铺
time.sleep(2)
driver.find_element_by_id('cn.com.taodaji:id/search_text').click()
driver.find_element_by_id('cn.com.taodaji:id/search_heard').click()
driver.find_element_by_id('cn.com.taodaji:id/shop').click()
enable_unicode()
input_txt = driver.find_element_by_id('cn.com.taodaji:id/search_edit')
input_txt.send_keys(supplier_account['name'])
time.sleep(5)
driver.find_element_by_id('cn.com.taodaji:id/right_text').click()
time.sleep(5)
driver.find_element_by_id('cn.com.taodaji:id/stroll_shop').click()
time.sleep(2)

#购买1个第一个商品
goodslist = driver.find_elements_by_id('cn.com.taodaji:id/goods_buy_group')
goodslist[0].click()
numlist = driver.find_elements_by_id('cn.com.taodaji:id/image_name')
numlist[0].click()

#点击 购物车
driver.find_element_by_id('cn.com.taodaji:id/action_cart').click()
#点击 去结算
driver.find_element_by_id('cn.com.taodaji:id/cart_pay').click()

bill_money = driver.find_element_by_id('cn.com.taodaji:id/cart_price_bottom').get_attribute('text')
print('bill_money: ', bill_money)

#选择收货地址
driver.find_element_by_id('cn.com.taodaji:id/address_detail').click()
time.sleep(2)
#选择第一个地址
time.sleep(5)
addr_list = driver.find_elements_by_id('cn.com.taodaji:id/item_myself_goods_receipt_address_text_layout')
time.sleep(5)
addr_list[0].click()

#点击 提交订单
driver.find_element_by_id('cn.com.taodaji:id/place_order').click()
time.sleep(2)

#支付
driver.find_element_by_id('cn.com.taodaji:id/switch1').click()
driver.find_element_by_id('cn.com.taodaji:id/pay_ok').click()
time.sleep(2)
'''
wait = WebDriverWait(driver, 10)
wait.until(EC.alert_is_present())
if EC.alert_is_present():
    print ('alert show')
    time.sleep(2)
    #alert = driver.switch_to_alert()
    #print (alert.text[0:])
'''
#获取支付后余额
#点击 我
time.sleep(5)
menulist = driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
time.sleep(5)
menulist[4].click()

driver.find_element_by_id('cn.com.taodaji:id/supply_money').click()
last_money = driver.find_element_by_id('cn.com.taodaji:id/supplier_money').get_attribute('text')
print ('last_money: ', last_money)
#验证
assert(float(last_money) == (float(buyer_money) - float(bill_money)))
#返回
driver.find_element_by_class_name('android.widget.ImageButton').click()

#获取订单编号
#点击 我
time.sleep(5)
menulist = driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
time.sleep(5)
menulist[4].click()
#点击 待发货
menulist = driver.find_elements_by_id('cn.com.taodaji:id/item_view')
time.sleep(5)
menulist[1].click()
time.sleep(10)
#点击第一个订单详情
print('click first bill to get bill num-------------')
menulist = driver.find_elements_by_id('cn.com.taodaji:id/item_view')
time.sleep(5)
menulist[1].click()
time.sleep(5)
#上滑
upswipe()
time.sleep(2)
#获取订单编号
order_num = driver.find_element_by_id('cn.com.taodaji:id/order_no').get_attribute('text')
print ('order_num: ', order_num)
#返回
driver.find_element_by_class_name('android.widget.ImageButton').click()
time.sleep(2)
driver.find_element_by_class_name('android.widget.ImageButton').click()
logout()

#step3 发货------------------------------------------------------------------------'''
#再次获取店铺供货款'''
#点击 我
menulist = driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
time.sleep(5)
menulist[4].click()

#供应商登录
print ('---supplier login---')
time.sleep(5)
driver.find_element_by_id('cn.com.taodaji:id/myself_headportrait').click()
driver.find_element_by_id('cn.com.taodaji:id/supplier_login').click()

login(supplier_account['account'], supplier_account['psw'])

#获取供货款
time.sleep(2)
driver.find_element_by_id('cn.com.taodaji:id/supply_money').click()
supplier_money_sale = driver.find_element_by_id('cn.com.taodaji:id/supplier_money').get_attribute('text')
print('supplier_money_sale: ', supplier_money_sale)
print('supplier_money_start: ', supplier_money_start)
print('bill_money: ', bill_money)
assert(float(supplier_money_sale) == (float(supplier_money_start) + float(bill_money)))

#返回
driver.find_element_by_class_name('android.widget.ImageButton').click()
time.sleep(2)

print ('---deliver goods---')

#退出店铺
logout()
#step4 后台打印-------------------------------------------------------------------------'''
print ('---print goods---')
#step5 申请售后-------------------------------------------------------------------------'''
print ('---after-sales---')
#step6 处理售后------------------------------------------------------------------------'''
#step7 供货商验证-------------------------------------------------------------------------'''
print ('---check supplier---')
#采step8 购商验证-------------------------------------------------------------------------'''
print ('---check buyer---')

driver.quit()