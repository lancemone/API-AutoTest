#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/13 下午6:39
# @Author  : motao
# @Site    : 
# @File    : unittest.py
# @Software: PyCharm


'''
单个测试用例管理
1、导入模块   import unittest
2、必须继承 unittest.TestCase
3、配置环境，主要是测试前的初始化工作，例如前置的参数赋值，数据库操作等
4、testcase，定义测试用例；定义assert断言，判断测试结果；testcase顺序执行
5、清理环境：tearDown,测试后的清除工作，比如参数的还原或销毁，数据库的数据清除与恢复
6、调用unittest.main()启动测试
'''
'''
assert断言：
assertEqual(a,b)/assertNotEqual(a,b)    a==b/a!=b
assertTrue(x)/assertFalse(x)   bool(x) is True/False
assertIs(a,b)/assertNot(a,b)    a is/is not b
assertNone(x)/assertNotNone(x)  x is None/Not None
assertIn(a,b)/assertNotIn(a,b)  a in/not in b
'''

'''
unittest模块的各个属性说明:
unittest.TestCase：TestCase类，所有测试用例类继承的基本类。可以方便的将一个单元测试模块变为可直接运行的测试脚本，main()方法使
用TestLoader类来搜索所有包含在该模块中以“test”命名开头的测试方法，并自动执行他们。执行方法的默认顺序是：根据ASCII码的顺序加载测
试用例，数字与字母的顺序为：0-9，A-Z，a-z。所以以A开头的测试用例方法会优先执行，以a开头会后执行。

unittest.TestSuite()：unittest框架的TestSuite()类是用来创建测试套件的。

unittest.TextTextRunner():unittest框架的TextTextRunner()类，通过该类下面的run()方法来运行suite所组装的测试用例，入参为suite测试套件。

unittest.defaultTestLoader(): defaultTestLoader()类，通过该类下面的discover()方法可自动更具测试目录start_dir匹配查找测试用例文
件（test*.py），并将查找到的测试用例组装到测试套件，因此可以直接通过run()方法执行discover，
用法：discover=unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

'''

# 导入模块
import unittest


# 定义测试类，继承自unittest.TestCase类
# 可继承unittest.TestCase的方法，如setUp和tearDown方法，不过此方法可以在子类重写，覆盖父类方法。
# 可继承unittest.TestCase的各种断言方法。
class Testcase_one(unittest.TestCase):
    def setUp(self):  # 环境配置
        print('/ncases before')
        pass

    def test_case_add(self):  # 定义测试用例
        print('add...')
        a = 3 + 4
        b = 7
        self.assertEqual(a, b, msg='a not euqal b')  # 定义断言

    def test_case_sub(self):
        print('sub...')
        a = 10 - 5
        b = 4
        self.assertEqual(a, b, msg='a not euqal b')

    def tearDown(self):
        print('case after')
        pass


# 执行测试用例
# 使用unittest.main方法会搜索该模块下所有以test开头的测试用例方法,并自动执行它们，执行顺序是命名顺序
if __name__ == '__main__':
    unittest.main()

# 执行测试用例方法2
# 先构造测试集
# 实例化测试套件
sunit = unittest.TestSuite()
# 将测试用例加载到测试套件中
# 执行顺序是安装加载顺序
sunit.addTest(Testcase_one('test_case_sub'))
sunit.addTest(Testcase_one('test_case_add'))
# 执行测试用例
# 实例化TextTestRunner类
runner = unittest.TextTestRunner()
# 使用run()方法运行测试套件
runner.run(sunit)

# 执行测试用例方法3
# 构造测试集（简化了方案二中先要创建测试套件然后再依次加载测试用例）
test_dir = '/Users/taomo/PycharmProjects/AutoTest/autotest_project/'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
# 执行测试用例
# 实例化TextTestRunner类
# 使用run()方法运行测试套件
runner.run(discover)
