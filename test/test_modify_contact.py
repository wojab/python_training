from model.contact import Contact
from random import randrange

def test_edit_contact(app, db, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(Contact(firstname="edited", lastname="edited"))

    old_contacts = db.get_contacts_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Random edited michal", lastname="Random edited aga")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(contact.id, contact)
    new_contacts = db.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_edit_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="test", middlename="test", lastname="test3", nickname="test",
#                                     title="newone", company="qa", address="Poland", home="-", mobile="-", work="-",
#                                     fax="-",
#                                     email="test@test.pl", email3="-", email2="-", homepage="-", byear="1980",
#                                     ayear="1990", address2="Poland, lodz"))
#     app.contact.edit_contact()

