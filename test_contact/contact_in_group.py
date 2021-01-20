from model.contact import Contact


def test_add_contact_in_group(app, db, check_ui):
    app.contact.contact_create(
           Contact(firstname="Сергей", middlename="Сергеевич", lastname="Сергеев", nickname="Серега",
                    address="г. Казань",
                    homephone="11111", mobile="22222", fax="121212",
                    work="333333", email="sergei@gmail.com", email2=1212, email3=1221, bday="", bmounth="May", byear="1975"))
    app.contact.select_none()
    old_contacts = db.get_groups_contact_list()
    app.contact.add_contact_in_group()
    new_contacts = db.get_groups_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_group_list(), key=Contact.id_or_max)


def test_remove_contact_in_group(app, db, check_ui):
    app.contact.contact_create(
           Contact(firstname="Сергей", middlename="Сергеевич", lastname="Сергеев", nickname="Серега",
                    address="г. Казань",
                    homephone="11111", mobile="22222", fax="121212",
                    work="333333", email="sergei@gmail.com", email2=1212, email3=1221, bday="", bmounth="May", byear="1975"))
    app.contact.select_none()
    old_contacts = db.get_groups_contact_list()
    app.contact.remove_contact_in_group()
    new_contacts = db.get_groups_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_group_list(), key=Contact.id_or_max)
