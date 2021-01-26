from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture


def test_remove_contact_in_group(app, db, check_ui):
    contact = Contact(firstname="Сергей", middlename="Сергеевич", lastname="Сергеев", nickname="Серега",
                       address="г. Казань",
                       homephone="11111", mobile="22222", fax="121212",
                       work="333333", email="sergei@gmail.com", email2=1212, email3=1221, bday="", bmounth="May",
                       byear="1975")
    app.contact.contact_create(contact)
    group = Group(name="11", footer="222", header="333")
    if app.group.count() == 0:
        app.group.group.create(group)
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    old_contacts_in_groups = db.get_contacts_in_group(Group(id=119))
    app.contact.select_none()
    app.contact.remove_contact_in_group()
    new_contacts = db.get_contacts_in_group(Group(id=119))
    assert len(old_contacts_in_groups) - 1 == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_group_list(), key=Contact.id_or_max)
