# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login("secret", "admin")
    app.group.create(Group(u"группа", u"группа", u"группа"))
    app.session.logout()

