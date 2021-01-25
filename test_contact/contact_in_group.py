from model.contact import Contact
from model.group import Group
import re


def test_add_contact_in_group(app, orm, check_ui):
    contact = Contact(firstname="Сергей", middlename="Сергеевич", lastname="Сергеев", nickname="Серега",
                       address="г. Казань",
                       homephone="11111", mobile="22222", fax="121212",
                       work="333333", email="sergei@gmail.com", email2=1212, email3=1221, bday="", bmounth="May",
                       byear="1975")
    if app.contact.count() == 0:
        app.contact.contact_create(contact)
    group_create = Group(name="11", footer="222", header="333")
    if app.group.count() == 0:
        app.group.group.create(group_create)
    group_id = orm.get_group_list()
    old_contacts_in_groups = orm.get_contacts_in_group(group_id)
    app.contact.select_none()
    app.contact.add_contact_in_group()
    new_contacts = orm.get_contacts_in_group()
    assert len(old_contacts_in_groups) + 1 == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_group_list(), key=Contact.id_or_max)


def test_remove_contact_in_group(app, orm, check_ui):
    contact = Contact(firstname="Сергей", middlename="Сергеевич", lastname="Сергеев", nickname="Серега",
                       address="г. Казань",
                       homephone="11111", mobile="22222", fax="121212",
                       work="333333", email="sergei@gmail.com", email2=1212, email3=1221, bday="", bmounth="May",
                       byear="1975")
    if app.contact.count() == 0:
        app.contact.contact_create(contact)
    group = Group(name="11", footer="222", header="333")
    if app.group.count() == 0:
        app.group.group.create(group)
    app.contact.select_none()
    old_contacts = orm.get_contacts_in_group()
    app.contact.remove_contact_in_group()
    new_contacts = orm.get_contacts_in_group()
    assert len(old_contacts) - 1 == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_group_list(), key=Contact.id_or_max)
