# -*- coding: utf-8 -*-
from model.group import Contact
from sys import maxsize


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(userfirstname="Edyta", usermiddlename="EK", userlastname="Karpinska", nick="EiKi", title="Title", company="Python", address="My address", home="Home",
                               mobile="789456123", workphone="85965784", fax="879654", email="test@localhost.com", email2="test2@localhost.com",
                               email3="test3@localhost.com", homepage="homepage", birthyear="1990", anniversaryyear="2015", secondaddres="Secondary address", homephone="Second home", notes="Note")
    app.contact.create_c(contact)
    # do usuniecia new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count_c()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_maxc) == sorted(new_contacts, key=Contact.id_or_maxc)
