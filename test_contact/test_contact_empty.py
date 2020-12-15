

from model.contact import Contact


def test_new_contact_empty(app):
    app.session.login(username="admin", password="secret")
    app.contact.fill_contact_form(
        Contact(firstname="", middlename="", lastname="", nickname="", address="", homephone="", mobile="",
                workphone="", mail="", bday="", bmounth="June", byear=""))
    app.session.logout()

