from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="wojtek", middlename="marek", lastname="wojtasik", nickname="nico",
                              title="newone", company="qa", address="Poland", home="-", mobile="-", work="-",
                              fax="-",
                              email="test@test.pl", email3="-", email2="-", homepage="-", byear="1980",
                              ayear="1990", address2="Poland, lodz"))
    app.session.logout()
