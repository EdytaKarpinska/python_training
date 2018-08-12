from selenium.webdriver.firefox.webdriver import WebDriver
from fixture_contact.session_contact import SessionContactHelper
from fixture_contact.contact2 import ContactHelper

class ContactApplication:
    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.sessions = SessionContactHelper(self)
        self.contact2 = ContactHelper(self)

    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/addressbook/")

    def destroy(self):
        self.wd.quit()