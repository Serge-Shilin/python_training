
from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, address=None, homephone=None, mobile=None, work=None, fax=None,  mail=None, bday=None, bmounth=None, byear=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.address = address
        self.homephone = homephone
        self.mobile = mobile
        self.fax = fax
        self.work = work
        self.mail = mail
        self.bday = bday
        self.bmounth = bmounth
        self.byear = byear
        self.id = id

    def __repr__(self):
        return "%s : %s : %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

