


def test_update_first_group(app):
    app.group.update_first_group()
    app.session.logout()