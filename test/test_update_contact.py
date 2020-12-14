

def test_contact_update(app):
    app.session.login(username="admin", password="secret")
    app.contact.test_contact_update()
    app.session.logout()
