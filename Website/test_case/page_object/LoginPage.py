from BasePage import *
from selenium.webdriver.common.by import By


# 登录操作

# 元素的封装
class LoginPage(Page):
    url = '/'

    username_loc = (By.NAME, 'userName')
    userPass_loc = (By.NAME, 'userPass')
    submit_loc = (By.XPATH, '/html/body/div/div[1]/div/form/button')

    def type_username(self, username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_userPass(self, userPass):
        self.find_element(*self.userPass_loc).clear()
        self.find_element(*self.userPass_loc).send_keys(userPass)

    def type_submit(self):
        self.find_element(*self.submit_loc).click()

    # 操作的封装
    def login_action(self, username, userPass):
        self.open()
        self.type_username(username)
        self.type_userPass(userPass)
        self.type_submit()

    loginpass_loc = (By.XPATH, '//*[@id="editor-tabs"]/div[1]/div[1]/div/ul/li/a/span')
    loginfail_Loc = (By.NAME, "userName")

    # 登录成功获取的元素
    def type_login_pass(self):
        return self.find_element(*self.loginpass_loc).text

    # 登录失败获取的元素
    def type_login_fail(self):
        return self.find_element(*self.loginfail_Loc).text
