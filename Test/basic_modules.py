# coding=utf-8

# from basic_variables import *
import basic_variables


def enable_sougou():
    print (basic_variables.cmd2)
    basic_variables.os.system(basic_variables.cmd2)


def enable_unicode():
    basic_variables.os.system(basic_variables.cmd3)


def login(name, psw):
    enable_sougou()
    wait(2)
    phone = basic_variables.driver.find_element_by_id('cn.com.taodaji:id/username_edit')
    phone.send_keys(name)
    psd = basic_variables.driver.find_element_by_id('cn.com.taodaji:id/password_edit')
    psd.send_keys(psw)
    wait(5)
    basic_variables.driver.hide_keyboard()
    btn = basic_variables.driver.find_element_by_id('cn.com.taodaji:id/login_button')
    btn.click()


def up_swipe():
    # 上滑
    basic_variables.driver.swipe(int(basic_variables.driver.get_window_size()['width'] * 0.5),
                                 int(basic_variables.driver.get_window_size()['height'] * 0.9),
                                 int(basic_variables.driver.get_window_size()['width'] * 0.5),
                                 int(basic_variables.driver.get_window_size()['height'] * 0.2))


def logout():
    # type: () -> object
    # 上滑
    up_swipe()
    # 退出
    basic_variables.driver.find_element_by_id('cn.com.taodaji:id/login_out').click()


def wait(sec):
    print('waiting...')
    basic_variables.time.sleep(sec)
