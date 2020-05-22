import unittest
from function import *
from HTMLTestRunner import HTMLTestRunner
from BSTestRunner import BSTestRunner
import time
report_dir = './test_report'
test_dir = './test_case'

print('开始运行测试用例')
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_login.py')
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_dir+'/'+now+'result.html'
with open(report_name, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title="测试报告", description="登录测试报告")
    runner.run(discover)
    f.close()
latest_report=latest_report(report_dir)
print("发送邮件")
send_mail(latest_report)
print("测试完成")
