from model.group import Contact

def test_delete_contact(app):
    if app.contact.count_c() == 0:
        app.contact.create_c(Contact(userfirstname="name_del"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
