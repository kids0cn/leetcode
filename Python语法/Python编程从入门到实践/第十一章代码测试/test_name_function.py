import unittest # 导入测试模块
from name_function import get_formatted_name # 导入要测试的函数

class NameTestCase(unittest.TestCase): # 该类包含一系列要测试的单元
    '''测试name_function.py'''
    def test_first_last_name(self): # 所有的方法必须以test打头，才能被自动执行
        formatted_name = get_formatted_name('kuki','kids')
        self.assertEqual(formatted_name,'Kuki Kids')
    
    def test_first_last_middle_name(self):
        formated_name = get_formatted_name('kuki','kids','k')
        self.assertEqual(formated_name,"Kuki K Kids")

unittest.main()