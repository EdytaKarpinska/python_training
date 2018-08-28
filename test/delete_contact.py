from model.group import Contact

def test_delete_contact(app):
    if app.contact.count_c() == 0:
        app.contact.create_c(Contact(userfirstname="name_del"))
    app.contact.delete_first_contact()
