from model.contact import Contact
from random import randrange

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="edited", lastname="edited"))

    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Random edited firstname", lastname="Random edited lastname")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_edit_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="test", middlename="test", lastname="test3", nickname="test",
#                                     title="newone", company="qa", address="Poland", home="-", mobile="-", work="-",
#                                     fax="-",
#                                     email="test@test.pl", email3="-", email2="-", homepage="-", byear="1980",
#                                     ayear="1990", address2="Poland, lodz"))
#     app.contact.edit_contact()

