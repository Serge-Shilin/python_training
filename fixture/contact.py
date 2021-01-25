from selenium.webdriver.support.select import Select
from fixture.db import DbFixture
from model.contact import Contact
import re


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
        self.change_field_value("work", contact.work)
        self.change_field_value("phone2", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
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

    def contact_update(self):
        self.contact_update_by_index(0)

    def contact_update_by_index(self, index, new_contact_data):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
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
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                all_emails = cells[4].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, address=address, all_emails_from_home_page=all_emails, id=id, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(id=id, firstname=firstname, lastname=lastname, address=address, homephone=homephone, work=workphone,
                       mobile=mobilephone, fax=secondaryphone, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, work=workphone,
                       mobile=mobilephone, fax=secondaryphone)

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_elements_by_css_selector("div.msgbox")
        self.app.open_home_page()
        self.contact_cache = None

    def count_group(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def select_none(self):
        wd = self.app.wd
        self.app.open_home_page()
        Select(wd.find_element_by_name("group")).select_by_visible_text("[none]")
        wd.find_element_by_xpath("//option[@value='[none]']").click()

    def select_group(self):
        wd = self.app.wd
        self.app.open_home_page()
        Select(wd.find_element_by_name("to_group")).select_by_visible_text("name25HM")
        wd.find_element_by_xpath("(//option[@value='119'])[2]").click()

    def add_contact_in_group(self):
        wd = self.app.wd
        #self.app.open_home_page()
        #Select(wd.find_element_by_name("group")).select_by_visible_text("[none]")
        #wd.find_element_by_xpath("//option[@value='[none]']").click()
        #self.app.contact_create()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_name("to_group")).select_by_visible_text("name25HM")
        wd.find_element_by_xpath("(//option[@value='119'])[2]").click()
        wd.find_element_by_name("add").click()
        self.app.open_home_page()

    def remove_contact_in_group(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("group").click()
        Select(wd.find_element_by_name("group")).select_by_visible_text("name25HM")
        wd.find_element_by_xpath("//option[@value='119']").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("remove").click()
        #self.accept_next_alert = True
        #wd.find_element_by_xpath("//input[@value='Delete']").click()
        #wd.switch_to_alert().accept()
        #wd.find_elements_by_css_selector("div.msgbox")
        wd.find_element_by_link_text("home").click()






