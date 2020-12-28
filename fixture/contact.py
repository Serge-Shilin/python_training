
from model.contact import Contact
from random import randrange

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("http://localhost/addressbook/") and len(wd.find_elements_by_name("searchstring")) > 0:
            return
        wd.find_element_by_link_text("home").click()

    def submit_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("email", contact.mail)
        self.change_field_value("byear", contact.byear)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_new_contacts(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def select_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def test_delete_first_contact(self):
        self.test_delete_contact_by_index(0)


    def test_delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_elements_by_css_selector("div.msgbox")
        self.app.open_home_page()
        self.contact_cache = None

    def contact_update(self, new_contact_data):
        self.contact_update_by_index(0)


    def contact_update_by_index(self, index, new_contact_data):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None


    def contact_create(self, new_contact_data):
        wd = self.app.wd
        self.open_new_contacts()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))


    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home_page()
            self.contact_cache = []
            x = 1
            for element in wd.find_elements_by_name("entry"):
                x = x + 1
                lastname = element.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" + str(x) + "]/td[2]").text
                firstname = element.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" + str(x) + "]/td[3]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname,  id=id))
        return list(self.contact_cache)




