from model.contact import Contact



def test_new_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="Сергей", middlename="Сергеевич", lastname="Сергеев", nickname="Серега", address="г. Казань",
                homephone="11111", mobile="22222",
                workphone="333333", mail="sergei@gmail.com", bday="", bmounth="May", byear="1975")
    app.contact.contact_create(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
