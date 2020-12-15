


def test_update_first_group(app):
    app.session.login("secret", "admin")
    app.group.update_first_group()
    app.session.logout()