import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_equal(self):
        tenant_id = "7e04d72e14f827e77fe7dac3e70b5183"
        self.assertEqual("0be78e4d0a913ee5ea05dad9b96c0c35", tenant_id)
        with self.assertRaises(TypeError):
            print("err")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
