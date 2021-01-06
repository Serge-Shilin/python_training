from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", address="",
                homephone="", mobile="",
                work="", fax="", mail="", bday="", bmounth="", byear="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20), lastname=random_string("lastname", 20), address=random_string("address", 30),
            homephone=random_string("homephone", 11), mobile=random_string("mobile", 12), work=random_string("work", 10), fax=random_string("fax", 10),
            mail=random_string("mail", 15))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_new_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.contact_create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)






