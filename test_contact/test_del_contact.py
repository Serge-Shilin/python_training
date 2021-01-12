
from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.contact_create(
            Contact(firstname="Сергей", middlename="Сергеевич", lastname="Сергеев", nickname="Серега",
                    address="г. Казань",
                    homephone="11111", mobile="22222", fax="121212",
                    work="333333", mail="sergei@gmail.com", bday="", bmounth="May", byear="1975"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.test_delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

