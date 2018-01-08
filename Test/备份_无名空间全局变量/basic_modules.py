# coding=utf-8

from basic_variables import *


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


def up_swipe():

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
    # type: () -> object
    #上滑
    up_swipe()
    # 退出
    driver.find_element_by_id('cn.com.taodaji:id/login_out').click()
