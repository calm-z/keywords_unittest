# __**__ coding=utf-8 __**__
# 作者：calm_zn
# 日期：2021/3/25 16:09
# 工具：PyCharm
# Python版本：3.7

import unittest
from keywords.keywords import Keywords
from ddt import ddt, file_data

@ddt
class Course_list(unittest.TestCase):
    """
    mfb_web类用于管理满分班web项目的测试用例
    """

    def setUp(self) -> None:
        self.wk = Keywords('Chrome')

    def tearDown(self) -> None:
        self.wk.quit()

    # 实现电商登录流程
    @file_data('F:/keywords_unittest/case_yaml/mfb_web/course-list/login.yaml')
    def test_01(self, **kwargs):
        """
        方法用于
        """
        self.wk.visit(kwargs['url'])
        self.wk.click(**kwargs['login_button'])
        self.wk.input(**kwargs['mobile'])
        self.wk.input(**kwargs['code'])
        self.wk.click(**kwargs['confirm_button'])
        self.wk.sleep(kwargs['sleep'])
        el = self.wk.explicit_wait(**kwargs['assert'])
        self.assertTrue(el)

    def test_02(self):
        print('这是第二个测试用例')

    def test_03(self):
        print('这是第三个测试用例')



if __name__ == '__main__':
    unittest.main()
