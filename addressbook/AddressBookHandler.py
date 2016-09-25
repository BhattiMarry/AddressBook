# -*- coding: utf-8 -*-

'''

AddressBookHandler class.

This module provides the implementation of Address Book using AddressBook objects.

:copyright: (c) 2016 Umair Bhatti
:licence: Apache2, see LICENCE file for more details.

'''

from AddressBook import AddressBook

class AddressBookHandler():
    addressBook = []
    groups = []

    def __init__(self):
        addressBook = []
        groups = []

    def add_group(self, Group_Name):
        if Group_Name:
            AddressBookHandler.groups.append(Group_Name)

    def check_sublist(self, list1, list2):
        for item in list1:
            if item not in list2:
                return False
        return True

    def add_person(self, FirstName, LastName, StreetAddress, Email, Phone, Group):
        if Group:
            if isinstance(Group, list):
                if not self.check_sublist(Group, AddressBookHandler.groups):
                    print("Group name not found in group list. Add the group first.")
                    return
            else:
                if Group not in AddressBookHandler.groups:
                    print("Group name not found in group list. Add the group first.")
                    return
            
        obj = AddressBook(FirstName, LastName, StreetAddress, Email, Phone, Group)
        AddressBookHandler.addressBook.append(obj)

    def count_persons(self):
        len1 = len(AddressBookHandler.addressBook)
        print len1
        return len1

    def get_address_book(self):
        return AddressBookHandler.addressBook

    def clear_address_book(self):
        print 'Clearing address book entries...'
        AddressBookHandler.addressBook = []

    def clear_address_book_groups(self):
        print 'Clearing address book groups...'
        AddressBookHandler.groups = []

    def print_short_info(self, AddressBook):
        print "First Name: %s, Last Name: %s, Group: %s" %(AddressBook.fname, AddressBook.lname, AddressBook.group)

    def get_all_groups(self):
    	all_groups = AddressBookHandler.groups
    	print all_groups
        return all_groups

    def get_persons_in_group(self, GroupName):
        members = []
        if not GroupName:
            print "Error: `No group name specified.`"
            return
        all_groups = self.get_all_groups()

        if not all_groups and GroupName not in all_groups:
            print 'Error: `No group(s) registered with this name.`'
            return

        if not AddressBookHandler.addressBook:
            print "Address book is empty. Add some contacts first."
            return

        addr_book = self.get_address_book()
        for i in xrange(0, len(addr_book)):
            if GroupName in addr_book[i].group:
                self.print_short_info(addr_book[i])
                members.append(addr_book[i])

        if members:
            return members
        else:
            print 'No person in this group.'

    def print_person_info(self, AddressBook):
        print 'First Name       :   %s' %AddressBook.fname
        print 'Last Name        :   %s' %AddressBook.lname
        print 'Street Address   :   %s' %AddressBook.stAddress
        print 'Email Address    :   %s' %AddressBook.email
        print 'Phone Number     :   %s' %AddressBook.phone
        print 'Address Group    :   %s' %AddressBook.group

    def get_group_info_of_person(self, _fname):
        nameFlag = True
        groups = []
        addr_book = self.get_address_book()
        for i in xrange(0, len(addr_book)):
            if addr_book[i].fname == _fname:
                nameFlag = False
                self.print_short_info(addr_book[i])
                groups.append(addr_book[i].group)
        if nameFlag:
            print 'Error: `Name not found in the address book.`'
        else:
            return groups

    def get_person_info_by_name(self, Name):
        members = []
        _fname = None
        _lname = None
        if not Name:
            print 'Error: `No name given.`'
            return
        nameTokens = Name.split(' ')
        if len(nameTokens) > 1:
            _fname = (['', ' '][len(nameTokens) > 2]).join(nameTokens[:len(nameTokens) - 1])
            _lname = ''.join(nameTokens[len(nameTokens) - 1])

        addr_book = self.get_address_book()
        for i in xrange(0, len(addr_book)):
            if _fname and _lname:
                if _fname == addr_book[i].fname and _lname == addr_book[i].lname:
                    members.append(addr_book[i])
                    self.print_short_info(addr_book[i])
            else:
                if Name in [addr_book[i].fname, addr_book[i].lname]:
                    members.append(addr_book[i])
                    self.print_short_info(addr_book[i])
        if members:
            return members
        else:
            print 'Name not found in the address book.'

    def get_person_info_by_email(self, Email):
        eName = None
        members = []
        if not Email:
            print 'Error: `No email address provided to look for.`'
            return
        addr_book = self.get_address_book()
        for i in range(0, len(addr_book)):
            if isinstance(addr_book[i].email, str):
                if Email in addr_book[i].email:
                    self.print_short_info(addr_book[i])
                    members.append(addr_book[i])
            elif isinstance(addr_book[i].email, list):
                for email in addr_book[i].email:
                    if Email in item:
                        self.print_short_info(addr_book[i])
                        members.append(addr_book[i])
        if members:
            return members
        else:
            print 'No person with given email address.'
