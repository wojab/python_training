from model.contact import Contact

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename="test", lastname="test3", nickname="test",
                              title="newone", company="qa", address="Poland", home="-", mobile="-", work="-",
                              fax="-",
                              email="test@test.pl", email3="-", email2="-", homepage="-", byear="1980",
                              ayear="1990", address2="Poland, lodz"))
    app.contact.edit_contact()
