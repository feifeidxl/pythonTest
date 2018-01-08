# coding=utf-8

"""
from basic_variables import *
from basic_modules import *
"""
import basic_variables
from basic_modules import *


def open_shop():
    # step1 打开店铺，获取店铺供货款-------------------------------------------------------------------------'''

    # 点击 我
    wait(5)
    menulist = basic_variables.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
    wait(2)
    menulist[4].click()

    # 供应商登录
    print ('supplier login...')
    wait(5)
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/myself_headportrait').click()
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/supplier_login').click()

    login(basic_variables.supplier_account['account'], basic_variables.supplier_account['psw'])

    # 打开店铺
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/shop_state').click()
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/business').click()

    # 获取供货款
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/supply_money').click()
    basic_variables.supplier_money_start = \
        basic_variables.driver.find_element_by_id('cn.com.taodaji:id/supplier_money').get_attribute('text')
    print('supplier_money_start: ', basic_variables.supplier_money_start)

    # 退出店铺
    # 返回
    basic_variables.driver.find_element_by_class_name('android.widget.ImageButton').click()
    wait(2)

    logout()


def buy_food():
    # step2 选菜-------------------------------------------------------------------------'''
    # 点击 我
    wait(5)
    menulist = basic_variables.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
    wait(5)
    menulist[4].click()

    # 采购商登录
    print ('client login...')
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/myself_headportrait').click()
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/purchaser_login').click()

    # 输入用户名密码
    login(basic_variables.buyer_account['account'], basic_variables.buyer_account['psw'])
    wait(2)

    # 获取余额
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/supply_money').click()
    basic_variables.buyer_money = \
        basic_variables.driver.find_element_by_id('cn.com.taodaji:id/supplier_money').get_attribute('text')
    print ('buyer_money: ', basic_variables.buyer_money)
    # 返回
    basic_variables.driver.find_element_by_class_name('android.widget.ImageButton').click()
    if basic_variables.buyer_money <= 0:
        logout()

    print ('search goods...')
    # 点去挑菜
    wait(5)
    menuList = basic_variables.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
    wait(5)
    menuList[2].click()

    # 搜索店铺
    wait(2)
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/search_text').click()
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/search_heard').click()
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/shop').click()
    enable_unicode()
    input_txt = basic_variables.driver.find_element_by_id('cn.com.taodaji:id/search_edit')
    input_txt.send_keys(basic_variables.supplier_account['name'])
    wait(5)
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/right_text').click()
    wait(5)
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/stroll_shop').click()
    wait(2)

    # 购买1个第一个商品
    goodslist = basic_variables.driver.find_elements_by_id('cn.com.taodaji:id/goods_buy_group')
    goodslist[0].click()
    numlist = basic_variables.driver.find_elements_by_id('cn.com.taodaji:id/image_name')
    numlist[0].click()

    # 点击 购物车
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/action_cart').click()
    # 点击 去结算
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/cart_pay').click()
    # 获取商品总价
    basic_variables.bill_money_before = \
        basic_variables.driver.find_element_by_id('cn.com.taodaji:id/cart_price').get_attribute('text')
    print('bill_money_before: ', basic_variables.bill_money_before)
    # 获取订单金额
    basic_variables.bill_money_after = \
        basic_variables.driver.find_element_by_id('cn.com.taodaji:id/cart_price_bottom').get_attribute('text')
    print('bill_money_after: ', basic_variables.bill_money_after)

    print('setting address...')
    # 选择收货地址
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/address_detail').click()
    wait(2)
    # 选择第一个地址
    wait(5)
    addr_list = \
        basic_variables.driver.find_elements_by_id('cn.com.taodaji:id/item_myself_goods_receipt_address_text_layout')
    wait(5)
    addr_list[0].click()

    # 点击 提交订单
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/place_order').click()
    wait(2)

    # 支付
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/switch1').click()
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/pay_ok').click()
    wait(2)
    '''
    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    if EC.alert_is_present():
        print ('alert show')
        time.sleep(2)
        #alert = driver.switch_to_alert()
        #print (alert.text[0:])
    '''
    print('reading money now...')
    # 获取支付后余额
    # 点击 我
    wait(5)
    menulist = basic_variables.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
    wait(5)
    menulist[4].click()

    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/supply_money').click()
    basic_variables.last_money = basic_variables.driver.find_element_by_id(
        'cn.com.taodaji:id/supplier_money').get_attribute('text')
    print ('last_money: ', basic_variables.last_money)
    # 验证
    print('asserting money...')
    assert (
        (float(basic_variables.buyer_money) - float(basic_variables.bill_money_after)) == float(
            basic_variables.last_money))

    # 返回
    basic_variables.driver.find_element_by_class_name('android.widget.ImageButton').click()

    # 注意，订单详情中没有订单编号，所以无法确认第一个订单是否为买家下的订单
    # 获取订单编号
    print('click first bill to get bill num...')
    # 点击 我
    wait(5)
    menulist = basic_variables.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
    wait(5)
    menulist[4].click()
    # 点击 待发货
    menulist = basic_variables.driver.find_elements_by_id('cn.com.taodaji:id/item_view')
    wait(5)
    menulist[1].click()
    wait(10)
    # 点击第一个订单详情
    menulist = basic_variables.driver.find_elements_by_id('cn.com.taodaji:id/item_view')
    wait(5)
    menulist[1].click()
    wait(5)
    # 上滑
    up_swipe()
    wait(2)
    # 获取订单编号
    basic_variables.order_num = basic_variables.driver.find_element_by_id('cn.com.taodaji:id/order_no').get_attribute(
        'text')
    print ('order_num: ', basic_variables.order_num)
    # 返回
    basic_variables.driver.find_element_by_class_name('android.widget.ImageButton').click()
    wait(2)
    basic_variables.driver.find_element_by_class_name('android.widget.ImageButton').click()

    logout()


