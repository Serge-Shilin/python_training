from model.contact import Contact


def test_contact_firstname(app):
    app.contact.contact_update(
        Contact(firstname="aaaaaa", middlename="aaaaaaa", lastname="aaaaaaa", nickname="aaaaa", address="aaaaa",
                homephone="777777", mobile="77777",
                workphone="77777", mail="@", bday="", bmounth="", byear="1111"))


def test_contact_update_lastname(app):
    app.contact.contact_update(
        Contact(firstname="sssssss", middlename="ssss", lastname="sssssss", nickname="sssssss", address="ssssss", homephone="99999", mobile="999999",
                workphone="99999", mail="@", byear="1901"))
