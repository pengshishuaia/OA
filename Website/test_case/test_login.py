import unittest
from Model import function, myunit, readExcel
from page_object.LoginPage import *
from time import sleep
from readExcel import *


class LoginTest(myunit.StartEnd):
    def test_login_normal1(self):
        '''输入正确的账号密码'''
        print('test_login_normal is start test...')
        # 文件的绝对路径
        data_path = "C:/Users/pengshaui/PycharmProjects/OA/login.xlsx"
        # sheet名称
        sheetname = "登录账户"
        # 定义get_data对象
        get_data = ExcelData(data_path, sheetname)
        # 读取Excel中的数据
        login_user = get_data.readExcel()
        # print(login_user)
        role = "中心秘书"
        # 等到角色为role的数组
        xinx = get_data.rendUser(login_user, role)
        # print(xinx)
        username = xinx[0]
        password = xinx[1]
        po = LoginPage(self.driver)
        po.login_action(username, password)
        sleep(3)
        self.assertEqual(po.type_login_pass(), '待办文件')
        function.insert_img(self.driver, '登录成功.png')
        print('test_login_normal test end!')

    def test_login_norma2(self):
        '''输入错误的账号密码'''
        print('test_login_normal is start test...')
        po = LoginPage(self.driver)
        po.login_action('00321310', '111112')
        sleep(3)
        self.assertEqual(po.type_login_fail(), '')
        function.insert_img(self.driver, '登录失败.png')
        print('test_login_normal test end!')


if __name__ == '__main__':
    unittest.main()