def deliver_food():
    # type: () -> object
    # step3 发货------------------------------------------------------------------------'''
    # 再次获取店铺供货款'''
    # 点击 我
    wait(5)
    menulist = basic_variables.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
    wait(5)
    menulist[4].click()

    # 供应商登录
    print ('supplier login...')
    wait(5)
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/myself_headportrait').click()
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/supplier_login').click()

    login(basic_variables.supplier_account['account'], basic_variables.supplier_account['psw'])

    # 获取供货款
    print('reading supplier money...')
    wait(2)
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/supply_money').click()
    basic_variables.supplier_money_sale = \
        basic_variables.driver.find_element_by_id('cn.com.taodaji:id/supplier_money').get_attribute('text')
    print('supplier_money_sale: ', basic_variables.supplier_money_sale)
    print('supplier_money_start: ', basic_variables.supplier_money_start)
    print('bill_money_before: ', basic_variables.bill_money_before)
    print('asserting money...')
    assert (float(basic_variables.supplier_money_sale) == (float(basic_variables.supplier_money_start) +
                                                           float(basic_variables.bill_money_before)))
    # 返回
    basic_variables.driver.find_element_by_class_name('android.widget.ImageButton').click()
    wait(2)

    print ('deliver goods...')
    # 点击“待确认”
    menulist = basic_variables.driver.find_elements_by_id('cn.com.taodaji:id/item_view')
    menulist[0].click()

    # 注意，订单详情中没有订单编号，所以无法确认第一个订单是否为买家下的订单
    # 因为没有订单编号，点击 确认发货 后，无法验证是否点击成功
    # 获取商品编号
    wait(3)
    # 点击第一个订单详情
    menulist = basic_variables.driver.find_elements_by_id('cn.com.taodaji:id/item_view')
    wait(5)
    menulist[1].click()
    wait(5)
    basic_variables.goods_num = basic_variables.driver.find_element_by_id('cn.com.taodaji:id/order_no').get_attribute(
        'text')
    print('goods_num:', basic_variables.goods_num)
    basic_variables.driver.find_element_by_class_name('android.widget.ImageButton').click()

    # 点击“确认发货”
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/order_ok').click()

    # 返回
    basic_variables.driver.find_element_by_class_name('android.widget.ImageButton').click()
    wait(2)

    # 退出店铺
    logout()


