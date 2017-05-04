from model.contact import Contact

def test_details_of_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename="test", lastname="test", nickname="test",
                              title="newone", company="qa", address="Poland", home="-", mobile="-", work="-",
                              fax="-",
                              email="test@test.pl", email3="-", email2="-", homepage="-", byear="1980",
                              ayear="1990", address2="Poland, lodz"))
    app.contact.details_of_first_contact()
