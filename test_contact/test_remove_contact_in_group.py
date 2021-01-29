from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture


def test_remove_contact_in_group(app, db, check_ui):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    contact = Contact(firstname="Сергей", middlename="Сергеевич", lastname="Сергеев", nickname="Серега",
                       address="г. Казань",
                       homephone="11111", mobile="22222", fax="121212",
                       work="333333", email="sergei@gmail.com", email2=1212, email3=1221, bday="", bmounth="May",
                       byear="1975")
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_contact_list_not_group()) == 0:
        app.contact.contact_create(contact)
        app.contact.select_none()
        app.contact.add_contact_in_group()
    g = db.get_group_list()[0]
    old_contacts_in_groups = db.get_contacts_in_group(g)
    app.contact.select_none()
    app.contact.remove_contact_in_group()
    new_contacts = db.get_contacts_in_group(g)
    assert len(old_contacts_in_groups) - 1 == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_group_list(), key=Contact.id_or_max)


