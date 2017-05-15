from sys import maxsize

class Contact:
    def __init__(self, name = None, firstname = None, lastname = None,id = None):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
        self.name = name

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name and self.lastname == other.lastname

    def id_or_max(gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize

# def __init__(self, firstname, middlename, lastname, nickname, title, company, address, home, mobile, work,
    #                    fax, email, email3, email2, homepage, byear, ayear, address2):
    #     self.firstname=firstname
    #     self.middlename=middlename
    #     self.lastname=lastname
    #     self.nickname=nickname
    #     self.title=title
    #     self.company=company
    #     self.address=address
    #     self.home=home
    #     self.mobile=mobile
    #     self.work=work
    #     self.fax=fax
    #     self.email=email
    #     self.email3=email3
    #     self.email2=email2
    #     self.homepage=homepage
    #     self.byear=byear
    #     self.ayear=ayear
    #     self.address2=address2