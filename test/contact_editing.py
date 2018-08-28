from model.group import Contact


def test_edit_contact_firstname(app):
    if app.contact.count_c() == 0:
        app.contact.create_c(Contact(userfirstname="name_modify"))
    app.contact.editing_first_contact(Contact(userfirstname="NewName"))


