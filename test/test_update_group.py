
from model.group import Group
from random import randrange


def test_update_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New group")
    group.id = old_groups[index].id
    app.group.update_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[index] = group
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

