from AddressBookHandler import AddressBookHandler
obj = AddressBookHandler()

#adds a person group with the given name.
obj.add_group('Human')

#adds a person with given details.
obj.add_person('Umair', 'Bhatti', 'KHI', 'umair@marry.com', '5001676', 'Human')

obj.add_group('Alien')

obj.add_person('Jawad', 'Aslam', 'ISB', 'hafiz@jawad.com', '5519726', 'Alien')
obj.add_person('Saim', 'Ali', 'PDK', 'saim@don.com', '9872208', ['Human', 'Alien'])
obj.add_person('Ch', 'Uzair', 'RWP', 'malik@uzair.com', '5028140', 'Malik')

obj.add_group('Malik')

obj.add_person('Ch', 'Uzair', 'RWP', 'malik@uzair.com', '5028140', 'Malik')

#returns and prints the total number of persons in the address book.
obj.count_persons()

#returns and prints a list of groups in address book
obj.get_all_groups()

#returns and prints the list of person(s) matching with the given group name
obj.get_persons_in_group('Malik')
obj.get_persons_in_group('Alien')
obj.get_persons_in_group('Human')

#returns and prints a list of group(s) against a given first name
obj.get_group_info_of_person('Umair')

#returns and prints a list of person(s) matching with given name
obj.get_person_info_by_name('Ch')

#returns and prints a list of person matching the email given
person = obj.get_person_info_by_email('don.com')

obj.print_person_info(person[0])
