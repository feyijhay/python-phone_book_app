import unittest

from Mavericks import Phone_Book


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_add_contact(self):
        Phone_Book.add_contact("Moh", "23490189100")
        self.assertEqual(1, len.Phone_Book.contactName)
if __name__ == '__main__':
    unittest.main()
