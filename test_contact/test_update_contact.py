from model.contact import Contact


def test_contact_update(app):
    app.session.login(username="admin", password="secret")
    app.contact.test_contact_update(Contact(firstname="1111", middlename="Сергеевич", lastname="Сергеев", nickname="Серега", address="г. Казань",
                homephone="11111", mobile="22222",
                workphone="333333", mail="sergei@gmail.com", bday="2", bmounth="May", byear="1975"))
    app.session.logout()
