# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_contacts_list()
    app.group.create(Group(u"группа", u"группа", u"группа"))
    new_groups = app.group.get_contacts_list()
    assert len(old_groups) + 1 == len(new_groups)

