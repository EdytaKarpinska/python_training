# -*- coding: utf-8 -*-
import pytest
from model_contact.contact import Contact
from fixture_contact.application_contact import ContactApplication

@pytest.fixture
def app(request):
    fixture = ContactApplication()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.sessions.login(username="admin", password="secret")
    app.create_contact(Contact(userfirstname="Edyta", usermiddlename="EK", userlastname="Karpinska", nick="EiKi", title="Title", company="Python", address="My address", home="Home",
                            mobile="789456123", workphone="85965784", fax="879654", email="test@localhost.com", email2="test2@localhost.com",
                            email3="test3@localhost.com", homepage="homepage", birthyear="1990", anniversaryyear="2015", secondaddres="Secondary address", homephone="Second home", notes="Note"))
    app.sessions.logout()

