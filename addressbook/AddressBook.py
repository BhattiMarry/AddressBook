# -*- coding: utf-8 -*-
'''

AddressBook class.

This module provides the Address Book object containing very primary information of a person.

:copyright: (c) 2016 Umair Bhatti
:licence: Apache2, see LICENCE file for more details.

'''
class AddressBook(object):

    def __init__(self, FirstName, LastName, StreetAddress, Email, Phone, Group):
        self.fname = FirstName
        self.lname = LastName
        if StreetAddress:
            self.stAddress = StreetAddress
        else:
            self.stAddress = "N/A"

        if Email:
            self.email = Email
        else:
            self.email = "N/A"

        if Phone:
            self.phone = Phone
        else:
            self.phone = "N/A"

        if Group:
            self.group = Group
        else:
            self.group = "N/A"
