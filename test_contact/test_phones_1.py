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


def clear(s):
    return re.sub("[./() -]", "", s)


def merge_phones_like_from_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobile, contact.work, contact.fax]))))


def merge_emails_like_from_home_page(contact):
    return "\n".join(filter(lambda x: x != "" and x is not None, [contact.email, contact.email2, contact.email3]))