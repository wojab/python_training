from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="wojtek", lastname="wojtasikk")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    # app.contact.create(Contact(firstname="wojtek", middlename="marek", lastname="wojtasik", nickname="nico",
    #                           title="newone", company="qa", address="Poland", home="-", mobile="-", work="-",
    #                           fax="-",
    #                           email="test@test.pl", email3="-", email2="-", homepage="-", byear="1980",
    #                           ayear="1990", address2="Poland, lodz"))


