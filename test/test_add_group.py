# -*- coding: utf-8 -*-
from model.group import Group


def test_test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create_g(Group(name="Python Group", header="This is the Logo", footer="Here we have a group footer"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create_g(Group(name="", header="", footer=""))
    app.session.logout()
