# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login("secret", "admin")
    app.fill_group_form(Group( u"группа", u"группа", u"группа"))
    app.logout()