def print_bills():
    # step4 后台打印发货-------------------------------------------------------------------------'''
    print("server login...")
    basic_variables.chrome_driver = basic_variables.webdriver.Chrome()
    basic_variables.chrome_driver.maximize_window()
    basic_variables.chrome_driver.get(basic_variables.server_url)
    wait(5)
    elem = basic_variables.chrome_driver.find_element_by_name('loginName')
    elem.send_keys('admin')
    elem = basic_variables.chrome_driver.find_element_by_name('passwd')
    elem.send_keys('tdj999999')
    wait(10)
    elem = basic_variables.chrome_driver.find_element_by_class_name('y_btn1')
    elem.click()
    wait(30)

    print('deliver goods...')
    basic_variables.chrome_driver.switch_to.frame('left')
    elem = basic_variables.chrome_driver.find_element_by_class_name('kc')
    elem.click()
    wait(10)
    
    basic_variables.chrome_driver.switch_to.parent_frame()
    basic_variables.chrome_driver.switch_to.frame('right')
    elem = basic_variables.chrome_driver.find_element_by_id('qrCode')
    # debug，真实需屏蔽
    # basic_variables.goods_num = '9171227000386'
    elem.send_keys(basic_variables.goods_num)
    wait(10)
    elem = basic_variables.chrome_driver.find_element_by_css_selector('.inq_btn.inq_btn2.add_btn')
    elem.click()
    wait(2)
    try:
        elem = basic_variables.chrome_driver.find_element_by_css_selector('.rk_btn.b_orange.in_stock')
        elem.click()
        wait(2)

        # 验证
        data = basic_variables.chrome_driver.find_element_by_id('tipMsg').text
        print 'asserting...'
        assert (data == u'入库成功！')
        wait(10)
    except:
        wait(3)
        basic_variables.chrome_driver.switch_to_alert().accept()

    print('print goods...')
    basic_variables.chrome_driver.switch_to.parent_frame()
    basic_variables.chrome_driver.switch_to.frame('left')
    elem = basic_variables.chrome_driver.find_element_by_css_selector('.dd.menuSs')
    elem.click()
    elem = basic_variables.chrome_driver.find_element_by_id('ddgl_dy')
    elem.click()

    basic_variables.chrome_driver.switch_to.parent_frame()
    basic_variables.chrome_driver.switch_to.frame('right')
    basic_variables.chrome_driver.find_element_by_id('expectDeliveredDateQ').clear()
    elem = basic_variables.chrome_driver.find_element_by_css_selector('.inq_btn.inq_query')
    elem.click()
    wait(30)

    table = basic_variables.chrome_driver.find_element_by_id('printOrderTableInfo')
    table_rows = table.find_elements_by_tag_name('tr')
    table_len = len(table_rows)
    print('table lens: ', table_len)
    # debug
    # basic_variables.order_num = u'9600000416'
    for i in range(1, table_len):
        row_col3 = table_rows[i].find_elements_by_tag_name('td')[3].text
        print('col3: ', row_col3)
        if row_col3 == basic_variables.order_num:
            table_rows[i].find_elements_by_tag_name('td')[-1].find_elements_by_tag_name('input')[-1].click()
            wait(2)
            basic_variables.chrome_driver.switch_to_alert().accept()
            wait(2)
            break
    wait(5)
    basic_variables.chrome_driver.quit()
    return


