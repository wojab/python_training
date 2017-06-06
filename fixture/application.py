#from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.android.webdriver import WebDriver

from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from selenium import webdriver

class Application:
    def __init__(self, browser="firefox", base_url="http://localhost/addressbook/"):
        if browser =="firefox":
           self.wd =webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "Ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError ("Unrecognized browser %s" % browser)

       # self.wd.implicitly_wait(2)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        #self.open_home_page()
        self.base_url=base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

