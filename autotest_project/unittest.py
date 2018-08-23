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

unittest.skip():装饰器，当运行用例时，有些用例可能不想执行等，可用装饰器暂时屏蔽该条测试用例。一种常见的用法就是比如说想调试某一个测试用例，想先屏蔽其他用例就可以用装饰器屏蔽。
@unittest.skip(reason): skip(reason)装饰器：无条件跳过装饰的测试，并说明跳过测试的原因。
@unittest.skipIf(reason): skipIf(condition,reason)装饰器：条件为真时，跳过装饰的测试，并说明跳过测试的原因。
@unittest.skipUnless(reason): skipUnless(condition,reason)装饰器：条件为假时，跳过装饰的测试，并说明跳过测试的原因。
@unittest.expectedFailure(): expectedFailure()测试标记为失败。

'''

'''
TestCase类的属性如下：
['__call__', '__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_addSkip', '_baseAssertEqual', '_classSetupFailed', '_deprecate', '_diffThreshold', '_formatMessage', '_getAssertEqualityFunc', '_truncateMessage', 'addCleanup', 'addTypeEqualityFunc', 'assertAlmostEqual', 'assertAlmostEquals', 'assertDictContainsSubset', 'assertDictEqual', 'assertEqual', 'assertEquals', 'assertFalse', 'assertGreater', 'assertGreaterEqual', 'assertIn', 'assertIs', 'assertIsInstance', 'assertIsNone', 'assertIsNot', 'assertIsNotNone', 'assertItemsEqual', 'assertLess', 'assertLessEqual', 'assertListEqual', 'assertMultiLineEqual', 'assertNotAlmostEqual', 'assertNotAlmostEquals', 'assertNotEqual', 'assertNotEquals', 'assertNotIn', 'assertNotIsInstance', 'assertNotRegexpMatches', 'assertRaises', 'assertRaisesRegexp', 'assertRegexpMatches', 'assertSequenceEqual', 'assertSetEqual', 'assertTrue', 'assertTupleEqual', 'assert_', 'countTestCases', 'debug', 'defaultTestResult', 'doCleanups', 'fail', 'failIf', 'failIfAlmostEqual', 'failIfEqual', 'failUnless', 'failUnlessAlmostEqual', 'failUnlessEqual', 'failUnlessRaises', 'failureException', 'id', 'longMessage', 'maxDiff', 'run', 'setUp', 'setUpClass', 'shortDescription', 'skipTest', 'tearDown', 'tearDownClass']

说明：

setUp():setUp()方法用于测试用例执行前的初始化工作。如测试用例中需要访问数据库，可以在setUp中建立数据库连接并进行初始化。如测试用例需要登录web，可以先实例化浏览器。

tearDown():tearDown()方法用于测试用例执行之后的善后工作。如关闭数据库连接。关闭浏览器。

assert*():一些断言方法：在执行测试用例的过程中，最终用例是否执行通过，是通过判断测试得到的实际结果和预期结果是否相等决定的。

assertEqual(a,b，[msg='测试失败时打印的信息']):断言a和b是否相等，相等则测试用例通过。

assertNotEqual(a,b，[msg='测试失败时打印的信息']):断言a和b是否相等，不相等则测试用例通过。

assertTrue(x，[msg='测试失败时打印的信息'])：断言x是否True，是True则测试用例通过。

assertFalse(x，[msg='测试失败时打印的信息'])：断言x是否False，是False则测试用例通过。

assertIs(a,b，[msg='测试失败时打印的信息']):断言a是否是b，是则测试用例通过。

assertNotIs(a,b，[msg='测试失败时打印的信息']):断言a是否是b，不是则测试用例通过。

assertIsNone(x，[msg='测试失败时打印的信息'])：断言x是否None，是None则测试用例通过。

assertIsNotNone(x，[msg='测试失败时打印的信息'])：断言x是否None，不是None则测试用例通过。

assertIn(a,b，[msg='测试失败时打印的信息'])：断言a是否在b中，在b中则测试用例通过。

assertNotIn(a,b，[msg='测试失败时打印的信息'])：断言a是否在b中，不在b中则测试用例通过。

assertIsInstance(a,b，[msg='测试失败时打印的信息'])：断言a是是b的一个实例，是则测试用例通过。

assertNotIsInstance(a,b，[msg='测试失败时打印的信息'])：断言a是是b的一个实例，不是则测试用例通过。
'''

'''
TestSuite类的属性如下：（组织用例时需要用到）

['__call__', '__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__iter__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_addClassOrModuleLevelException', '_get_previous_module', '_handleClassSetUp', '_handleModuleFixture', '_handleModuleTearDown', '_tearDownPreviousClass', '_tests', 'addTest', 'addTests', 'countTestCases', 'debug', 'run']

说明：

addTest(): addTest()方法是将测试用例添加到测试套件中，如下方，是将test_baidu模块下的BaiduTest类下的test_baidu测试用例添加到测试套件。

suite = unittest.TestSuite()
suite.addTest(test_baidu.BaiduTest('test_baidu'))
'''

'''
TextTextRunner的属性如下：（组织用例时需要用到）

['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_makeResult', 'buffer', 'descriptions', 'failfast', 'resultclass', 'run', 'stream', 'verbosity']

说明：
run(): run()方法是运行测试套件的测试用例，入参为suite测试套件。
'''
# 导入模块
import unittest


# 定义测试类，继承自unittest.TestCase类
# 可继承unittest.TestCase的方法，如setUp和tearDown方法，不过此方法可以在子类重写，覆盖父类方法。
# 可继承unittest.TestCase的各种断言方法。
# 整个文件的开始和结束执行
def setUpModule():
    print("test module start >>>>>>>>>>>>>>")


def tearDownModule():
    print("test module end >>>>>>>>>>>>>>")

class Testcase_one(unittest.TestCase):

    # 整个Test类的开始和结束执行
    @classmethod
    def setUpClass(cls):
        print("test class start =======>")

    @classmethod
    def tearDownClass(cls):
        print("test class end =======>")

    # 每个用例的开始和结束执行
    def setUp(self):  # 环境配置
        print('/ncases before')
        pass

    def tearDown(self):
        print('case after')
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
