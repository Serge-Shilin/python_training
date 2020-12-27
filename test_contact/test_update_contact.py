from model.contact import Contact


def test_contact_firstname(app):
    old_contacts = app.contact.get_contacts_list()
    if app.contact.count() == 0:
        app.contact.contact_create(
            Contact(firstname="Сергей", middlename="Сергеевич", lastname="Сергеев", nickname="Серега",
                    address="г. Казань",
                    homephone="11111", mobile="22222",
                    workphone="333333", mail="sergei@gmail.com", bday="", bmounth="May", byear="1975"))
    app.contact.contact_update(
        Contact(firstname="aaaaaa", middlename="aaaaaaa", lastname="aaaaaaa", nickname="aaaaa", address="aaaaa",
                homephone="777777", mobile="77777",
                workphone="77777", mail="@", bday="", bmounth="", byear="1111"))
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)

def test_contact_update_lastname(app):
    old_contacts = app.contact.get_contacts_list()
    if app.contact.count() == 0:
        app.contact.contact_create(
            Contact(firstname="Сергей", middlename="Сергеевич", lastname="Сергеев", nickname="Серега",
                    address="г. Казань",
                    homephone="11111", mobile="22222",
                    workphone="333333", mail="sergei@gmail.com", bday="", bmounth="May", byear="1975"))
    app.contact.contact_update(
        Contact(firstname="sssssss", middlename="ssss", lastname="sssssss", nickname="sssssss", address="ssssss", homephone="99999", mobile="999999",
                workphone="99999", mail="@", byear="1901"))
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
