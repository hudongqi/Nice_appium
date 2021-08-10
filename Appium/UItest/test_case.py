import unittest
from Base import create_file
import HTMLTestRunnerCN


class Uitest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('start')
    @classmethod
    def tearDownClass(cls) -> None:
        print('end')

    @unittest.skip(" 无业务逻辑不展示 ")
    def test_case1(self):

        self.assertEquals(1,1),'true'


    def make_html(self):
        res_file = create_file.make_file()
        with open(res_file, 'wb') as fp:
            runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='业务流程执行报告', verbosity=2, description='测试测试',
                                                     tester='hudongqi')

            '''
            只是框架，不写具体业务测试逻辑
            '''
            # runner.run(suite())
        return res_file
