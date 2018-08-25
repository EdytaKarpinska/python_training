from model.group import Contact


def test_edit_contact_firstname(app):
    app.contact.editing_first_contact(Contact(userfirstname="NewName"))


