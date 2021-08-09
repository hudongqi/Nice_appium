from time import sleep
from appium import webdriver
import unittest
from Base import tools

desired_caps = {}
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '14.4'
desired_caps['deviceName'] = 'iPhone 12 Pro'
desired_caps['bundleId'] = 'com.KKGOO.kk'
# desired_caps['udid'] = '00008030-001664C43A99802E'
# desired_caps['newCommandTimeout'] = 600  # 1 hour
driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
sleep(2)
#driver.quit()
#driver.Remote(127)


class register_login():
    def __init__(self):
        self.mob = tools.mod

    def login(self):
        #driver.find_element_by_ios_predicate('name == "同意"').click()
        driver.find_element_by_ios_predicate('name == "登录"').click()
        driver.find_element_by_ios_predicate('name == "已有账号登录"').click()
        sleep(2)
        driver.find_element_by_ios_predicate('label == "+1"').click()
        #driver.tap([(376, 579)], 500)
        account = driver.find_element_by_ios_predicate('type == "XCUIElementTypeTextField"')
        sleep(2)
        value = account.text
        sleep(2)

        if value == None:
            account.send_keys(10179074836)

        elif value != '101 7907 4836':
            account.clear()
            account.send_keys(10179074836)
        #
        # sleep(3)
        driver.find_element_by_ios_predicate('type == "XCUIElementTypeSecureTextField"').set_value('123456')
        driver.find_element_by_ios_predicate('name == "登录"').click()

        driver.tap([(330, 395)], 500)
        driver.tap([(376,579)], 500)



    def register(self):
        try:
            driver.find_element_by_ios_predicate('label == "同意"').click()
        except Exception as e:
            print("except:",e)

        '''
        首页
        '''
        driver.find_element_by_ios_predicate('name == "登录"').click()
        sleep(2)

        '''
        注册登录页
        '''
        driver.find_element_by_ios_predicate('label == "手机号注册"').click()
        sleep(2)

        """
        设置账号和密码
        """
        driver.tap([(67,237)],500)
        sleep(2)
        driver.find_element_by_ios_predicate('label == "中国大陆 +86"').click()
        sleep(1)
        driver.find_element_by_ios_predicate('label == "中国大陆 +86"').click()


        account = driver.find_element_by_ios_predicate('type == "XCUIElementTypeTextField"')
        account.send_keys(self.mob)

        driver.find_element_by_ios_predicate('value == "请设置密码"').set_value('123456')
        sleep(2)
        driver.tap([(89,338)],500)
        sleep(2)
        driver.find_element_by_ios_predicate('label == "common checkbox middle normal"').click()
        sleep(2)
        driver.find_element_by_ios_predicate('label == "下一步"').click()

        '''
        验证手机号
        '''
        sleep(2)
        driver.find_element_by_ios_predicate('value == "请输入收到的验证码"').set_value(str(tools.base_tools().get_yanzhengma()))
        sleep(2)
        driver.find_element_by_ios_predicate('label == "下一步"').click()
        sleep(2)
        print(self.mob)

    def log_out(self):

        '''
        首页
        '''
        driver.find_element_by_ios_predicate('label == "我的"').click()
        sleep(1)
        driver.find_element_by_ios_predicate('label == "personage set icon"').click()
        sleep(1)
        driver.find_element_by_ios_predicate('label == "退出登录"').click()
        sleep(1)
        driver.find_element_by_ios_predicate('label == "退出登录" ').click()


if __name__ == '__main__':
     register_login().register()
     register_login().log_out()