def after_sales_start():
    # step5 终端申请售后-------------------------------------------------------------------------'''
    # debug
    # basic_variables.driver.quit()
    basic_variables.driver = basic_variables.appium_webdriver.Remote('http://localhost:4723/wd/hub',
                                                                     basic_variables.desired_caps)
    # 点击 我
    wait(5)
    menulist = basic_variables.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
    wait(5)
    menulist[4].click()

    # 采购商登录
    print ('client login...')
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/myself_headportrait').click()
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/purchaser_login').click()

    # 输入用户名密码
    login(basic_variables.buyer_account['account'], basic_variables.buyer_account['psw'])
    wait(2)

    # 确认收货
    # 点击 待收货
    menulist = basic_variables.driver.find_elements_by_id('cn.com.taodaji:id/item_view')
    wait(5)
    menulist[2].click()
    wait(5)
    elemlist = basic_variables.driver.find_elements_by_id('cn.com.taodaji:id/order_ok')
    wait(5)
    elemlist[0].click()
    wait(2)

    # 申请售后
    # 点击 待评价
    menulist = basic_variables.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
    wait(5)
    menulist[4].click()
    wait(5)
    elemlist = basic_variables.driver.find_elements_by_id('cn.com.taodaji:id/after_sales')
    wait(5)
    elemlist[0].click()
    wait(2)
    count = basic_variables.driver.find_element_by_id('cn.com.taodaji:id/count')
    count.send_keys('1')
    aftersales = basic_variables.driver.find_element_by_id('cn.com.taodaji:id/after_sales')
    aftersales.click()
    groupiterms = basic_variables.driver.find_elements_by_id('cn.com.taodaji:id/group_item')
    groupiterms[0].click()
    probtype = basic_variables.driver.find_element_by_id('cn.com.taodaji:id/problem_type')
    probtype.click()
    groupiterms = basic_variables.driver.find_elements_by_id('cn.com.taodaji:id/group_item')
    groupiterms[2].click()
    descrip = basic_variables.driver.find_element_by_id('cn.com.taodaji:id/description')
    descrip.send_keys('auto_test')
    up_swipe()
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/ok').click()

    # 采购商退出登录
    # 返回
    basic_variables.driver.find_element_by_class_name('android.widget.ImageButton').click()
    wait(2)

    logout()
    basic_variables.driver.quit()
    return


def after_sales_handle():
    # step6 后台处理售后------------------------------------------------------------------------'''
    print("server login...")
    basic_variables.chrome_driver = basic_variables.webdriver.Chrome()
    basic_variables.chrome_driver.maximize_window()
    basic_variables.chrome_driver.get(basic_variables.server_url)
    wait(5)
    elem = basic_variables.chrome_driver.find_element_by_name('loginName')
    elem.send_keys('admin')
    elem = basic_variables.chrome_driver.find_element_by_name('passwd')
    elem.send_keys('tdj999999')
    wait(5)
    elem = basic_variables.chrome_driver.find_element_by_class_name('y_btn1')
    elem.click()
    wait(30)

    print('after_sales_handle...')
    basic_variables.chrome_driver.switch_to.frame('left')
    elem = basic_variables.chrome_driver.find_element_by_class_name('tk')
    elem.click()
    wait(10)
    elem = basic_variables.chrome_driver.find_element_by_id('shgl_ddcl')
    elem.click()

    basic_variables.chrome_driver.switch_to.parent_frame()
    basic_variables.chrome_driver.switch_to.frame('right')
    table = basic_variables.chrome_driver.find_element_by_id('afterSalesProcessTableInfo')
    table_rows = table.find_elements_by_tag_name('tr')
    table_len = len(table_rows)
    print('table lens: ', table_len)
    # debug
    # basic_variables.goods_num = u'9180102000106'
    for i in range(1, table_len):
        row_col2 = table_rows[i].find_elements_by_tag_name('td')[2].text
        print('col2: ', row_col2)
        if row_col2 == basic_variables.goods_num:
            print(u'处理售后..')
            table_rows[i].find_elements_by_tag_name('td')[-1].find_elements_by_tag_name('input')[-1].click()
            wait(5)
            print(u'同意退款。。。')
            elem = basic_variables.chrome_driver.find_element_by_id('agreeRefundBtn')
            elem.click()
            wait(10)
            print(u'确认同意退款。。。')
            elem = basic_variables.chrome_driver.find_element_by_xpath('/html/body/div[7]/div/div/div[3]/button[1]')
            elem.click()
            wait(2)
            print(u'进度查询。。。')
            '''
            table_rows[i].find_elements_by_tag_name('td')[-1].find_elements_by_tag_name('input')[-1].click()
            wait(5)
            '''
            table2 = basic_variables.chrome_driver.find_element_by_id('afterSalesProcessTableInfo')
            table_rows2 = table2.find_elements_by_tag_name('tr')
            table_rows2[i].find_elements_by_tag_name('td')[-1].find_elements_by_tag_name('input')[-1].click()
            wait(3)
            print(u'退款成功。。。')
            basic_variables.chrome_driver.find_element_by_id('rechargeOKBtn').click()
            wait(10)
            print(u'同意完成售后。。。')
            elem = basic_variables.chrome_driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]')
            elem.click()
            wait(2)
            print(u'操作成功。。。')
            elem = basic_variables.chrome_driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button')
            elem.click()
            wait(2)
            print(u'返回。。。')
            basic_variables.chrome_driver.find_element_by_class_name('return_btn').click()
            wait(5)
            break
    wait(10)
    basic_variables.chrome_driver.quit()
    return


