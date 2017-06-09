from model.contact import Contact
import random

def test_del_first_contact(app, db, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(Contact(firstname="deltest_firstname", lastname="deltest_last_name"))
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contacts_list(), key=Contact.id_or_max)

# def test_del_first_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="deltest_firstname", lastname="deltest_last_name"))
#     old_contacts = app.contact.get_contacts_list()
#     index = randrange(len(old_contacts))
#     app.contact.delete_contact_by_index(index)
#     new_contacts = app.contact.get_contacts_list()
#     assert len(old_contacts) - 1 == len(new_contacts)



    # old_contacts[index:index+1] = []
    # assert old_contacts == new_contacts

  # app.contact.create(Contact(firstname="test2", middlename="test", lastname="test", nickname="test",
        #                       title="newone", company="qa", address="Poland", home="-", mobile="-", work="-",
        #                       fax="-",
        #                       email="test@test.pl", email3="-", email2="-", homepage="-", byear="1980",
        #                       ayear="1990", address2="Poland, lodz"))