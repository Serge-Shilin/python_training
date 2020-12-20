from model.group import Group



def test_update_group_name(app):
    app.group.update_group(Group(name="New group"))

def test_update_group_header(app):
    app.group.update_group(Group(header="New header"))

