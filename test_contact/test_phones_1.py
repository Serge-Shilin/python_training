from model.contact import Contact
import re
from random import randrange


def test_contact_info_home_vs_db(app, db):
    if app.contact.count() == 0:
        app.contact.contact_create(
            Contact(firstname="Сергей", middlename="Сергеевич", lastname="Сергеев", nickname="Серега",
                    address="г. Казань",
                    homephone="11111", mobile="22222", fax="121212",
                    work="333333", email="sergei@gmail.com", email2=1212, email3=1221, bday="", bmounth="May", byear="1975"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Иван", middlename="Иванович", lastname="Иванов",
                                   homephone="111", mobile="111", work="111",
                                   address="Казань",
                                   fax="111", email="111u", email2="111",
                                   email3="111"))
    contact_from_home_page = app.contact.get_contacts_list()
    contact_from_db = db.get_contact_list()
    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(contact_from_db, key=Contact.id_or_max)


def test_contact_info_home_vs_edit(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Иван", middlename="Иванович", lastname="Иванов",
                                   homephone="111", mobile="111", work="111",
                                   address="Казань",
                                   fax="111", email="111u", email2="111",
                                   email3="111"))
    list_contacts = app.contact.get_contacts_list()
    index = randrange(len(list_contacts))
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_from_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_from_home_page(contact_from_edit_page)


def test_contact_info_home_vs_view(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Иван", middlename="Иванович", lastname="Иванов",
                                   homephone="111", mobile="111", work="111",
                                   address="Казань",
                                   fax="111", email="111u", email2="111",
                                   email3="111"))
    list_contacts = app.contact.get_contacts_list()
    index = randrange(len(list_contacts))
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.fax == contact_from_edit_page.fax


def clear(s):
    return re.sub("[./() -]", "", s)


def merge_phones_like_from_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobile, contact.work, contact.fax]))))


def merge_emails_like_from_home_page(contact):
    return "\n".join(filter(lambda x: x != "" and x is not None, [contact.email, contact.email2, contact.email3]))