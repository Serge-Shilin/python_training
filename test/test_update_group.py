from model.group import Group



def test_update_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_contacts_list()
    app.group.update_group(Group(name="New group"))
    new_groups = app.group.get_contacts_list()
    assert len(old_groups) == len(new_groups)

def test_update_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_contacts_list()
    app.group.update_group(Group(header="New header"))
    new_groups = app.group.get_contacts_list()
    assert len(old_groups) == len(new_groups)
