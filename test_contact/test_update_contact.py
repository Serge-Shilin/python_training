from model.contact import Contact


def test_contact_update(app):
    app.session.login(username="admin", password="secret")
    app.contact.fill_contact_form(
        Contact(firstname="11111", middlename="2222222", lastname="3333333", nickname="444444", address="55555",
                homephone="11111", mobile="22222",
                workphone="333333", mail="22222", bday="1", bmounth="May", byear="1901"))
    app.session.logout()
