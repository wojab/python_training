from model.contact import Contact


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contacts_list()
    app.contact.create(contact)
    new_contacts = db.get_contacts_list()
    old_contacts.append(contact)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_add_contact(app, json_contacts):
#     contact = json_contacts
#     old_contacts = app.contact.get_contacts_list()
#     app.contact.create(contact)
#     assert len(old_contacts) + 1 == app.contact.count()
#     new_contacts = app.contact.get_contacts_list()
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




# def test_add_contact(app):
#     old_contacts = app.contact.get_contacts_list()
#     contact = Contact(firstname="wojtek", lastname="wojtasikk", homephone="123456789", mobilephone="987654321", workphone="5647382910", secondaryphone="546123512")
#     app.contact.create(contact)
#     assert len(old_contacts) + 1 == app.contact.count()
#     new_contacts = app.contact.get_contacts_list()
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    # app.contact.create(Contact(firstname="wojtek", middlename="marek", lastname="wojtasik", nickname="nico",
    #                           title="newone", company="qa", address="Poland", home="-", mobile="-", work="-",
    #                           fax="-",
    #                           email="test@test.pl", email3="-", email2="-", homepage="-", byear="1980",
    #                           ayear="1990", address2="Poland, lodz"))

