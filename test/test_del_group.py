


def test_delete_first_group(app):
    app.session.login("secret", "admin")
    app.group.delete_first_group()
    app.session.logout()
