from model.contact import Contact
from random import randrange


def test_contact_firstname(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.contact_create(
            Contact(firstname="Сергей", middlename="Сергеевич", lastname="Сергеев", nickname="Серега",
                    address="г. Казань",
                    homephone="11111", mobile="22222",
                    work="333333", email="sergei@gmail.com", email2=111, email3=222, bday="", bmounth="May", byear="1975"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="aaaaaa", middlename="aaaaaaa", lastname="aaaaaaa", nickname="aaaaa", address="aaaaa",
                homephone="777777", mobile="77777",
                work="77777", email="se333@gmail.com", email2=33, email3=44, bday="", bmounth="", byear="1111")
    contact.id = old_contacts[index].id
    app.contact.contact_update_by_index(index, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_group_list(), key=Contact.id_or_max)

