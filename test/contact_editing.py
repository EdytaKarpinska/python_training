from model.group import Contact


def test_edit_contact_firstname(app):
    if app.contact.count_c() == 0:
        app.contact.create_c(Contact(userfirstname="name_modify"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(userfirstname="NewName")
    contact.id = old_contacts[0].id
    app.contact.editing_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_maxc) == sorted(new_contacts, key=Contact.id_or_maxc)


