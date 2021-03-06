from model.contact import Contact
from selenium.webdriver.support.ui import Select
import re

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_add_contact_page(self):
        wd = self.app.wd
   #     if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_css_selector("img[alt='Edit']")) > 0):
        wd.find_element_by_link_text("add new").click()

    def return_to_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_contact_page()
        wd.implicitly_wait(5)
        self.contact_cache = None
      #  self.return_to_contact_page()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        # self.change_field_value("middlename", contact.middlename)
        # self.change_field_value("nickname", contact.nickname)
        # self.change_field_value("title", contact.title)
        # self.change_field_value("company", contact.company)
        # self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("phone2", contact.secondaryphone)
        # self.change_field_value("fax", contact.fax)
        # self.change_field_value("email", contact.email)
        # self.change_field_value("email3", contact.email3)
        # self.change_field_value("email2", contact.email2)
        # self.change_field_value("homepage", contact.homepage)
        # # birtday day
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
        #     wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
        # # birthday month
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
        #     wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
        # wd.find_element_by_name("byear").click()
        # wd.find_element_by_name("byear").clear()
        # # birthday year
        # wd.find_element_by_name("byear").send_keys(contact.byear)
        # # anniversary day
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[4]").is_selected():
        #     wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[4]").click()
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[4]").is_selected():
        #     wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[4]").click()
        # # anniversary month
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[2]").is_selected():
        #     wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[2]").click()
        # # anniversary year
        # self.change_field_value("ayear", contact.ayear)
        # self.change_field_value("address2", contact.address2)

    def details_of_first_contact(self):
        wd = self.app.wd
        self.return_to_contact_page()
        #click on details
        wd.find_element_by_css_selector("img[alt='Details']").click()

    def edit_contact(self):
        wd = self.app.wd
        self.return_to_contact_page()
        # edit
        wd.find_element_by_css_selector("img[alt='Edit']").click()
        # change value
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("olaf")
        # submit changes
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.return_to_contact_page()
        self.select_contact_by_index(index)
        wd.find_elements_by_css_selector("img[alt='Edit']")[index].click()
       # wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        wd.implicitly_wait(10)
        self.contact_cache = None

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.return_to_contact_page()
        print(id)
      #  self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@id= '%s']/../following-sibling::td[@class='center']/a/img[@alt='Edit']"%id).click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        wd.implicitly_wait(10)
        self.contact_cache = None

    def del_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.return_to_contact_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//div[@id ='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        wd.implicitly_wait(10)
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.return_to_contact_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//div[@id ='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        wd.implicitly_wait(10)
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value = '%s']" % id).click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def count(self):
        wd = self.app.wd
        self.return_to_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_contact_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                all_emails = cells[4].text
                all_phones = cells[5].text
                all_addresses = cells[3].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname,
                                                  id=id, all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails, all_addresses_from_home_page=all_addresses))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        secondaryaddress = wd.find_element_by_name("address2").get_attribute("value")

        return Contact(firstname=firstname, lastname=lastname,
                       id=id, homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone,
                       email=email, email2=email2, email3=email3,
                       address=address, secondaryaddress = secondaryaddress)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.return_to_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.return_to_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contacts_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        firstname =  text.split(" ")[0]

        return Contact(homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone, firstname=firstname)

    def add_contact_to_group(self, id):
        wd = self.app.wd
        self.return_to_contact_page()
        self.select_contact_by_id(id)
        Select(wd.find_element_by_name("to_group")).select_by_visible_text("PowiazGrupa")
        wd.find_element_by_name("add").click()

    def open_groups_page(self):
        wd = self.app.wd
        Select(wd.find_element_by_name("group")).select_by_visible_text("PowiazGrupa")

    def del_contact_from_group(self, id):
        wd = self.app.wd
        self.return_to_contact_page()
        self.open_groups_page()
        self.select_contact_by_id(id)
        wd.find_element_by_name("remove").click()














