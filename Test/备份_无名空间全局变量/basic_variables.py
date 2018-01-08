# coding=utf-8

from appium import webdriver
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
#真实环境
supplier_account = {'account': '18571161280', 'psw': '111111', 'name': u'咪咪虾条'}
buyer_account = {'account': '18727120758', 'psw': '111111'}
"""
# 测试环境
supplier_account = {'account': '18924665240', 'psw': '111111', 'name': u'打烊了'}
buyer_account = {'account': '18727120758', 'psw': '111111'}

cmd0 = 'adb shell ime list -s'
cmd1 = 'adb shell settings get secure default_input_method'
cmd2 = 'adb shell ime set com.sohu.inputmethod.sogouoem/.SogouIME'
cmd3 = 'adb shell ime set io.appium.android.ime/.UnicodeIME'

desired_caps = {'platformName': 'Android', 'platformVersion': '5.1.1', 'deviceName': 'Android Emulator',
                'appPackage': 'cn.com.taodaji', 'appActivity': '.ui.activity.linkPage.StartActivity',
                'unicodeKeyboard': True, 'resetKeyboard': True}

supplier_money_start = 0
supplier_money_sale = 0
supplier_money_return = 0
bill_money = 0
buyer_money = 0
last_money = 0

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
