from model.group import Contact
from random import randrange

def test_delete_contact(app):
    if app.contact.count_c() == 0:
        app.contact.create_c(Contact(userfirstname="name_del"))
    old_contacts = app.contact.get_contact_list()
    index_con = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index_con)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index_con:index_con+1] = []
    assert old_contacts == new_contacts
