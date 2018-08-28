from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create_g(Group(name="test_m"))
    app.group.modify_first_group(Group(name="NewGroup"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create_g(Group(header="test_m"))
    app.group.modify_first_group(Group(header="NewHeader"))
