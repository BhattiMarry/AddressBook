========
Usage
========

To use AddressBook in a project::

A sample code can be found in SAMPLES directory. The code shows how to use this API.

    from addressbook import address_book_handler
    
    Obj = address_book_handler.AddressBookHandler()
    
    Obj.add_person(FirstName, LastName, Street_Address = [], Email = [], Phone = [], Group = [])
    
Its mandatory to add a group first before adding a person's info to the address book.

    Obj.add_group(GroupName)
