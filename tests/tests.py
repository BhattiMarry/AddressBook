import unittest
from AddressBook import AddressBook
from AddressBookHandler import AddressBookHandler

class AddressBookTests(unittest.TestCase):
    def setUp(self):
        self.obj = AddressBookHandler()

    def test_address_book_object(self):
        assert not AddressBook("Umair", "Bhatti", "GHQ", "marry@smart.com", "5001676", "Human") == None

    def test_add_group(self):
        self.obj.add_group('Human')

    def test_add_person(self):
        self.obj.add_person("Jawad", "Aslam", "PDK", "jawad@hafiz.com", "5519726", "Human")
        assert self.obj.count_persons() > 0

        self.obj.add_person("Umair", "Bhatti", "GHQ", "marry@smart.com", "5001676", "Human")
        assert self.obj.count_persons() == 2

    def test_get_address_book(self):
        assert type(self.obj.get_address_book()) == list

    def test_ptrint_short_info(self):
        allPersons = self.obj.get_address_book()
        if len(allPersons) > 0:
            self.obj.print_short_info(allPersons[0])

    def test_get_persons_in_group(self):
        allGroups = self.obj.get_all_groups()
        if len(allGroups) > 0:
            self.obj.get_persons_in_group(self.obj.get_all_groups()[0])
        else:
            self.obj.get_persons_in_group("Default")

    def test_print_person_info(self):
        allPersons = self.obj.get_address_book()
        if len(allPersons) > 0:
            self.obj.print_person_info(allPersons[0])

    def test_get_group_info_of_person(self):
        allPersons = self.obj.get_address_book()
        if len(allPersons) > 0:
            self.obj.get_group_info_of_person(allPersons[0].fname)

    def test_get_person_info_by_name(self):
        allPersons = self.obj.get_address_book()
        if len(allPersons) > 0:
            self.obj.get_person_info_by_name(allPersons[0].fname)

    def test_get_person_info_by_email(self):
        allPersons = self.obj.get_address_book()
        if len(allPersons) > 0:
            self.obj.get_person_info_by_name(allPersons[0].email)

    def tearDown(self):
        self.obj = None

if __name__ == '__main__':
    unittest.main()
