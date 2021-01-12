from model.contact import Contact


def test_new_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contacts_list()
    app.contact.contact_create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)






