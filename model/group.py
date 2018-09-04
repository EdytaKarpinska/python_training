from sys import maxsize

class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

class Contact:
    def __init__(self, userfirstname=None, usermiddlename=None, userlastname=None, nick=None, title=None, company=None, address=None, home=None,
                mobile=None, workphone=None, fax=None, email=None, email2=None, email3=None, homepage=None, birthyear=None, anniversaryyear=None, secondaddres=None,
                homephone=None, notes=None, id=None):
        self.userfirstname = userfirstname
        self.usermiddlename = usermiddlename
        self.userlastname = userlastname
        self.nick = nick
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birthyear = birthyear
        self.anniversaryyear = anniversaryyear
        self.secondaddres = secondaddres
        self.homephone = homephone
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.userfirstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.userfirstname == other.userfirstname

    def id_or_maxc(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