def buyer_check_done():
    # 采step8 购商验证-------------------------------------------------------------------------'''
    # debug
    # basic_variables.driver.quit()

    basic_variables.driver = basic_variables.appium_webdriver.Remote('http://localhost:4723/wd/hub',
                                                                     basic_variables.desired_caps)

    wait(5)
    menulist = basic_variables.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
    wait(5)
    menulist[4].click()

    # 采购商登录
    print ('client login...')
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/myself_headportrait').click()
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/purchaser_login').click()

    # 输入用户名密码
    login(basic_variables.buyer_account['account'], basic_variables.buyer_account['psw'])
    wait(2)

    # 获取余额
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/supply_money').click()
    buyer_money = \
        basic_variables.driver.find_element_by_id('cn.com.taodaji:id/supplier_money').get_attribute('text')
    print ('buyer_money: ', buyer_money)
    print ('last_money', basic_variables.last_money)
    print('bill_money_before', basic_variables.bill_money_before)
    print('asserting...')
    assert (
        (float(basic_variables.last_money) + float(basic_variables.bill_money_before)) == float(
            buyer_money))
    # 返回
    basic_variables.driver.find_element_by_class_name('android.widget.ImageButton').click()
    logout()
    return


def supplier_check_done():
    # step7 供货商验证-------------------------------------------------------------------------'''
    # 点击 我
    wait(5)
    menulist = basic_variables.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
    wait(2)
    menulist[4].click()

    # 供应商登录
    print ('supplier login...')
    wait(5)
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/myself_headportrait').click()
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/supplier_login').click()

    login(basic_variables.supplier_account['account'], basic_variables.supplier_account['psw'])

    # 获取供货款
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/supply_money').click()
    supplier_money = \
        basic_variables.driver.find_element_by_id('cn.com.taodaji:id/supplier_money').get_attribute('text')
    print('supplier_money: ', supplier_money)
    print('asserting...')
    print('supplier_money_sale', basic_variables.supplier_money_sale)
    print('bill_money_before', basic_variables.bill_money_before)
    assert (
        (float(basic_variables.supplier_money_sale) - float(basic_variables.bill_money_before)) == float(
            supplier_money))

    # 退出店铺
    # 返回
    basic_variables.driver.find_element_by_class_name('android.widget.ImageButton').click()
    wait(2)

    logout()
    basic_variables.driver.quit()
    return
