
from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.contact_create(
            Contact(firstname="Сергей", middlename="Сергеевич", lastname="Сергеев", nickname="Серега",
                    address="г. Казань",
                    homephone="11111", mobile="22222",
                    workphone="333333", mail="sergei@gmail.com", bday="", bmounth="May", byear="1975"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.test_delete_first_contact()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)

