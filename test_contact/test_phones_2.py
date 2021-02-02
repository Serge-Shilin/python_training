import re
from model.contact import Contact


def test_contact_check(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test"))
    contacts_ui = app.contact.get_contacts_list()
    contacts_db = db.get_contact_list()
    assert sorted(contacts_ui, key=Contact.id_or_max) == sorted(contacts_db, key=Contact.id_or_max)

    for contact_ui in contacts_ui:
        contact_db = list(filter(lambda x: x.id == contact_ui.id, contacts_db))[0]
        assert contact_ui.firstname == clear(contact_db.firstname)
        assert contact_ui.lastname == clear(contact_db.lastname)
        assert contact_ui.address == clear(contact_db.address)
        #assert contact_ui.all_phones_from_home_page == merge_phones_like_on_home_page(contact_db)
        #assert contact_ui.all_emails_from_home_page == merge_emails_like_on_home_page(contact_db)


def clear(s):
    return re.sub("^\s+|\n|\r|\s+$", "", s)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                        [contact.email, contact.email2, contact.email3]))))


def clear_for_phones(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_for_phones(x),
                                filter(lambda x: x is not None,
                                        [contact.home, contact.mobile, contact.work, contact.phone2]))))