from model.contact import Contact
import re


def test_contact_on_home_page_and_db(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.contact_create(Contact(firstname="Иван", middlename="Иванович", lastname="Иванов",
                                   homephone="111", mobile="111", work="111",
                                   address="Казань",
                                   fax="111", email="111u", email2="111",
                                   email3="111"))
    contacts_from_home_page = app.contact.get_contacts_list()
    contacts_from_db = db.get_contact_list()
    list_contacts_from_home_page = list(
        map(lambda y: (y.id, y.firstname, y.lastname, y.all_emails_from_home_page, y.all_phones_from_home_page, y.address), contacts_from_home_page))
    list_contacts_from_db = list(
        map(lambda y: (y.id, y.firstname, y.lastname, merge_phones_like_on_home_page(y),
                       merge_emails_like_on_home_and_edit_page(y), y.address), contacts_from_db))
    assert sorted(list_contacts_from_home_page, key=lambda y: y[0]) == sorted(list_contacts_from_db, key=lambda y: y[0])


def clear(s):
    return re.sub("[() -]", "", s)


def merge_address_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.address]))))



def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobile, contact.work, contact.fax]))))


def merge_emails_like_on_home_and_edit_page(contact):
    return "\n".join(filter(lambda x: x != "" and x is not None, [contact.email, contact.email2, contact.email3]))