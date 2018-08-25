# -*- coding: utf-8 -*-
from model.group import Group


def test_test_add_group(app):
    app.group.create_g(Group(name="Python Group", header="This is the Logo", footer="Here we have a group footer"))


def test_add_empty_group(app):
    app.group.create_g(Group(name="", header="", footer=""))
