'''
中心秘书拟稿提交中心领导
'''
from LoginPage import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Model import function, myunit
from page_object.LoginPage import *
from selenium.webdriver.support.ui import Select


class ArticleTest(LoginPage):
    # 元素定位
    # 一级菜单
    first_menu_loc = (By.XPATH, "//ul[@id='expmenu-freebie']/li/ul/li[2]/div")
    # 二级菜单
    secondary_menu_loc = (By.LINK_TEXT, "台内行文拟稿")
    # 定位标题元素
    title_loc = (By.XPATH, '//*[@id="title"]')
    # 定位承办人元素
    reportusername_loc = (By.ID, "reportusername")
    # 点位联系电话元素
    tel_loc = (By.ID, "tel")
    # 定位呈报单位
    applyUserDept_temp_loc = (By.ID, "applyUserDept_temp")
    # 定位提交按钮元素
    tijiao_loc = (By.ID, "tijiao")
    # 定位选择中心领导元素
    choice_loc = (By.LINK_TEXT, "中心领导/总监")
    # 定位搜素框元素
    search_loc = (By.NAME, "_username")
    # 定位搜索按钮元素
    search_button_loc = (By.XPATH, '//*[@id="searchForm"]/div/div[3]/div/span/button')
    # 定位单选按钮元素
    radio_button_loc = (By.XPATH, '/html/body/div/div/div/div/div/div[1]/table[2]/tbody/tr/td[1]/div/ins')
    # 定位确定按钮元素
    userChooseCheck_loc = (By.ID, "userChooseCheck")

    # 点击一级菜单
    def type_first_menu(self):
        self.driver.find_element(*self.first_menu_loc).click()

    # 点击二级菜单
    def type_secondary_menu(self):
        self.driver.find_element(*self.secondary_menu_loc).click()

    # 标题文本框输入内容
    def type_title(self):
        self.driver.find_element(*self.title_loc).send_keys("公文测试002")

    # 承办人文本框输入内容
    def type_reportusername(self):
        self.driver.find_element(*self.reportusername_loc).send_keys("彭帅")

    # 联系电话文本框输入内容
    def type_tel(self):
        self.driver.find_element(*self.tel_loc).send_keys("85068083")

    # 呈报单位时下拉框，选择想要的呈报单位
    def type_applyUserDept_temp(self):
        Select(self.driver.find_element(*self.applyUserDept_temp_loc)). \
            select_by_visible_text("总台技术局")

    # 点击提交操作按钮
    def type_tijiao(self):
        self.driver.find_element(*self.tijiao_loc).click()

    # 选择中心领导点击提交
    def type_choice(self):
        self.driver.find_element(*self.choice_loc).click()

    # 点击搜素文本框，输入搜素内容
    def type_search(self):
        self.driver.find_element(*self.search_loc).send_keys("徐进")

    # 点击搜索按钮进行搜索
    def type_search_button(self):
        self.driver.find_element(*self.search_button_loc).click()

    # 搜索处结果后，点击单选按钮
    def type_radion_button(self):
        self.driver.find_element(*self.radio_button_loc).click()

    # 选择之后，点击确定按钮
    def type_userChooseCheck(self):
        self.driver.find_element(*self.userChooseCheck_loc).click()

    def click_menu(self):
        self.type_first_menu()
        self.type_secondary_menu()
        sleep(5)
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.frame(1)
        sleep(5)
        self.type_title()
        self.type_reportusername()
        self.type_tel()
        self.type_applyUserDept_temp()
        self.type_tijiao()
        self.type_choice()
        windows = self.driver.current_window_handle  # 定位当前页面句柄
        all_handles = self.driver.window_handles  # 获取全部页面句柄
        for handle in all_handles:  # 遍历全部页面句柄
            if handle != windows:  # 判断条件
                self.driver.switch_to.window(handle)  # 切换到新页面
        sleep(3)
        self.type_search()
        self.type_search_button()
        self.type_radion_button()
        self.type_userChooseCheck()
        self.driver.switch_to.alert.accept()
