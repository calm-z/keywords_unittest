# __**__ coding=utf-8 __**__
# 作者：calm_zn
# 日期：2021/3/26 11:34
# 工具：PyCharm
# Python版本：3.7

import unittest
from excute.mfb_web.course_list import Course_list
from unittestreport import TestRunner
import time


class MFB_suites():
    suite = unittest.TestSuite()
    # 1.添加用例到套件中：添加单个测试用例，通过用例的名称进行添加
    # suite.addTest(Course_list('test_01'))
    # suite.addTest(Course_list('test_02'))
    # 2.批量添加用例到套件:一次性添加多个测试用例，通过用例集合来进行添加
    # cases = [Course_list('test_02'),Course_list('test_03')]
    # suite.addTests(cases)
    # 3.批量添加测试用例:通过TestCase对象直接添加一整个UnitTest类
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Course_list))
    # 4.批量添加测试用例：通过类名来进行添加
    # suite.addTests(unittest.TestLoader().loadTestsFromName('excute.mfb_web.course_list.Course_list'))
    # 5.批量添加测试用例：通过文件名来添加
    # 定义获取用例的路径
    case_dir = './excute/mfb_web/'
    # 基于路径来找用例，组合成套件
    discover = unittest.defaultTestLoader.discover(start_dir=case_dir, pattern='*.py')
    filename = 'mfb_web' + time.strftime("%Y-%m-%d", time.localtime())

    # 使用unittestreport中的testrunner进行运行测试套件，并生成测试报告
    runner = TestRunner(discover,
                        filename=filename + '.html',
                        report_dir="./reports/",
                        title='测试报告',
                        tester='赵宁',
                        desc="满分班web项目测试生成的报告",
                        templates=1)
    runner.run()
    runner.send_email(host="smtp.qq.com", port=465, user="305321378@qq.com", password="orqxgfynxcavbjbi", to_addrs="calmz@foxmail.com")


if __name__ == '__main__':
    MFB_suites()
