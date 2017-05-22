from model.contact import Contact

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_add_contact_page(self):
        wd = self.app.wd
   #     if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_css_selector("img[alt='Edit']")) > 0):
        wd.find_element_by_link_text("add new").click()

    def return_to_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home")

    def create(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.implicitly_wait(5)
        self.contact_cache = None
      #  self.return_to_contact_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        # wd.find_element_by_name("middlename").send_keys(contact.middlename)
        # wd.find_element_by_name("lastname").click()
        # wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        # wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # wd.find_element_by_name("title").click()
        # wd.find_element_by_name("title").clear()
        # wd.find_element_by_name("title").send_keys(contact.title)
        # wd.find_element_by_name("company").click()
        # wd.find_element_by_name("company").clear()
        # wd.find_element_by_name("company").send_keys(contact.company)
        # wd.find_element_by_name("address").click()
        # wd.find_element_by_name("address").clear()
        # wd.find_element_by_name("address").send_keys(contact.address)
        # wd.find_element_by_name("home").click()
        # wd.find_element_by_name("home").clear()
        # wd.find_element_by_name("home").send_keys(contact.home)
        # wd.find_element_by_name("mobile").click()
        # wd.find_element_by_name("mobile").clear()
        # wd.find_element_by_name("mobile").send_keys(contact.mobile)
        # wd.find_element_by_name("work").click()
        # wd.find_element_by_name("work").clear()
        # wd.find_element_by_name("work").send_keys(contact.work)
        # wd.find_element_by_name("fax").click()
        # wd.find_element_by_name("fax").clear()
        # wd.find_element_by_name("fax").send_keys(contact.fax)
        # wd.find_element_by_name("email").click()
        # wd.find_element_by_name("email").clear()
        # wd.find_element_by_name("email").send_keys(contact.email)
        # wd.find_element_by_name("email3").click()
        # wd.find_element_by_name("email3").clear()
        # wd.find_element_by_name("email3").send_keys(contact.email3)
        # wd.find_element_by_name("email2").click()
        # wd.find_element_by_name("email2").clear()
        # wd.find_element_by_name("email2").send_keys(contact.email2)
        # wd.find_element_by_name("homepage").click()
        # wd.find_element_by_name("homepage").clear()
        # wd.find_element_by_name("homepage").send_keys(contact.homepage)
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
        # wd.find_element_by_name("ayear").click()
        # wd.find_element_by_name("ayear").clear()
        # wd.find_element_by_name("ayear").send_keys(contact.ayear)
        # wd.find_element_by_name("address2").click()
        # wd.find_element_by_name("address2").clear()
        # wd.find_element_by_name("address2").send_keys(contact.address2)

    def details_of_first_contact(self):
        wd = self.app.wd
        self.return_to_contact_page()
        #click on details
        wd.find_element_by_css_selector("img[alt='Details']").click()

    def edit_contact(self):
        wd = self.app.wd
        self.return_to_contact_page()
        #edit
        wd.find_element_by_css_selector("img[alt='Edit']").click()
        #change value
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("olaf")
        #submit changes
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def del_first_contact(self):
        wd = self.app.wd
        self.return_to_contact_page()
        #select first group
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//div[@id ='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.return_to_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    # def get_contacts_list(self):
    #     if self.contact_cache is None:
    #         wd = self.app.wd
    #         self.return_to_contact_page()
    #         self.contact_cache = []
    #         for element in wd.find_elements_by_css_selector("tr.odd"):
    #             text = element.text
    #             id = element.find_element_by_name("selected[]").get_attribute("value")
    #             self.contact_cache.append(Contact(lastname=text, id=id))
    #     return list(self.contact_cache)

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_contact_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                name = cells[2].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=name, lastname=lastname, id=id))
        return list(self.contact_cache)




