from model.group import Contact
from random import randrange

def test_edit_contact_firstname(app):
    if app.contact.count_c() == 0:
        app.contact.create_c(Contact(userfirstname="name_modify"))
    app.contact.editing_first_contact(Contact(userfirstname="NewName"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(userfirstname="NewName")
    contact.id = old_contacts[0].id
    app.contact.editing_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_maxc) == sorted(new_contacts, key=Contact.id_or_maxc)

def test_edit_firstname_random_contact(app):
    if app.contact.count_c() == 0:
        app.contact.create_c(Contact(userfirstname="name_modify"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(userfirstname="NewName")
    contact.id = old_contacts[index].id
    app.contact.editing_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_maxc) == sorted(new_contacts, key=Contact.id_or_maxc)


