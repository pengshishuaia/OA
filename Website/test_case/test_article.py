import unittest
from Model import function,myunit
from page_object.LoginPage import *
from page_object.ArticlePage import *
from time import sleep

class LoginTest(myunit.StartEnd):
    def test_article_normal(self):
        print('test_login_normal is start test...')
        po = LoginPage(self.driver)
        po.login_action("00000554",'123456')
        sleep(3)
        po1 = ArticleTest(self.driver)
        po1.click_menu()
        print('test_login_normal test end!')


if __name__ == '__main__':
    unittest.main()

