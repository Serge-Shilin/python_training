from model.group import Group



def test_update_group_name(app):
    app.session.login("secret", "admin")
    app.group.update_group(Group(name="New group"))
    app.session.logout()

def test_update_group_header(app):
    app.session.login("secret", "admin")
    app.group.update_group(Group(header="New header"))
    app.session.logout()

