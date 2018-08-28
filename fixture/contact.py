from model.group import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_return_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def create_c(self, contact):
        wd = self.app.wd
        self.open_return_contacts_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.open_return_contacts_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value_contact("firstname", contact.userfirstname)
        self.change_field_value_contact("middlename", contact.usermiddlename)
        self.change_field_value_contact("lastname", contact.userlastname)
        self.change_field_value_contact("nickname", contact.nick)
        self.change_field_value_contact("title", contact.title)
        self.change_field_value_contact("company", contact.company)
        self.change_field_value_contact("address", contact.address)
        self.change_field_value_contact("home", contact.home)
        self.change_field_value_contact("mobile", contact.mobile)
        self.change_field_value_contact("work", contact.workphone)
        self.change_field_value_contact("fax", contact.fax)
        self.change_field_value_contact("email", contact.email)
        self.change_field_value_contact("email2", contact.email2)
        self.change_field_value_contact("email3", contact.email3)
        self.change_field_value_contact("homepage", contact.homepage)
        self.change_field_value_contact("byear", contact.birthyear)
        self.change_field_value_contact("ayear", contact.anniversaryyear)
        self.change_field_value_contact("address2", contact.secondaddres)
        self.change_field_value_contact("phone2", contact.homephone)
        self.change_field_value_contact("notes", contact.notes)

#        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
#            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
#        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").is_selected():
#            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").click()

#        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[5]").is_selected():
#            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[5]").click()
#        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[8]").is_selected():
#            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[8]").click()

    def change_field_value_contact(self, field_name_contact, text_contact):
        wd = self.app.wd
        if text_contact is not None:
            wd.find_element_by_name(field_name_contact).click()
            wd.find_element_by_name(field_name_contact).clear()
            wd.find_element_by_name(field_name_contact).send_keys(text_contact)


    def delete_first_contact(self):
        wd = self.app.wd
        self.open_return_contacts_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        wd.switch_to.alert.accept()
        self.open_return_contacts_page()


    def editing_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_return_contacts_page()
        wd.find_element_by_name("selected[]").click()
        #wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(new_contact_data)
        #wd.switch_to.alert.accept()
        wd.find_element_by_name("update").click()
        self.open_return_contacts_page()


    def count_c(self):
        wd = self.app.wd
        self.open_return_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))