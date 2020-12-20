from model.contact import Contact



def test_new_contact(app):
    app.contact.contact_create(
        Contact(firstname="Сергей", middlename="Сергеевич", lastname="Сергеев", nickname="Серега", address="г. Казань",
                homephone="11111", mobile="22222",
                workphone="333333", mail="sergei@gmail.com", bday="", bmounth="May", byear="1975"))

