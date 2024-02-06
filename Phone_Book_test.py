import unittest

from Mavericks import Phone_Book


class MyTestCase(unittest.TestCase):

    def setUp(self):
        Phone_Book.add_new_contact("Moh", "23490189100")
        Phone_Book.add_new_contact("Bolaji", "23411111111")
        Phone_Book.add_new_contact("Dayo", "23422222222")

    def tearDown(self):
        Phone_Book.contactName.clear()
        Phone_Book.contactPhoneNumber.clear()
    def test_add_new_contact(self):
        self.assertEqual(3, len(Phone_Book.contactName))
        Phone_Book.add_new_contact("Timi", "23433333333")
        self.assertEqual(4, len(Phone_Book.contactName))
        self.assertEqual(4, len(Phone_Book.contactPhoneNumber))

    def test_delete_contact(self):
        self.assertEqual(3, len(Phone_Book.contactName))
        self.assertEqual(3, len(Phone_Book.contactPhoneNumber))
        Phone_Book.delete_contact("Moh", "23490189100")
        self.assertEqual(2, len(Phone_Book.contactName))
        self.assertEqual(2, len(Phone_Book.contactPhoneNumber))

    def test_search_contact(self):
        self.assertEqual(3, len(Phone_Book.contactName))
        Phone_Book.search_contact("Dayo")
        self.assertEqual("Dayo", Phone_Book.search_contact("Dayo"))