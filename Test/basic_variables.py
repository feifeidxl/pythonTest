# coding=utf-8

from appium import webdriver as appium_webdriver
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

"""
#真实环境
supplier_account = {'account': '18571161280', 'psw': '111111', 'name': u'咪咪虾条'}
buyer_account = {'account': '18727120758', 'psw': '111111'}
server_url = 'http://admin.taodaji.com.cn/businessCenter/login.html'
"""
# 测试环境
supplier_account = {'account': '18924665240', 'psw': '111111', 'name': u'打烊了'}
buyer_account = {'account': '18924665240', 'psw': '111111'}
server_url = 'http://test.51taodj.com/businessCenter/login.html'

cmd0 = 'adb shell ime list -s'
cmd1 = 'adb shell settings get secure default_input_method'
cmd2 = 'adb shell ime set com.sohu.inputmethod.sogouoem/.SogouIME'
cmd3 = 'adb shell ime set io.appium.android.ime/.UnicodeIME'

desired_caps = {'platformName': 'Android', 'platformVersion': '5.1.1', 'deviceName': 'Android Emulator',
                'appPackage': 'cn.com.taodaji', 'appActivity': '.ui.activity.linkPage.StartActivity',
                'unicodeKeyboard': True, 'resetKeyboard': True}

supplier_money_start = 0    # 初始供货款
supplier_money_sale = 0     # 加上订单金额后的供货款
# supplier_money_return = 0
bill_money_before = 0   # 商品总价
bill_money_after = 0    # 订单金额
buyer_money = 0     # 支付前的余额
last_money = 0  # 支付后的余额
goods_num = 0
order_num = 0

driver = appium_webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

chrome_driver = None
