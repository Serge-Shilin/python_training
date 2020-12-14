import pytest
from model.contact import Contact
from application import Application


@pytest.fixture
def app1(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.fill_contact_form(
        Contact(firstname="Сергей", middlename="Сергеевич", lastname="Сергеев", nickname="Серега", address="г. Казань",
                homephone="11111", mobile="22222",
                workphone="333333", mail="sergei@gmail.com", bday="", bmounth="May", byear="1975"))
    app.session.logout()
