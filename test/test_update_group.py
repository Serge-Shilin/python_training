from model.group import Group


def test_update_first_group(app):
    app.session.login("secret", "admin")
    app.group.create(Group(u"11111", u"11111", u"11111"))
    app.session.logout()