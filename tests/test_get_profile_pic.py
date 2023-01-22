import unittest
import basic_webscraper


class MyTestCase(unittest.TestCase):
    def test_something(self):
        username_test = 'arianitxyz'
        self.assertEqual(basic_webscraper.get_user_profile(username_test),
                         'https://avatars.githubusercontent.com/u/22275124?v=4')


if __name__ == '__main__':
    unittest.main()
