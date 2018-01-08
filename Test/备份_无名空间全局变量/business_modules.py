# coding=utf-8


from basic_variables import *
from basic_modules import *



def open_shop():
    # step1 打开店铺，获取店铺供货款-------------------------------------------------------------------------'''

    # 点击 我
    time.sleep(5)
    menulist = driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
    time.sleep(2)
    menulist[4].click()

    # 供应商登录
    print ('---supplier login---')
    time.sleep(5)
    driver.find_element_by_id('cn.com.taodaji:id/myself_headportrait').click()
    driver.find_element_by_id('cn.com.taodaji:id/supplier_login').click()

    login(supplier_account['account'], supplier_account['psw'])

    # 打开店铺
    driver.find_element_by_id('cn.com.taodaji:id/shop_state').click()
    driver.find_element_by_id('cn.com.taodaji:id/business').click()

    # 获取供货款
    driver.find_element_by_id('cn.com.taodaji:id/supply_money').click()
    supplier_money_start = driver.find_element_by_id('cn.com.taodaji:id/supplier_money').get_attribute('text')
    print('supplier_money_start: ', supplier_money_start)

    # 退出店铺
    # 返回
    driver.find_element_by_class_name('android.widget.ImageButton').click()
    time.sleep(2)

    logout()


def buy_food():
    # step2 选菜-------------------------------------------------------------------------'''
    # 点击 我
    time.sleep(5)
    menulist = driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
    time.sleep(5)
    menulist[4].click()

    # 采购商登录
    print ('---client login---')
    driver.find_element_by_id('cn.com.taodaji:id/myself_headportrait').click()
    driver.find_element_by_id('cn.com.taodaji:id/purchaser_login').click()

    # 输入用户名密码
    login(buyer_account['account'], buyer_account['psw'])

    # 获取余额
    driver.find_element_by_id('cn.com.taodaji:id/supply_money').click()
    buyer_money = driver.find_element_by_id('cn.com.taodaji:id/supplier_money').get_attribute('text')
    print ('buyer_money: ', buyer_money)
    # 返回
    driver.find_element_by_class_name('android.widget.ImageButton').click()
    if buyer_money <= 0:
        logout()

    print ('---buy goods---')
    # 点去挑菜
    time.sleep(5)
    menuList = driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
    time.sleep(5)
    menuList[2].click()

    # 搜索店铺
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

    # 购买1个第一个商品
    goodslist = driver.find_elements_by_id('cn.com.taodaji:id/goods_buy_group')
    goodslist[0].click()
    numlist = driver.find_elements_by_id('cn.com.taodaji:id/image_name')
    numlist[0].click()

    # 点击 购物车
    driver.find_element_by_id('cn.com.taodaji:id/action_cart').click()
    # 点击 去结算
    driver.find_element_by_id('cn.com.taodaji:id/cart_pay').click()

    bill_money = driver.find_element_by_id('cn.com.taodaji:id/cart_price_bottom').get_attribute('text')
    print('bill_money: ', bill_money)

    # 选择收货地址
    driver.find_element_by_id('cn.com.taodaji:id/address_detail').click()
    time.sleep(2)
    # 选择第一个地址
    time.sleep(5)
    addr_list = driver.find_elements_by_id('cn.com.taodaji:id/item_myself_goods_receipt_address_text_layout')
    time.sleep(5)
    addr_list[0].click()

    # 点击 提交订单
    driver.find_element_by_id('cn.com.taodaji:id/place_order').click()
    time.sleep(2)

    # 支付
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
    # 获取支付后余额
    # 点击 我
    time.sleep(5)
    menulist = driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
    time.sleep(5)
    menulist[4].click()

    driver.find_element_by_id('cn.com.taodaji:id/supply_money').click()
    last_money = driver.find_element_by_id('cn.com.taodaji:id/supplier_money').get_attribute('text')
    print ('last_money: ', last_money)
    # 验证
    assert (float(last_money) == (float(buyer_money) - float(bill_money)))
    # 返回
    driver.find_element_by_class_name('android.widget.ImageButton').click()

    # 获取订单编号
    # 点击 我
    time.sleep(5)
    menulist = driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
    time.sleep(5)
    menulist[4].click()
    # 点击 待发货
    menulist = driver.find_elements_by_id('cn.com.taodaji:id/item_view')
    time.sleep(5)
    menulist[1].click()
    time.sleep(10)
    # 点击第一个订单详情
    print('click first bill to get bill num-------------')
    menulist = driver.find_elements_by_id('cn.com.taodaji:id/item_view')
    time.sleep(5)
    menulist[1].click()
    time.sleep(5)
    # 上滑
    up_swipe()
    time.sleep(2)
    # 获取订单编号
    order_num = driver.find_element_by_id('cn.com.taodaji:id/order_no').get_attribute('text')
    print ('order_num: ', order_num)
    # 返回
    driver.find_element_by_class_name('android.widget.ImageButton').click()
    time.sleep(2)
    driver.find_element_by_class_name('android.widget.ImageButton').click()
    logout()

def deliver_food():
    # type: () -> object
    # step3 发货------------------------------------------------------------------------'''
    # 再次获取店铺供货款'''
    # 点击 我
    menulist = driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
    time.sleep(5)
    menulist[4].click()

    # 供应商登录
    print ('---supplier login---')
    time.sleep(5)
    driver.find_element_by_id('cn.com.taodaji:id/myself_headportrait').click()
    driver.find_element_by_id('cn.com.taodaji:id/supplier_login').click()

    login(supplier_account['account'], supplier_account['psw'])

    # 获取供货款
    time.sleep(2)
    driver.find_element_by_id('cn.com.taodaji:id/supply_money').click()
    supplier_money_sale = driver.find_element_by_id('cn.com.taodaji:id/supplier_money').get_attribute('text')
    print('supplier_money_sale: ', supplier_money_sale)
    print('supplier_money_start: ', supplier_money_start)
    print('bill_money: ', bill_money)
    assert (float(supplier_money_sale) == (float(supplier_money_start) + float(bill_money)))

    # 返回
    driver.find_element_by_class_name('android.widget.ImageButton').click()
    time.sleep(2)

    print ('---deliver goods---')

    # 退出店铺
    logout()


def print_bills():
    # step4 后台打印-------------------------------------------------------------------------'''
    return


def after_sales_start():
    # step5 申请售后-------------------------------------------------------------------------'''
    return


def after_sales_handle():
    # step6 处理售后------------------------------------------------------------------------'''
    return


def buyer_check_done():
    # 采step8 购商验证-------------------------------------------------------------------------'''
    return


def supplier_check_done():
    # step7 供货商验证-------------------------------------------------------------------------'''
    driver.quit()
    return


