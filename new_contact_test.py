import pytest
from contact import Contact
from application1 import Application1

@pytest.fixture
def app1(request):
    fixture = Application1()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_new_contact(app1):
    app1.login(username="admin", password="secret")
    app1.fill_contact_form(Contact(firstname="Сергей", middlename="Сергеевич", lastname="Сергеев", nickname="Серега", address="г. Казань", homephone="11111", mobile="22222",
                               workphone="333333", mail="sergei@gmail.com", bday="", bmounth="May", byear="1975"))
    app1.logout()

def test_new_contact_empty(app1):
    app1.login(username="admin", password="secret")
    app1.fill_contact_form(Contact(firstname="", middlename="", lastname="", nickname="", address="", homephone="", mobile="",
                               workphone="", mail="", bday="", bmounth="June", byear=""))
    app1.logout()
