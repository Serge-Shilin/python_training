import re
from model.contact import Contact
from random import randrange


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contacts_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.fax == contact_from_edit_page.fax


def test_other_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Иван", middlename="Иванович", lastname="Иванов",
                                   homephone="111", mobile="111", work="111",
                                   address="Казань",
                                   fax="111", email="111u", email2="111",
                                   email3="111"))
    list_contact = app.contact.get_contacts_list()
    index = randrange(len(list_contact))
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_emails_from_home_page == merge_all_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.lastname == merge_lastname_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == merge_firstname_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.address == merge_address_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[(),-]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.homephone, contact.mobile, contact.work, contact.fax]))))


def merge_all_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))


def merge_firstname_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.firstname]))))


def merge_lastname_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.lastname]))))


def merge_address_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.address]))))

