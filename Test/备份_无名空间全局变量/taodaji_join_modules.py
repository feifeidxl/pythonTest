#coding=utf-8

from business_modules import *

'''TODO
获取alert 内容，降低selenuum 版本为3.3.1 pip install selenium==3.3.1
总结python appium 搭建环境，及用例步骤
'''

'''
执行前注意：
退出账号，打开供应商店铺，屏蔽短信提醒
采购商账号余额应足够买菜
'''

print ('---open_shop---')
open_shop()
print ('---buy_food---')
buy_food()
print ('---deliver_food---')
deliver_food()
print ('---print_bills---')
print_bills()
print ('---after_sales_start---')
after_sales_start()
print ('---after_sales_handle---')
after_sales_handle()
print ('---buyer_check_done---')
buyer_check_done()
print ('---supplier_check_done---')
supplier_check_done()

