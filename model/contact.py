

class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, address=None, homephone=None, mobile=None, workphone=None, mail=None, bday=None, bmounth=None, byear=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.address = address
        self.homephone = homephone
        self.mobile = mobile
        self.workphone = workphone
        self.mail = mail
        self.bday = bday
        self.bmounth = bmounth
        self.byear = byear
        self.id = id

    def __repr__(self):
            return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
            return self.id == other.id and self.firstname == other.firstname
